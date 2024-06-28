#http://api.weatherapi.com/v1 #base url for weather API
#API key for weatherAPI= c526e7caac4c403e9f4212109242706

#import tkinter as tk
#import time
#from PIL import Image, ImageDraw, ImageFont, ImageTk
import requests

APIKeyForWeatherAPI = "c526e7caac4c403e9f4212109242706"
#longitude = data['location']['lat']
#latitude = data['location']['lng']

def getCurrentWeatherData(APIKey):
    weatherAPIUPL = f"http://api.weatherapi.com/v1/current.json?key={APIKey}&q=auto:ip"
    response = requests.get(weatherAPIUPL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

weatherData = getCurrentWeatherData(APIKeyForWeatherAPI)

print(f"現在地: {weatherData['location']['name']}, {weatherData['location']['region']}, {weatherData['location']['country']}")
print(f"現在時刻: {weatherData['location']['localtime']}")
print(f"現在の天気: {weatherData['current']['condition']['icon']}")
print(f"気温: {weatherData['current']['temp_c']} ℃")
print(f"湿度: {weatherData['current']['humidity']} %")
print(f"風速: {weatherData['current']['wind_kph']} km/h")
print(f"気圧: {weatherData['current']['pressure_mb']} hPa")
print(f"体感温度: {weatherData['current']['feelslike_c']} ℃")

#print(latAndLon)
#print(weatherData)


    