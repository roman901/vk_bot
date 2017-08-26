class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('stop', self.stop)

    def stop(self):
        # TODO(spark): Answer pong to VK API
        print('Bot stopped')
        self.vk_bot.stop()
