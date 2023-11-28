import telebot
import random

bot = telebot.TeleBot('6906533346:AAFlQ2Dv-Q0ojkwA4uTfQiFSaUZRwYwAUzw')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message('Нихао, аригато', parse_mode='Markdown')

@bot.message_handler(commands=['число'])
def main(message):
    bot.send_message(digit=random.randint(1,10))

@bot.message_handler(commands=['дрель'])
def main(message):
    bot.send_message('*ВжжжжжВЖжжжж*')

bot.infinyty_pooling()