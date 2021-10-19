import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import TOKEN
import random

session = vk_api.VkApi(token=TOKEN)


def send_message(user_id, message):
	session.method("messages.send", {
		"user_id": user_id,
		"message": message,
		'random_id': 0
	})	


for event in VkLongPoll(session).listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me:
		text = event.text.lower()
		user_id = event.user_id

		if text == "hello" or text == "Hello" or text == "Привет" or text == "привет":
			send_message(user_id, "Привет")

		elif text == "Как дела?" or text == "Как дела" or text == "How are you?" or text == "как ты?" or text == "как ты" or text == "как дела?":
			send_message(user_id, "Нормально, a вы как?")

		elif text == "I'm fine" or text == "отлично" or text == "Я в порядке" or text == "нормально":
			send_message(user_id, "Я рад за вас")

		elif text == "тоже рад"	or text == "тоже рада" or text == "ok" or text == "Ок" or text == "ок" or text == "понятно":
			send_message(user_id, "ок")

			

		else:
			print("Error occured!")
			input("Press any key to exit...")
			break

