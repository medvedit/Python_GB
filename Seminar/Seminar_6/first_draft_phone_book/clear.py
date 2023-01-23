import os  # для с операционными системами.
from sys import platform  # информация об операционной системе.


def clear_screen():  # Очистка консоли
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")  # для Linux & MacOS
    elif platform == "win32" or platform == "cygwin":
        os.system("cls")    # для Windows
