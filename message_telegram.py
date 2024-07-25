import sys
import requests
from telegram.error import TelegramError
from tkinter import Tk, Label




if __name__ == "__main__":
    # Токен бота
    TOKEN = '7138161176:AAHbtumnbrUsXTG7D5LJqdtdTyyQkr5rKTk'
    # ID вашего канала (например, '@yourchannelname' или '-1001234567890')
    # 7138161176:AAHbtumnbrUsXTG7D5LJqdtdTyyQkr5rKTk
    CHANNEL_ID = '@techvagonmash_loger'

        # Получаем сообщение из командной строки
    message = sys.argv[1] if len(sys.argv) > 1 else "No message provided."

    # Отправляем сообщение в канал
    #send_message(TOKEN, CHANNEL_ID, "ufd")
    TOKEN = "7138161176:AAHbtumnbrUsXTG7D5LJqdtdTyyQkr5rKTk"
    chat_id = "@techvagonmash_loger" 
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # this sends the message




    # Создаем окно
    root = Tk()
    root.title("Message Display")

    # Добавляем метку с сообщением
    label = Label(root, text=message, padx=20, pady=20)
    label.pack()

    # Запускаем главный цикл приложения
    root.mainloop()