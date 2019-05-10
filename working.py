import telebot
import json
import time as t

liza_id = 166934167
token = '857333265:AAHwUpghmbxCwKnqVUE_kHzNz1NijpRqYHY'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Новичок', 'Любитель', 'Профессионал')
    bot.send_message(message.from_user.id, 'Привет! Выбери свой уровень сложности:', reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_level(message):
    if message.text == 'Новичок':
        with open('trains.json', 'r') as f:
            training = json.load(f)
        img = open('beginner/pic1.png', 'rb')
        day = 1
        bot.send_message(message.from_user.id, training['Новичок{0}'.format(str(day))])
        bot.send_photo(message.from_user.id, img)
        img.close()
        sendingtime = '00'
        while 1:
            now = t.strftime("%S", t.localtime())
            if now == sendingtime:
                day += 1
                bot.send_message(message.from_user.id, training['Новичок{0}'.format(str(day))])
                img = open('beginner/pic{0}.png'.format(str(day)), 'rb')
                bot.send_photo(message.from_user.id, img)
                img.close()
                if day == 30:
                    break
            t.sleep(1)
    elif message.text == 'Любитель':
        with open('trains.json', 'r') as f:
            training = json.load(f)
        img = open('average/pic1.png', 'rb')
        day = 1
        bot.send_message(message.from_user.id, training['Средний{0}'.format(str(day))])
        bot.send_photo(message.from_user.id, img)
        img.close()
        sendingtime = '00'
        while 1:
            now = t.strftime("%S", t.localtime())
            if now == sendingtime:
                day += 1
                bot.send_message(message.from_user.id, training['Средний{0}'.format(str(day))])
                img = open('average/pic{0}.png'.format(str(day)), 'rb')
                bot.send_photo(message.from_user.id, img)
                img.close()
                if day == 30:
                    break
            t.sleep(1)
    elif message.text == 'Профессионал':
        with open('trains.json', 'r') as f:
            training = json.load(f)
        img = open('professional/pic1.png', 'rb')
        day = 1
        bot.send_message(message.from_user.id, training['Профессионал{0}'.format(str(day))])
        bot.send_photo(message.from_user.id, img)
        img.close()
        sendingtime = '00'
        while 1:
            now = t.strftime("%S", t.localtime())
            if now == sendingtime:
                day += 1
                bot.send_message(message.from_user.id, training['Профессионал{0}'.format(str(day))])
                img = open('professional/pic{0}.png'.format(str(day)), 'rb')
                bot.send_photo(message.from_user.id, img)
                img.close()
                if day == 30:
                    break
            t.sleep(1)


bot.polling(none_stop=True, interval=0)


