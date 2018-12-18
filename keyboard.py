from random import randint

import settings
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def keyboard(key, vk_obj):
    rand = randint(0, 9223372036854775807)

    vk_session = vk_api.VkApi(token=settings.TOKEN)
    vk = vk_session.get_api()

    keyboard = VkKeyboard(one_time=False)

    if key == 1:
        key = ['Текущая система', 'Удалить выбор', 'Changelog', 'Возврат']
    elif key == 2:
        key = ['D&D', 'Coriolis', 'Eclipse Phase', 'Возврат']
    else:
        return "No Key"

    # 1 строка
    keyboard.add_button(key[0], color=VkKeyboardColor.DEFAULT)
    keyboard.add_button(key[1], color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_button(key[2], color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button(key[3], color=VkKeyboardColor.PRIMARY)

    c_id = vk_obj.chat_id

    vk.messages.send(
        chat_id=c_id,
        message='Подменю',
        keyboard=keyboard.get_keyboard(),
        random_id=rand
    )


def basic(vk_obj):
    rand = randint(0, 9223372036854775807)

    vk_session = vk_api.VkApi(token=settings.TOKEN)
    vk = vk_session.get_api()

    keyboard = VkKeyboard(one_time=False)

    # 1 строка

    keyboard.add_button('Выбор системы', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Настройки', color=VkKeyboardColor.PRIMARY)

    c_id = vk_obj.chat_id

    vk.messages.send(
        chat_id=c_id,
        message='Меню',
        keyboard=keyboard.get_keyboard(),
        random_id=rand
    )