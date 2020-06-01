"""
removeCsvHeader.py - Удаляет заголовки из всех CSV-файлов
    в текущем рабочем каталоге.
"""

import csv
import os

path = './routine_tasks_automation/css_json_working/'
pathHeaderRemoved = path + 'headerRemoved/'
os.makedirs(path + 'headerRemoved', exist_ok=True)
for csvFilename in os.listdir(path + 'csvfiles/'):
    if not csvFilename.endswith('.csv'):
        continue
    print('Удаление заголовка из файла', csvFilename, '...')
    csvRows = []
    with open(path + 'csvfiles/' + csvFilename) as csvFileObj:
        readerObj = csv.reader(csvFileObj)
        for row in readerObj:
            if readerObj.line_num == 1:
                continue
            csvRows.append(row)
    with open(pathHeaderRemoved + csvFilename, 'w', newline='') as csvFileObj:
        csvWriter = csv.writer(csvFileObj)
        for row in csvRows:
            csvWriter.writerow(row)
