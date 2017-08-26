class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('stop', self.stop)

    async def stop(self, vk_api, sender, message):
        await self.vk_bot.send_message(sender, 'Bot stopped')
        self.vk_bot.stop()
