import hashlib


class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('md5', self.md5)

    async def md5(self, sender, sender_id, message):
        message = message[4:]
        if len(message) is 0:
            await self.vk_bot.send_message(sender, 'Usage: !md5 text')
        else:
            await self.vk_bot.send_message(sender,
                                           'MD5 hash: {}'.format(hashlib.md5(message.encode('utf-8')).hexdigest()))
