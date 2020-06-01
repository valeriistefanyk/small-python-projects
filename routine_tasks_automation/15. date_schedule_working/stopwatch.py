"""
stopwatch.py - Простая программа-хронометр.
"""

import time

print('Чтобы начать отсчет, нажмите клавишу ENTER.')
print('Для выхода из программы нажмите <Ctrl+C>')
input()
print('Отсчет начат.')
startTime = time.time()
lastTime = startTime
lapNum = 1
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        text = f'Замер #{lapNum}: {totalTime} ({lapTime})'
        print(text, end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nГотово')
    exit()
