from run import vk_bot


def c_test():
    print('Test passed')

vk_bot.add_command('test', c_test)
