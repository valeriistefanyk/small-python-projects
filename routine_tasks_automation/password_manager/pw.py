#! python 3
# pw.py - Программа для незащищенного хранения паролей

import sys
import pyperclip


PASSWORDS = {
    'email': 'sdfsdafsdkjklsadjfkljsdflkasdjfsdf',
    'blog': 'sadkfjdskafjdalksfjkldjfaskldfjkdjsfakj',
    'luggage': 'sdffdff',
}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Использование: python pw.py [имя учетной записи]')
        sys.exit()
    account = sys.argv[1]
    
    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print(f'Пароль для {account} скопирован в буфер.')
    else:
        print(f'Учетная запись {account} отсутствует в списке')
