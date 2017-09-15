from tinydb import Query


class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('karma', self.karma_command)
        self.vk_bot.add_filter(self.karma_filter)

    async def karma_command(self, sender, sender_id, message, attachment):
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

    async def karma_filter(self, sender, sender_id, message, attachment):
        if sender > 2000000000:
            print(attachment)
            if 'fwd' in attachment:
                print(attachment['fwd'].split(':')[-1])
                msg_sender = int(attachment['fwd'].split('_')[0])

                if message == '++':
                    print(msg_sender, sender_id)
                    if msg_sender == sender_id:
                        await self.vk_bot.send_message(sender, 'You cannot do this')
                    else:
                        self.modify_karma(sender, sender_id, 1)
                elif message == '--':
                    if msg_sender == sender_id:
                        await self.vk_bot.send_message(sender, 'You cannot do this')
                    else:
                        self.modify_karma(sender, sender_id, -1)

    def modify_karma(self, sender, user_id, value):
        q = Query()
        db = self.vk_bot.database['karma_{}'.format(sender - 2000000000)]
        res = db.search(q.user_id == user_id)
        if not res:
            count = 0
        else:
            print(res)
            count = int(res['count'])
        db.update({'count': count+value})
