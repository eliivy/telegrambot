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
        level = "beginner"

    if message.text == 'Любитель':
        level = "average"

    if message.text == 'Профессионал':
        level = "professional"

    with open('trains.json', 'r') as f:
        training = json.load(f)
    img = open('{0}/pic1.png'.format(level), 'rb')
    day = 1
    bot.send_message(message.from_user.id, training['{1}{0}'.format(str(day), level)])
    bot.send_photo(message.from_user.id, img)
    img.close()
    sendingtime = '00'
    while 1:
        now = t.strftime("%S", t.localtime())
        if now == sendingtime:
            day += 1
            bot.send_message(message.from_user.id, training['{1}{0}'.format(str(day), level)])
            img = open('{1}/pic{0}.png'.format(str(day), level), 'rb')
            bot.send_photo(message.from_user.id, img)
            img.close()
            if day == 30:
                break
        t.sleep(1)




if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
