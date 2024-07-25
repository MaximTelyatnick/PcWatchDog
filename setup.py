from cx_Freeze import setup, Executable

# Определение исполняемого файла
executables = [
    Executable("message_telegram.py")
]

# Настройка
setup(
    name="MessageApp",
    version="0.1",
    description="An application that displays a message passed via command line arguments",
    executables=executables
)