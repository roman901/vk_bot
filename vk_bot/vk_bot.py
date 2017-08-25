import logging
from .config import Config


class VKBot(object):
    def __init__(self):
        self.config = Config()
        self.logger = logging.getLogger()

    def run(self):
        self.init_logging()
        self.logger.info('Starting VKBot')

    def init_logging(self):
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)

        if self.config['DEBUG']:
            self.logger.setLevel(logging.DEBUG)

        if self.config['LOG_TO_FILE']:
            fh = logging.FileHandler(self.config['LOG_FILENAME'])
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

        self.logger.addHandler(sh)

