"""
lucky.py - Открывает первые 3 ссылки по указанному запросу
"""


from bs4 import BeautifulSoup
import requests
import sys
import webbrowser


if len(sys.argv) > 1:
    request = ' '.join(sys.argv[1:])
else:
    request = 'lucky'
full_url = 'https://www.google.com/search?q=' + request
res = requests.get(full_url)
res.raise_for_status()

googleSearchPageSoup = BeautifulSoup(res.text, 'html.parser')
linkSoup = googleSearchPageSoup.select('.kCrYT a')

numOpen = min(3, len(linkSoup))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkSoup[i].get('href'))
