import time


class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('uptime', self.uptime)

    async def uptime(self, vk_api, sender, message):
        await self.vk_bot.send_message(sender, 'Total uptime: {} seconds'.format(round(time.time() - self.vk_bot.start_time)))
