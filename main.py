#def print_hi(name):
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#if __name__ == '__main__':
#    print_hi('PyCharm')


import telebot

bot = telebot.TeleBot('5718650989:AAFOb2MV8wc_fzptk8KVn2bHbJZAgXIoYCI')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет. Выбери город')
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
# Запускаем бота
bot.polling(none_stop=True, interval=0)