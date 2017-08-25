from import_string.base import import_string


class Config(dict):
    def apply(self, cfg):
        obj = import_string(cfg)
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)


class BaseConfig(object):
    DEBUG = False
    APP_ID = 0
    IMPLICIT = True
    USER_LOGIN = 'test@vk.com'
    USER_PASSWORD = 'password'
    LOG_TO_FILE = True
    LOG_FILENAME = 'vk_bot.log'

    START_SYM = '!'
    PREFIX = '[BOT] '
