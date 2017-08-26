class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('ping', self.ping)

    async def ping(self, sender, sender_id, message):
        await self.vk_bot.send_message(sender, 'Pong')

