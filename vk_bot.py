import os
from vk_bot import VKBot

config_file = os.environ.get('VK_BOT_CONFIG', 'local_config.LocalConfig')
print('Start using {}'.format(config_file))

vk_bot = VKBot()
vk_bot.config.apply(config_file)
vk_bot.run()