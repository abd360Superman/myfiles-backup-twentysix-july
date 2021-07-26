#! python3
# getOpenWeather.py - Prints the weather for a location entered.

APPID = '4d09820275977e4e908f2339f9467c82'

import json, requests

print('Usage: Enter city to know it\'s weather')
location = input()

url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

data = response.json()
# getting the main dict block
main = data['main']
# getting temperature
temperature = main['temp']
# getting the humidity
humidity = main['humidity']
# getting the pressure
pressure = main['pressure']
# weather report
report = data['weather']
print(f"{location:-^30}")
print(f"Temperature: {temperature}")
print(f"Humidity: {humidity}")
print(f"Pressure: {pressure}")
print(f"Weather Report: {report[0]['description']}")
