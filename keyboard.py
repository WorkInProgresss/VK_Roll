from random import randint

import settings
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def send(comm):
    key = ['d 1d20', 'd 2d20', 'd 3d20', 'd 4d20']
    return keyboard(key)


def keyboard(key):
    rand = randint(0, 9223372036854775807)

    vk_session = vk_api.VkApi(token=settings.TOKEN)
    vk = vk_session.get_api()

    keyboard = VkKeyboard(one_time=False)

    # 1 строка
    keyboard.add_button(key[0], color=VkKeyboardColor.DEFAULT)
    keyboard.add_button(key[1], color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_button(key[2], color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button(key[3], color=VkKeyboardColor.PRIMARY)

    vk.messages.send(
        chat_id=settings.DND,
        message='Roll',
        keyboard=keyboard.get_keyboard(),
        random_id=rand
    )


def main():
    rand = randint(0, 9223372036854775807)

    vk_session = vk_api.VkApi(token=settings.TOKEN)
    vk = vk_session.get_api()

    keyboard = VkKeyboard(one_time=False)

    # 1 строка
    keyboard.add_button('D&D', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('Coriolis', color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_button('Fate Core', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Eclipse Phase', color=VkKeyboardColor.PRIMARY)

    vk.messages.send(
        chat_id=settings.DND,
        message='Basic',
        keyboard=keyboard.get_keyboard(),
        random_id=rand
    )


if __name__ == '__main__':
    main()
