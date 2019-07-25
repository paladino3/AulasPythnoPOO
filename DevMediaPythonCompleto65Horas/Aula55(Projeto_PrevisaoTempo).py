import urllib.request
from xml.etree.ElementTree import parse
import json


WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?p=%s'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/res/1.0'

def weather_for_zip(zip_code):
    url = WEATHER_URL % zip_code
    res = parse(urllib.request.urlopen(url)).getroot()
    forecasts = []
    for element in res.findall('channel/item/(&s)forecast'%WEATHER_NS):
        forecasts.append({
            'date':element.get('date'),
            'low':element.get('low'),
            'high':element.get('high'),
            'condition':element.get('text')
        })

    ycodition=rss.find('channel/item/(%s)condition'%WEATHER_NS)
    return {
        'current_condition':ycodition.get('text'),
        'current_temp':ycodition.get('temp'),
        'forecasts':forecasts,
        'title':rss.findtext('channel/title')
    }
myWeather=weather_for_zip("BRXX032X")

print(str(myWeather["title"]))
print()
print("Condição atual: "+str(myWeather))
print("Temperatura atual: "+str(myWeather["current_condition"]))
print()
print("Previsao para hoje: "+str(myWeather["forecasts"][0]["date"]))
print("Condicao para hoje: "+str(myWeather["forecasts"][0]["condition"]))
print("Maxima para hoje: "+str(myWeather["forecasts"][0]["high"]))
print("Minima para hoje: "+str(myWeather["forecasts"][0]["low"]))
print()
print("Previsao para amanha: "+str(myWeather["forecasts"][1]["date"]))
print("Condicao para amanha: "+str(myWeather["forecasts"][1]["condition"]))
print("Maxima para amanha: "+str(myWeather["forecasts"][1]["high"]))
print("Minima para amanha: "+str(myWeather["forecasts"][1]["low"]))
