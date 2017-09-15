from tinydb import Query


class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('ignore', self.ignore_command, admin_only=True)
        self.vk_bot.add_filter(self.ignore_filter)
        self.db = self.vk_bot.database['ignore']

    async def ignore_command(self, sender, sender_id, message, attachment):
        message = message[7:]
        if len(message) > 0:
            q = Query()
            res = self.db.search(q.id == int(message))
            if not res:
                self.db.insert({'id': int(message)})
                await self.vk_bot.send_message(sender, 'Successful ignored')
            else:
                self.db.remove(q.id == int(message))
                await self.vk_bot.send_message(sender, 'Successful de-ignored')
        else:
            await self.vk_bot.send_message(sender, 'Usage: !ignore id')

    async def ignore_filter(self, sender, sender_id, message, attachment):
        q = Query()
        res = self.db.search(q.id == sender_id)
        if res:
            return False
        return True
