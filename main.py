import telebot
bot = telebot.TeleBot('6811968600:AAGMfqWutHwsrlgR1CdtK-fClrf12IbgTT8')
 
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '*добро пожаловать в бот!*', parse_mode='Markdown')
    
@bot.message_handler(commands=['greetings'])
def main(message):
    bot.send_message(message.chat.id, 'Приветствую тебя в моём первом боте!', parse_mode='Markdown')
    
    
@bot.message_handler(commands=['binary code'])
def main(message):
    bot.send_message(message.chat.id, 'двоичный код-данные в виде 1 и 0', parse_mode='Markdown')
    
      
@bot.message_handler(commands=['measurement of information '])
def main(message):
    bot.send_message(message.chat.id, 'измерение информации-бит\nбайт\nКилобайт\nМегабайт\nГигобайт\nТерабайт', parse_mode='Markdown')
    
    
@bot.message_handler(commands=['Informatics '])
def main(message):
    bot.send_message(message.chat.id, 'информатика-это наука,изучающая автоматическую работу с информацией', parse_mode='Markdown') 
    
bot.infinity_polling()
