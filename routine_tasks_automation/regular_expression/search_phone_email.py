#! python3
# search_phone_email.py - Находит телефанные номера и
# адреса электронной почты в буфере обмена.

import pyperclip
import re

# регулярное выражение для поиска телефонов
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                 # территориальный код
    (\s|-|\.)?                         # разделитель
    (\d{3})                            # первые 3 цифры
    (\s|-|\.)                          # разделитель
    (\d{4})                            # последние 4 цифры
    (\s* (ext|x|ext.)\s*(\d{2,5}))?    # добавочный номер
    )''', re.VERBOSE)


# регулярное выражение для поисков адресов электронной почты
emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+       # имя пользователя
        @                       # символ @
        [a-zA-Z0-9.-]+          # имя домена
        (\.[a-zA-Z]{2,5})       # остальная часть адреса
    )''', re.VERBOSE)


# поиск соответствий в тексте буфера обмена
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])
    

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса электронной \
        почты не обнаружены.')
        

text_for_test = ''' 
    valerii@mg.au 380-000-0000
    valeriistefanyk@gmail.com  900-5432
'''