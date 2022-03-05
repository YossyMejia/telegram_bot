import telebot
from api_data import *
from bot_token import *
from flask import Flask
from flask import request
from flask import Response

bot = telebot.TeleBot(bot_token)

app = Flask(__name__)


def parse_message(message):
    pass


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        message = request.get_json()
        print(message)
        # Prevent telegram bot to spam the message with status 200
        return Response('Ok', status=200)
    else:
        return '<h1>BB</h1>'


if __name__ == '__main__':
    app.run(debug=True)

#  @bot.message_handler(commands=["help","start"])
#  def enviar(message):
#     bot.reply_to(message, "PRUEBA DE COMANDOS")
#
#
# @bot.message_handler(func=lambda message: True)
# def crypto_value(message):
#     bot.reply_to(message, getCoinPrice(message.text))
#
#
# bot.polling()


# https:api.telegram.org/bot5127830572:AAFZhd_S5ZUHwOgs1jjcqsU8BryajrMAIXQ/setWebhook?url=https://0a3c-201-202-112-18.ngrok.io
