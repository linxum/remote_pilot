import subprocess as sp

import telebot
from telebot import types

token = '1692814273:AAH9rmQS1372UZ5t_GQYzT3hUwcvn6bdOSs'
hashed_password = '57c37c5b724092c978f7bc5c4f16ac2713e7bdad6299bc3db214cc32a7bbc719'
bot = telebot.TeleBot(token)
ip_addr = sp.run(["""ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'"""], shell=True, capture_output=True).stdout.decode()
bot_path = '/home/smkhnv/a.py'
bot_name = 'a.py'


def get_main_keyboard():
    main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_menu.row("Вкл/Выкл бота")
    main_menu.row("Перезагрузить бота")
    main_menu.row("Статус бота")

    return main_menu
