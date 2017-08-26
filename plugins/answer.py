class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_filter(self.answer)

    async def answer(self, sender, message):
        if message.endswith('нет') or message.endswith('Нет'):
            await self.vk_bot.send_message(sender, 'Пидора ответ')
