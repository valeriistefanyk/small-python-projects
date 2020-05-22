"""
backupToZip.py - Копирует папку вместе со всем ее содержимым
    в ZIP-файл с инкрементируемым номером копии в имени файла.
"""

import zipfile, os


def backup_to_zip(forlder, files_to_backup):
    folder = os.path.abspath(forlder)

    # определить имя файла последнего бэкапа
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + \
            str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
        

    # Создание ZIP-файла
    print(f"Создается файл {zipFilename}")
    backupZip = zipfile.ZipFile(folder + '\\' + zipFilename, 'w')

    # обход всего дерева папки и сжатие файлов, содержащихся в папке
    for foldername, subfolders, filenames in os.walk(files_to_backup):
        print(f'Добавление файлов из папки {foldername}')
        backupZip.write(foldername)
        for filename in filenames:
            newsBase = os.path.basename(folder) + '_'
            # if filename.startswith(newBase) and filename.endswith('.zip'):
            #     continue
            backupZip.write(os.path.join(foldername, filename))
        backupZip.close()


    print('Готово.')





if __name__ == "__main__":
    backup_folder = r'routine_tasks_automation\file_management\backup'
    path_for_backup = r'routine_tasks_automation\file_management\files'
    if os.path.exists(backup_folder) and os.path.exists(path_for_backup):
        backup_to_zip(backup_folder, path_for_backup)
    else:
        print(f"Пути '{path}' не существует")