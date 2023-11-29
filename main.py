import telebot

bot = telebot.TeleBot('6187203002:AAFqQ9JCdI3WCG0I9PuoOIhgd2P8ZkyvZJY')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет /n наконец-то ты нашёл меня')


@bot.message_handler(commands=['love'])
def main(message):
    bot.send_message(message.chat.id, 'Один честны разговор - может решить много проблем')


@bot.message_handler(commands=['friend'])
def main(message):
    bot.send_message(message.chat.id, 'Любовь может обойтись без взаимности, но дружба — никогда')


@bot.message_handler(commands=['family'])
def main(message):
    bot.send_message(message.chat.id, 'Семья – это место силы')


@bot.message_handler(commands=['career'])
def main(message):
    bot.send_message(message.chat.id, 'Страх высоты многим мешает делать карьеру… ')


bot.infinity_polling()
