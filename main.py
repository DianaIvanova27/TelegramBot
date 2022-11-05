#def print_hi(name):
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#if __name__ == '__main__':
#    print_hi('PyCharm')


import telebot
#import random
from telebot import types

bot = telebot.TeleBot('5718650989:AAFOb2MV8wc_fzptk8KVn2bHbJZAgXIoYCI')


# Загружаем список интересных фактов
#f = open('data/facts.txt', 'r', encoding='UTF-8')
#facts = f.read().split('\n')
#f.close()
# Загружаем список поговорок
#f = open('data/thinktxt's., 'r', encoding='UTF-8')
#thinks  = f.read().split('\n')
#f.close()

@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Чебоксары")
        item2=types.KeyboardButton("Челябинск")
        item3=types.KeyboardButton("Стамбул")
        item4=types.KeyboardButton("Москва")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        bot.send_message(m.chat.id, 'В каком городе хочешь узнать погоду?',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Чебоксары':
            #answer = random.choice(facts)
            answer = "Дубак"
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Челябинск':
            #answer = random.choice(thinks)
            answer = "Холодно"
    elif message.text.strip() == 'Стамбул':
            answer = "Норм"
    elif message.text.strip() == 'Москва':
            answer = "Мерзко"
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)