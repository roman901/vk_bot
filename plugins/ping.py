class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('ping', self.ping)

    async def ping(self, vk_api, sender, message):
        await vk_api.messages.send(peer_id=sender,
                                  message='{}Pong'.format(self.vk_bot.config['PREFIX']))

