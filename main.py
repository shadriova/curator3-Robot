import telebot
bot=telebot.TeleBot('6939469753:AAGMnNjy1itjLXu0fj3fNoVNCxraCBhl9Ac')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat,id,'*привет,выбери команду*')
@bot.message_handler(commands=['back'])
def main(message):
    bot.send_message(message.chat,id,'обратно вернуться нельзя,что было то прошло')
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat,id,'помощь уже в пути. Ждите.')
@bot.message_handler(commands=['end'])
def main(message):   
    bot.send_message(message.chat,id,'прощай')
bot.infinity_polling()
