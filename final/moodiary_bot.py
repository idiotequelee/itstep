import telebot
import os
from treatment import Treatment


TOKEN = '1884663910:AAH80xZMIdE5901WCTYWlAw0U6HuL27vyco'

bot = telebot.TeleBot(TOKEN)

treatment = Treatment()


@bot.message_handler(commands=['start'])
def start(message):
    answer = treatment.start(message)
    bot.send_message(message.chat.id, 'Hello, '
                     + message.from_user.first_name +
                     '!\n' + answer)


@bot.message_handler(commands=['week'])
def week(message):
    answer = treatment.week(message)
    bot.send_message(message.chat.id, 'Hello, '
                     + message.from_user.first_name +
                     '!\n' + answer)


@bot.message_handler(commands=['stop'])
def stop(message):
    answer = treatment.stop(message)
    bot.send_message(message.chat.id, 'Hello, '
                     + message.from_user.first_name +
                     '!\n' + answer)


@bot.message_handler(content_types=["text"])
def text(message):  
    answer = treatment.text(message)
    bot.send_message(message.chat.id, 'Hello, '
                     + message.from_user.first_name +
                     '!\n' + answer)


if __name__ == '__main__':
    bot.infinity_polling()