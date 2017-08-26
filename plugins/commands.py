class Plugin:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot
        self.vk_bot.add_command('commands', self.commands)

    async def commands(self, sender, message):
        msg = 'List of registered commands:\n'
        for c in self.vk_bot.commands:
            msg += c
            if c in self.vk_bot.admin_commands:
                msg += ' [admin command]'
            msg += '\n'
        await self.vk_bot.send_message(sender, msg)
