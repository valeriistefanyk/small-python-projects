import threading
import time

print('Начало программы.')


def takeANap():
    time.sleep(5)
    print('Проснись!')


threadObj = threading.Thread(target=takeANap)
threadObj2 = threading.Thread(
    target=print,
    args=['Cats', 'Dogs', 'Frogs'],
    kwargs={'sep': ' & '}
)
threadObj.start()
threadObj2.start()
print('Конец программы.')
