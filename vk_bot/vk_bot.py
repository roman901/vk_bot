import logging
import os
import time
from .config import Config

commands = {}
filters = []


class VKBot(object):
    def __init__(self):
        self.config = Config()
        self.logger = logging.getLogger()

        self.start_time = int(time.time())

    def run(self):
        self.init_logging()
        self.logger.info('Starting VKBot')

        self.logger.info('Init plugins')
        self.init_plugins()

        commands['test']()

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
