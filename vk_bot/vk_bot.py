import logging
import os
import sys
import time
import asyncio
from aiovk import ImplicitSession, API
from aiovk.longpoll import LongPoll
from .config import Config
from .database import Database


class VKBot(object):
    def __init__(self):
        self.config = Config()
        self.database = Database(self)
        self.logger = logging.getLogger()

        self.commands = {}
        self.filters = []
        self.admin_commands = []

        self.start_time = int(time.time())
        self.running = True

        self.vk_api = None

    def run(self):
        self.init_logging()
        self.logger.info('Starting VKBot')

        self.logger.info('Init plugins')
        self.init_plugins()

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.init_vk())

        self.logger.info('Stopping bot')

    def init_logging(self):
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        self.logger.addHandler(sh)

        if self.config['DEBUG']:
            self.logger.setLevel(logging.DEBUG)

        if self.config['LOG_TO_FILE']:
            fh = logging.FileHandler(self.config['LOG_FILENAME'])
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

    def init_plugins(self):
        path = self.config['PLUGINS_PATH']
        sys.path.insert(0, path)
        for f in os.listdir(path):
            fname, ext = os.path.splitext(f)
            if ext == '.py':
                self.logger.debug('Found plugin {}'.format(fname))
                mod = __import__(fname)
                mod.Plugin(self)
                self.logger.debug('Loaded plugin {}'.format(fname))
        sys.path.pop(0)

    async def init_vk(self):
        vk_session = None
        if self.config['IMPLICIT']:
            vk_session = ImplicitSession(self.config['USER_LOGIN'], self.config['USER_PASSWORD'],
                                         self.config['APP_ID'], ['messages'])
        else:
            # TODO(spark): implement TokenSession
            pass

        self.logger.info('Auth in VK...')
        await vk_session.authorize()

        self.vk_api = vk_api = API(vk_session)
        vk_lp = LongPoll(vk_api, mode=0)

        while self.running:
            # Main working loop
            response = await vk_lp.wait()

            for action in response['updates']:
                if action[0] is 4:
                    message_id = action[1]
                    sender = action[3]
                    sender_id = sender
                    message = str(action[6])
                    self.logger.debug('Got message: {}'.format(message))

                    if sender > 2000000000:
                        # Groupchat
                        g_response = await vk_api.messages.getById(message_ids=message_id)
                        sender_id = g_response['items'][0]['user_id']

                    f_flag = False
                    for f in self.filters:
                        f_res = await f(sender, sender_id, message)
                        if f_res is False:
                            f_flag = True
                            continue

                    if f_flag:
                        continue

                    if message.startswith(self.config['COMMAND_SYMBOL']) and message[1] is not ' ':
                        message = message[1:]
                        flag = False
                        for c in self.commands:
                            if message.startswith(c) and not flag:
                                flag = True
                                command = message.split(' ')[0]
                                if command in self.admin_commands and sender_id not in self.config['ADMINS']:
                                    await self.send_message(sender, 'Access denied')
                                else:
                                    await self.commands[command](sender, sender_id, message)
                        if flag is False:
                            await self.send_message(sender, 'Command not found')

        vk_session.close()

    def add_command(self, name, func, admin_only=False):
        self.commands[name] = func
        if admin_only:
            self.admin_commands.append(name)

    def add_filter(self, func):
        self.filters.append(func)

    async def send_message(self, destination, message):
        await self.vk_api.messages.send(peer_id=destination,
                                   message='{}{}'.format(self.config['PREFIX'], message))

    def stop(self):
        self.running = False
