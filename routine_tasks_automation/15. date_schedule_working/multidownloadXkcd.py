"""
multidownloadXkdc.py - Загружает все комиксы XKCD с
    использованием нескольких потоков выполнения.
"""

import requests
import os
import bs4
import threading


url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)


res = requests.get(url)
res.raise_for_status()


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print(f'Загружается страница {url}...')
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Не удалось найти изображение.')
        else:
            comicUrl = comicElem[0].get('src')
            if comicUrl.startswith('//'):
                comicUrl = comicUrl.replace('//', 'http://')
            print(f'Загружается изображение {comicUrl}...')
            res = requests.get(comicUrl)
            res.raise_for_status()

            imageFile = open(
                os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(
        target=downloadXkcd,
        args=(i, i + 99)
    )
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()
print('Готово')

# while not url.endswith('#'):
#     prevLink = soup.select('a[rel="prev"]')[0]
#     url = 'http://xkcd.com' + prevLink.get('href')
# else:
#     print('Готово')
