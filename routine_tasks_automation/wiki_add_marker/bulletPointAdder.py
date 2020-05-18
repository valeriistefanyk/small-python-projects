#! python 3 
# bulletPointAdder.py - Добавляет маркеры Википедии в начало
# каждой строки текста, сохраненного в буфере обмена.

import pyperclip


if __name__ == '__main__':
    text = pyperclip.paste()

    lines = text.split('\n')

    # удаляем лишние символы в начале строки и в конце,
    # а также пустые элементы, если они имеются
    lines = [item.strip() for item in lines]
    lines = [value for value in lines if value]

    for i in range(len(lines)):
        lines[i] = '* ' + lines[i]
    
    text = '\n'.join(lines)    

    pyperclip.copy(text)



    