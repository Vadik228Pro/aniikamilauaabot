import telebot

import time
from time import sleep
import random

from telebot import types

bot = telebot.TeleBot('5351482321:AAFnDNgQjHK-O4jcxJtG5Jg601hBGTUYqLQ')



keyboard1 = telebot.types.InlineKeyboardMarkup()
keyboard1.row('Узнать кто я')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, узнай кто ты, нажав кнопку узнать кто я.', reply_markup=keyboard1)
    print(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'узнать кто я':
        perc = 0

    while(perc < 100):
        try:
            text = "Процесс выполнения..." + str(perc) + "%"
            bot.send_message(message.chat.id, text, reply_markup=None)

            perc += random.randint(1, 45)
            sleep(0)

        except FloodWait as e:
            sleep(e.x)

    bot.send_message(message.chat.id, "И так...", reply_markup=None)
    sleep(0.2)
    bot.send_message(message.chat.id, "Тебя зовут...", reply_markup=None)
    sleep(0.2)
    bot.send_message(message.chat.id, "Тебя зовут Аня.", reply_markup=None)
    sleep(0.2)
    bot.send_message(message.chat.id, "И ты милашка)", reply_markup=None)
    sleep(0.1)
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEjxhiZyWRai0pZ5iMhx-ZgoLVJBpnygACeAoAAuxscEp9E5FvOZm6EyQE", reply_markup=None)

# RUN
bot.polling(none_stop=True)