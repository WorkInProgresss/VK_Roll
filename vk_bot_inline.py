import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from logic import clear


def main():
    session = requests.Session()

    # Авторизация группы:

    gr_token = open("token.txt", "r")
    gr_token = gr_token.read()

    vk_session = vk_api.VkApi(token=gr_token)

    vk = vk_session.get_api()

    longpoll = VkBotLongPoll(vk_session, '172052571')

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            print('Для меня от: ', end='')

            print(event.obj.from_id)

            print('Текст:', event.obj.text)
            print()

            name = vk.users.get(user_ids=event.obj.from_id)
            name = name[0]['first_name']
            vk.messages.send(
                chat_id=event.chat_id,
                message=str(name) + str(clear(event.obj.text))
            )

if __name__ == '__main__':
    main()