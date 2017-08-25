import logging
import os
from .config import Config


class VKBot(object):
    def __init__(self):
        self.config = Config()
        self.logger = logging.getLogger()
        self.plugins = []

    def run(self):
        self.init_logging()
        self.logger.info('Starting VKBot')

        self.logger.info('Init plugins')
        self.init_plugins()
        self.logger.info('Loaded {} plugins'.format(len(self.plugins)))

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
        plugins = os.listdir('plugins')
        for p in plugins:
            if p.endswith('.py') and not p.startswith('.'):
                self.logger.debug('Found plugin {}'.format(p))
                self.plugins.append(p)
