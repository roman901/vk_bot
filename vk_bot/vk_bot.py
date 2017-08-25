import logging
import os
import time
import asyncio
from aiovk import ImplicitSession, API
from aiovk.longpoll import LongPoll
from .config import Config


class VKBot(object):
    def __init__(self):
        self.config = Config()
        self.logger = logging.getLogger()

        self.commands = {}
        self.filters = []

        self.start_time = int(time.time())
        self.running = True

    def run(self):
        self.init_logging()
        self.logger.info('Starting VKBot')

        self.logger.info('Init plugins')
        self.init_plugins()

        #loop = asyncio.get_event_loop()
        #loop.run_until_complete(self.init_vk())

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
        # TODO(spark): move plugin dir to config
        plugins = os.listdir('plugins')
        for p in plugins:
            if p.endswith('.py') and not p.startswith('.'):
                self.logger.debug('Found plugin {}'.format(p))

                # TODO(spark): add capability to ignore plugins
                self.logger.debug('Try to load plugin {}'.format(p))
                filename = 'plugins/{}'.format(p)
                exec(compile(open(filename, "rb").read(), filename, 'exec'))

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

        vk_api = API(vk_session)
        vk_lp = LongPoll(vk_api, mode=0)

        while self.running:
            # Main working loop
            action = await vk_lp.wait()
            print(action['ts'])

        vk_session.close()

    def add_command(self, name, func):
        self.commands[name] = func

    def add_filter(self, func):
        self.filters.append(func)

    def stop(self):
        self.running = False
