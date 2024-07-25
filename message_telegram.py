import sys
import requests
from telegram.error import TelegramError
from tkinter import Tk, Label




if __name__ == "__main__":
    # Токен бота
    TOKEN = '7138161176:AAHbtumnbrUsXTG7D5LJqdtdTyyQkr5rKTk'
    # ID  канала 
    CHANNEL_ID = '@techvagonmash_loger'

    # Получаем сообщение из командной строки
    message = sys.argv[1] if len(sys.argv) > 1 else "No messafffffge provided."

    # Отправляем сообщение в канал
    #send_message(TOKEN, CHANNEL_ID, "ufd")
    TOKEN = "7138161176:AAHbtumnbrUsXTG7D5LJqdtdTyyQkr5rKTk"
    chat_id = "@techvagonmash_loger" 
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # this sends the message

