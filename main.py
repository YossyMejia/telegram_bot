#5127830572:AAFZhd_S5ZUHwOgs1jjcqsU8BryajrMAIXQ
import telebot
from api_data import *

bot = telebot.TeleBot("5127830572:AAFZhd_S5ZUHwOgs1jjcqsU8BryajrMAIXQ")


#@bot.message_handler(commands=["help","start"])
#def enviar(message):
#    bot.reply_to(message, "PRUEBA DE COMANDOS")


@bot.message_handler(func=lambda message:True)
def mensaje(message):
    bot.reply_to(message, getCoinPrice(message.text))


bot.polling()



