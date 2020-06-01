"""
quickWeather.py - Выводит прогноз погоды для заданного
    населенного пункта.
"""

import json
import requests
import sys

# if len(sys.argv) < 2:
#     print('Использование: quickWeather.py location')
#     sys.exit()
location = ' '.join(sys.argv[1:])
urlBase = 'https://samples.openweathermap.org/data/2.5/forecast/'
urlConcrete = urlBase + 'daily?lat=35&lon=139&cnt=10&appid=8'
response = requests.get(urlConcrete)
response.raise_for_status()
weatherData = json.loads(response.text)
w = weatherData['list']
print('Погода сегодня:', w[0]['weather'][0]['main'])
print('Информация:', w[0]['weather'][0]['description'])
print()
print('Погода завтра:', w[1]['weather'][0]['main'])
print('Информация:', w[1]['weather'][0]['description'])
