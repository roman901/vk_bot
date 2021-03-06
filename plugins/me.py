class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('me', self.me)

    async def me(self, sender, sender_id, message, attachment):
        msg = 'Information about me:\n'
        info = await self.vk_bot.vk_api.users.get(user_id=sender_id,
                                                  fields='bdate,city,country,status,followers_count,'
                                                         'nickname')
        info = info[0]
        msg += 'Name: {} {} {}\n'.format(info['first_name'], info['nickname'], info['last_name'])
        msg += 'Status: {}\n'.format(info['status'])
        if 'bdate' in info: msg += 'Birthday: {}\n'.format(info['bdate'])
        if 'country' in info and 'city' in info: msg += 'Location: {}, {}\n'.format(info['country']['title'], info['city']['title'])
        msg += 'Followers: {}\n'.format(info['followers_count'])
        await self.vk_bot.send_message(sender, msg)

