class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('stop', self.stop, admin_only=True)

    async def stop(self, sender, sender_id, message):
        await self.vk_bot.send_message(sender, 'Bot stopped')
        self.vk_bot.stop()
