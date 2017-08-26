class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('stop', self.stop)

    async def stop(self, vk_api, sender, message):
        # TODO(spark): Answer pong to VK API
        await vk_api.messages.send(peer_id=sender,
                                   message='{}Bot stopped'.format(self.vk_bot.config['PREFIX']))
        self.vk_bot.stop()
