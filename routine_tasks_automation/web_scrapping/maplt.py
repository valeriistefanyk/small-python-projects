"""
maplt.py - Запускает карту в браузере, извлекая почтовый адрес
            из командной строки или буфера обмена.
"""


import webbrowser
import sys
import pyperclip


if len(sys.argv) > 1:
    # Получение почтового адреса из командной строки.
    address = ' '.join(sys.argv[1:])
else:
    # Получение почтового адреса из буфера обмена.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
