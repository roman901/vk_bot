from run import vk_bot


def c_ping():
    print('ping')

vk_bot.add_command('ping', c_ping)
