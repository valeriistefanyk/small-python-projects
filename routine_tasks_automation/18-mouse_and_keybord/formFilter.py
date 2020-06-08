"""
formFilter.py  - Автоматически заполняет форму.
"""


import pyautogui
import time

pyautogui.PAUSE = 0.5

nameField = (979, 174)
passwordField = (979, 250)
submitButton = (1398, 299)
submitButtonColor = (0, 105, 217)
submitAnotherLink = (760, 224)

formData = [
    {'name': 'valerii', 'password': '91lilkuk91'},
]

for person in formData:
    print('>>> 5-секундная пауза')
    time.sleep(5)
    while not pyautogui.pixelMatchesColor(
        submitButton[0],
        submitButton[1],
        submitButtonColor
    ):
        time.sleep(0.5)
        pyautogui.click(nameField[0], nameField[1])
        pyautogui.typewrite(person['name'] + '\t')
        pyautogui.typewrite(person['password'] + '\t')
        pyautogui.press('enter')
        print('Выполнен щелчек по enter')
        time.sleep(5)
