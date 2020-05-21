# mcb.pyw - Сохраняет и загружает фрагменты текста
# в буфер обмена
# Использование:    py.exe mcb.pyw save <ключевое_слово> - 
#                       Сохраняет буфер обмена в ключевое слово.
#                   py.exe mcb.pyw <ключевое_слово> -
#                       Загружает ключевое слово в буфер обмена.
#                   py.exe mcb.pyw list -
#                       Загружает все ключевые слова в буфер обмена.

import shelve, pyperclip, sys, os

mcbShelf = shelve.open(r'routine_tasks_automation\read_write_files\mcb_shelve\mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # Сохрание содержимого буфера обмена.
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # Формирование списка ключевых слов и загрузка содержимого
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

