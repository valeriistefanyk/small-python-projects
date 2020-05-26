"""
Получаем таблицу с информацией о статистике коронавируса
с ресурса index.minfin.com.ua
"""

from bs4 import BeautifulSoup
import requests
from math import ceil


def parting(xs, parts, getText=True, replaceSymbols=True):
    _xs = xs[:]
    if getText:
        _xs = [element.getText() for element in _xs]
    if replaceSymbols:
        _xs = del_html_sybmols(_xs)

    elements_len = ceil(len(xs) / parts)
    return [tuple(_xs[parts*k: parts*(k+1)]) for k in range(elements_len)]


def del_html_sybmols(xs):
    xs = [el.replace('\xa0', ' ') for el in xs]
    xs = [el.replace('\xad', '') for el in xs]
    return xs


res = requests.get('https://index.minfin.com.ua/reference/coronavirus/')
res.raise_for_status()
covidSoup = BeautifulSoup(res.text, "html.parser")
covidElem = covidSoup.select('.main-table tr td')

parting_list = parting(covidElem, 3)
for category in parting_list:
    print(category)
