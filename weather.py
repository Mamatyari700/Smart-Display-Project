#http://api.weatherapi.com/v1 #base url for weather API
#API key = c526e7caac4c403e9f4212109242706
#API key for ipify = https://geo.ipify.org/api/v2/country,city?apiKey=at_uJGnmiXcuETNuyc3tukfxtMY75Iu9

#import tkinter as tk
#import time
#from PIL import Image, ImageDraw, ImageFont, ImageTk
import requests

ipifyURL = "https://geo.ipify.org/api/v2/country,city?apiKey=at_uJGnmiXcuETNuyc3tukfxtMY75Iu9"

response = requests.get(ipifyURL)

data = response.json()

print(f"IPアドレス: {data['ip']}")
print(f"場所: {data['location']['city']}, {data['location']['region']}, {data['location']['country']}")
print(f"緯度: {data['location']['lat']}, 経度: {data['location']['lng']}")

APIKeyForWeatherAPI = "c526e7caac4c403e9f4212109242706"
longitude = data['location']['lat']
latitude = data['location']['lng']

def getWeatherData(APIKey, longitude, latitude):
    weatherAPIUPL = f"http://api.weatherapi.com/v1/current.json?key={APIKey}&q={longitude},{latitude}"
    response = requests.get(weatherAPIUPL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

weatherData = getWeatherData(APIKeyForWeatherAPI, longitude, latitude)

print(f"現在の天気: {weatherData['current']['condition']['text']}")
print(f"気温: {weatherData['current']['temp_c']} ℃")
print(f"湿度: {weatherData['current']['humidity']} %")


    