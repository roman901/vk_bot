import os
from import_string.base import import_string

config_file = os.environ.get('VK_BOT_CONFIG', 'local_config.LocalConfig')
print('Start using {}'.format(config_file))

obj = import_string(config_file)
