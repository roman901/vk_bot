class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('ping', self.ping)

    def ping(self):
        # TODO(spark): Answer pong to VK API
        print('pong')
