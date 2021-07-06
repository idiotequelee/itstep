import telebot
from datetime import datetime, timedelta, time, date
from date_time_event import Untiltime
import json


TOKEN = '1768402948:AAH-uJWG2yFqeEjUFePMvzDiE-C-Ys1YL7U'

FILE_STORAGE = 'data.json'

bot = telebot.TeleBot(TOKEN)

date = datetime.now() + timedelta(0, 5)

REMINDER_CONST = time(hour=13, minute=10)


"""
{
    "chat_id": [
        (date, mark),
        (date, mark),
        (date, mark)
    ],
    "chat_id2": [
        (date, mark),
        (date, mark),
        (date, mark)
    ]
}

"""

def read_file():
    with open(FILE_STORAGE, 'r') as f:
        return json.load(f)

def write_file(data):
     with open(FILE_STORAGE, 'w') as f:
         json.dump(data, f)

@Untiltime(dateOrtime=REMINDER_CONST)
def schedule():
    bot.send_message("196266971", "TIME is now")
    print('Hello! Its time!', datetime.now())

@bot.message_handler(content_types=["photo"])
def photo_handler(message):
    bot.send_message(message.chat.id, "Nice photo")
    print("Send nice")

# @bot.message_handler(func=lambda m: True)
# def send_welcome(message):
#     print(message)
#     bot.reply_to(message, "Welcome")



@bot.message_handler(content_types=["text"])
def mark_handler(message):
    print(message)
    msg = message.text.strip()
    if msg in ["1", "2", "3", "4", "5"]:
        bot.reply_to(message, "Дані твого самопочуття зафіксовано")
        try:
            all_data = read_file()
        except:
            all_data = {}
        chat_id = message.chat.id
        if chat_id in all_data:
            all_data[chat_id].append()
        else:
            all_data[chat_id] = [(str(date.now()), msg)]
            # global x, y
            x = str(date.now())
            y = msg 
        print(x, y)
            # return x, y
            
        write_file(all_data)

# print(x, y)
        
# def data_plot(message):
#     all_data = read_file()
#     chat_id = message.chat.id
#     x_list = []
#     y_list = []
#     for item in all_data[chat_id]:
#         print(item)
#         x_list.append(item[chat_id])
#         return x_list
#     print(x_list)
        

schedule()
bot.polling()
