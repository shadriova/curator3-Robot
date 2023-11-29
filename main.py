import telebot
bot = telebot.TeleBot('6636808037:AAFmPOlYpuTUdXhvLl2xPkjXF2WzeYtDbrU')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*ПРИВЕТ, БОЛЕЛЬЩИК*', parse_mode='Markdown')

@bot.message_handler(commands=['goool'])
def main(message):
    bot.send_message(message.chat.id, '*ОЛЕ-ОЛЕ-ОЛЕ*', parse_mode='Markdown')

@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, '[ссылка](https://rfs.ru/)', parse_mode='Markdown')

bot.infinity_polling()
