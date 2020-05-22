""" 
renameDates.py - Переименовывает файлы, имена которых включают
    даты, указанные в американском формате (ММ-ДД-ГГГГ), приводя
    их в соответствие с европейским форматом дат (ДД-ММ-ГГГГ).
"""

import os, shutil, re


def exist_path(path):
    return os.path.exists(path)


def date_pattern():
    datePattern = re.compile(r"""^(.*?)     # весь текст перед датой
            ((0|1)?\d)-                     # одна или две цифры месяца
            ((0|1|2|3)?\d)-                 # одна или две цифры числа
            ((19|20)\d\d)                   # четыре цифры года
            (.*?)$                          # весь текст после даты
        """, re.VERBOSE)
    return datePattern


def search_file(path, pattern):
    for amerFilename in os.listdir(path):
        mo = pattern.search(amerFilename)
        if mo == None:
            continue

        # получение отдельных частей имен файлов
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)

        euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

        # получение полных абсолютных путей к файлам
        absWorkingDir = os.path.abspath(path_folder)
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)

        # print(f"{amerFilename} -> {euroFilename}")
        shutil.move(amerFilename, euroFilename)

if __name__ == "__main__":
    path_folder = r'routine_tasks_automation\file_management\files'
    if exist_path(path_folder):
        print(os.listdir(path_folder))
        pattern = date_pattern()
        search_file(path_folder, pattern)
    else:
        print(f"Пути '{path_folder}' не существует")