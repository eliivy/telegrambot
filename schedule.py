import telebot
import json
import time as t
from datetime import datetime as dt
import schedule

liza_id = 166934167
token = '857333265:AAHwUpghmbxCwKnqVUE_kHzNz1NijpRqYHY'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Новичок', 'Любитель', 'Профессионал')
    bot.send_message(message.from_user.id, 'Привет! Выбери свой уровень сложности:', reply_markup=user_markup)


def sender(message, day):
    with open('trains.json', 'r') as f:
        training = json.load(f)
        bot.send_message(message.from_user.id, training['Новичок{0}'.format(str(day))])
        day += 1


@bot.message_handler(content_types=['text'])
def handle_level(message):
    if message.text == 'Новичок':
        with open('trains.json', 'r') as f:
            training1 = json.load(f)
        day1 = 1
        day = 2
        bot.send_message(message.from_user.id, training1['Новичок{0}'.format(str(day1))])
        schedule.every(5).seconds.do(sender, message, day)
        while 1:
            schedule.run_pending()
            t.sleep(1)


bot.polling(none_stop=True, interval=0)



'''def sender():
    for minuta in range(2, 31):
        startminuta = dt.now().minute
        utro='08:00'
        while 1:
            with open('trains.json', 'r') as f:
                training = json.load(f)
            if startminuta == minuta:
                bot.send_message(message.from_user.id, training['Новичок{0}'.format(minuta)])
            t.sleep(60)'''

