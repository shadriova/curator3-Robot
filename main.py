import telebot
from telebot import types
import random

list_1 = ['Далия', 'Аня', 'Регина', 'Диана']
list_2 = ['Рамзик', 'Ильнур', 'Рузик']
bot = telebot.TeleBot('6857170618:AAFtBdvQXt83dI1rWOZJMAlWnyVg4k8ZGVA')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Узнать шлюху дня")
    item2 = types.KeyboardButton("Узнать пидора дня")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Привет! Я бот с кнопками. У меня есть 2 команды:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    random_word_1 = random.choice(list_1)
    random_word_2 = random.choice(list_2)
    if message.text == "Узнать шлюху дня":
        bot.send_message(message.chat.id, f"Шлюха дня: {random_word_1}")
    elif message.text == "Узнать пидора дня":
        bot.send_message(message.chat.id, f"Пидор дня дня: {random_word_2}")

bot.polling()
