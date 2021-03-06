import time


class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('uptime', self.uptime)

    async def uptime(self, sender, sender_id, message, attachment):
        await self.vk_bot.send_message(sender,
                                       'Total uptime: {} seconds'.format(round(time.time() - self.vk_bot.start_time)))
