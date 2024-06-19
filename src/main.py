import json

import hash
import pm
from config import *


@bot.message_handler(commands=['start'])
def com_start(message):
    mes = bot.send_message(message.chat.id, "Введите код активации...")
    bot.register_next_step_handler(mes, com_code)


def com_code(message):
    if hash.verify_password(message.text, hashed_password):
        main_page(message)
    else:
        mes = bot.send_message(message.chat.id, "Код активации неверен!")
        bot.register_next_step_handler(mes, com_code)


def main_page(message):
    bot.send_message(message.chat.id, "IP адрес сервера:" + ip_addr + "\n\nГлавная страница", reply_markup=get_main_keyboard())


@bot.message_handler(content_types=['text'])
def com_main_page(message):
    server = sp.run(['pm2', 'status'], capture_output=True).stdout.decode()
    server = pm.parse(server)
    if message.text == "Вкл/Выкл бота":
        for bot_pm in server:
            if bot_pm['status'] == 'online' and bot_pm['name'] == bot_name:
                sp.run(['pm2', 'stop', bot_name], capture_output=True)
                bot.send_message(message.chat.id, "Бот выключен!", reply_markup=get_main_keyboard())
            elif bot_pm['status'] == 'stopped' and bot_pm['name'] == bot_name:
                sp.run(['pm2', 'start', bot_path, '--interpreter=python3', f"""--name='{bot_name}'"""], capture_output=True)
                bot.send_message(message.chat.id, "Бот включен!", reply_markup=get_main_keyboard())
    elif message.text == "Перезагрузить бота":
        for bot_pm in server:
            if bot_pm['status'] == 'stopped' and bot_pm['name'] == bot_name:
                sp.run(['pm2', 'start', bot_path, '--interpreter=python3', f"""--name={bot_name}"""], capture_output=True)
            elif bot_pm['status'] == 'online' and bot_pm['name'] == bot_name:
                sp.run(['pm2', 'stop', bot_name, '&&', 'pm2', 'start', bot_path, '--interpreter=python3', f"""--name='{bot_name}'"""], capture_output=True)
        bot.send_message(message.chat.id, "Бот перезагружен!", reply_markup=get_main_keyboard())
    elif message.text == "Статус бота":
        flag = False
        for bot_pm in server:
            if bot_pm['name'] == bot_name:
                bot.send_message(message.chat.id, json.dumps(bot_pm, indent=4) , reply_markup=get_main_keyboard())
                flag = True
        if not flag:
            bot.send_message(message.chat.id, "Не удалось получить статус", reply_markup=get_main_keyboard())


if __name__ == '__main__':
    bot.polling(none_stop=True)