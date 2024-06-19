import subprocess as sp
from dotenv import load_dotenv
import os

import telebot
from telebot import types

load_dotenv(dotenv_path='token.env')

token = os.getenv('TELEGRAM_TOKEN')
hashed_password = os.getenv('PASSWORD')

bot = telebot.TeleBot(token)
ip_addr = sp.run(["""ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'"""], shell=True, capture_output=True).stdout.decode()
bot_path = os.getenv('BOT_PATH')
bot_name = os.getenv('BOT_NAME')


def get_main_keyboard():
    main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_menu.row("Вкл/Выкл бота")
    main_menu.row("Перезагрузить бота")
    main_menu.row("Статус бота")

    return main_menu
