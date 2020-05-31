"""
combinePDFs.py - объединяет все PDF-документы, находящиеся
    в текущем рабочем каталоге, в единый PDF-документ.
"""

import PyPDF2
import os

pdfFiles = []
path = './routine_tasks_automation/pdf_word_working/combinePDFFiles/'
for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()
for filename in pdfFiles:
    filename = path + filename
    with open(filename, 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
with open(path + 'allminutes.pdf', 'wb') as pdfOutput:
    pdfWriter.write(pdfOutput)
