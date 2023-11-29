import telebot

bot = telebot.TeleBot('6483708701:AAFJoAVOXeGnc-uoJqoY2p9ps3DOX9Mboxo')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*Погнали!)*', parse_mode='Markdown')


@bot.message_handler(commands=['happy'])
def main(message):
    bot.send_message(message.chat.id, '_Ура!_', parse_mode='Markdown')


@bot.message_handler(commands=['sad'])
def main(message):
    bot.send_message(message.chat.id, '=(', parse_mode='Markdown')


@bot.message_handler(commands=['buy'])
def main(message):
    bot.send_message(message.chat.id, 'Пока!', parse_mode='Markdown')


bot.infinity_polling()
