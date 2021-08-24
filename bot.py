from types import new_class
from requests.api import post
import telebot
from telega_bot import *

bot = telebot.TeleBot('1730976473:AAH8_0mE4gKm1_rUwf63asD6r2vZGqFcf-4')

title = [f'{i + 1}. {data_[i]["title"]}' for i in range(20)]
title = '\n'.join(title)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Выберите новость 1-20.\n\n' + title)
    bot.register_next_step_handler(message, choose)


def choose(message):
    try:
        global new
        new = int(message.text)
        if new > 0 and new < 20:
            bot.send_message(message.from_user.id, f"вы выбрали пост {new}. \nОписание или Фото?")
            bot.register_next_step_handler(message, select)
        else:
            bot.send_message(message.from_user.id, f"Неверная операция!,выберите еще раз.")
            bot.send_message(message.from_user.id, f"/start")
            bot.register_next_step_handler(message, start_command)
    except:
        bot.send_message(message.from_user.id, f"Неверная операция! try again!")
        bot.send_message(message.from_user.id, f"/start")


def select(message):
    if message.text == 'Описание'.lower() or message.text == '1':
        bot.send_message(message.from_user.id, data_[new]['info'])
    elif message.text == 'Фото'.lower() or message.text == '2':
        bot.send_message(message.from_user.id, data_[new]['img'])
    else:
        bot.send_message(message.from_user.id, 'ВЫ ВВЕЛИ НЕКОРРЕКТНО! TRY AGAIN')
        bot.register_next_step_handler(message, select)
        bot.register_next_step_handler(message, start_command)


bot.polling()