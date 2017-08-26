class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('me', self.me)

    async def me(self, sender, message):
        # TODO(spark): firstly make ability to get user_id from groupchat
        msg = 'Information about me:'

        await self.vk_bot.send_message(sender, msg)

