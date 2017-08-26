class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('ping', self.ping)

    async def ping(self, vk_api, sender, message):
        await self.vk_bot.send_message(sender, 'Pong')

