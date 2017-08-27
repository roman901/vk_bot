from tinydb import Query


class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('karma', self.karma_command)
        #self.vk_bot.add_filter(self.ignore_filter)

    async def karma_command(self, sender, sender_id, message):
        message = message[5:]

        if sender < 2000000000:
            await self.vk_bot.send_message(sender, 'Karma works only in groupchats!')
            return

        db = self.vk_bot.database['karma_{}'.format(sender - 2000000000)]

        q = Query()
        res = db.search(q.user_id == sender_id)
        if not res:
            await self.vk_bot.send_message(sender, 'Your karma is 0')
        else:
            await self.vk_bot.send_message(sender, 'Your karma is {}'.format(res['value']))

    async def karma_filter(self, sender, sender_id, message):
        pass
