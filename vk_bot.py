import os
from import_string import import_string

config_file = os.environ.get('VK_BOT_CONFIG', 'config.local.LocalConfig')
print('Using {}'.format(config_file))

obj = import_string(config_file)
