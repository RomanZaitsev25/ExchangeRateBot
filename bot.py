import telebot
import requests

from config import config

bot = telebot.TeleBot(config.TOKEN)


def get_rate():
    response = requests.get(
        'https://belarusbank.by/api/kursExchange?city=Червень'
    )
    if response.ok:
        return response.json()
    return []


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        'Этот бот даёт информацию о курсе валют на сегодняшний день '
        'в отделении Беларусбанка в г.Червене.'
    )


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(
        message.chat.id,
        'Список доступных команд:\n'
        '   /help - получить список доступных команд\n'
        '   /usd - получить курс доллара по отношению к белорусскому рублю \n'
        '   /eur - получить курс евро по отношению к белорусскому рублю\n'
        '   /rub - получить курс российского рубля'
        ' по отношению к белорусскому рублю\n'
        '   /pln - получить курс польского злотого'
        ' по отношению к белорусскому рублю\n'
    )


@bot.message_handler(commands=['usd'])
def usd(message):
    data = get_rate()
    out_message = ''
    for info in data:
        out_message += 'Курс продажи {}, курс покупки {}.\n'.format(
            info['USD_in'], info['USD_out']
        )
    if not out_message:
        out_message = 'Сайт сейчас не доступен.'
    bot.send_message(message.chat.id, out_message)


@bot.message_handler(commands=['eur'])
def eur(message):
    data = get_rate()
    out_message = ''
    for info in data:
        out_message += 'Курс продажи {}, курс покупки {}.\n'.format(
            info['EUR_in'], info['EUR_out']
        )
    if not out_message:
        out_message = 'Сайт сейчас не доступен.'
    bot.send_message(message.chat.id, out_message)


@bot.message_handler(commands=['rub'])
def rub(message):
    data = get_rate()
    out_message = ''
    for info in data:
        out_message += 'Курс продажи {}, курс покупки {}.\n'.format(
            info['RUB_in'], info['RUB_out']
        )
    if not out_message:
        out_message = 'Сайт сейчас не доступен.'
    bot.send_message(message.chat.id, out_message)


@bot.message_handler(commands=['pln'])
def pln(message):
    data = get_rate()
    out_message = ''
    for info in data:
        out_message += 'Курс продажи {}, курс покупки {}.\n'.format(
            info['PLN_in'], info['PLN_out']
        )
    if not out_message:
        out_message = 'Сайт сейчас не доступен.'
    bot.send_message(message.chat.id, out_message)


bot.polling()
