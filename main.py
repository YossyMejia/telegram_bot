import telebot
from api_data import *
from bot_token import *

bot = telebot.TeleBot(bot_token)


#@bot.message_handler(commands=["help","start"])
#def enviar(message):
#    bot.reply_to(message, "PRUEBA DE COMANDOS")


@bot.message_handler(func=lambda message:True)
def mensaje(message):
    bot.reply_to(message, getCoinPrice(message.text))


bot.polling()



