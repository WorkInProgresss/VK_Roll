#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from random import randint

import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from sys_select import clear


def main():
    vk, longpoll = connect()

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            print('Для меня от: ', end='')

            print(event.obj.from_id)

            print('Текст:', event.obj.text)
            print()

            name = vk.users.get(user_ids=event.obj.from_id)
            name = name[0]['first_name']

            # p_mass = vk.messages.getConversationMembers(
            #     peer_id=2000000002
            # )
            # p_id = ['response'][d['id'] for d in 'profiles']

            rand = randint(0, 9223372036854775807)

            vk.messages.send(
                chat_id=event.chat_id,
                message=(str(clear(event.obj.text, event.obj.from_id))),
                random_id=rand
            )


def connect():
    session = requests.Session()

    # Очистка файла логов
    log = open('logs.txt', 'w', encoding='utf-8')
    log.write('None')
    log.close()
    print('Лог очищен')

    # Импорт токена из файла
    gr_token = open("token.txt", "r")
    gr_token = gr_token.read()

    # Авторизация группы:
    vk_session = vk_api.VkApi(token=gr_token)

    vk = vk_session.get_api()

    longpoll = VkBotLongPoll(vk_session, '172052571')
    return vk, longpoll


if __name__ == '__main__':
    main()
