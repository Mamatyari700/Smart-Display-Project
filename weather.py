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
    currentWeatherURL = f"http://api.weatherapi.com/v1/current.json?key={APIKey}&q=auto:ip"
    response = requests.get(currentWeatherURL)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def getWeatherForecast(APIKey,days):
    weatherForecastURL = f"http://api.weatherapi.com/v1/forecast.json?key={APIKey}&q=auto:ip&days={days}"
    response = requests.get(weatherForecastURL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

currentWeatherData = getCurrentWeatherData(APIKeyForWeatherAPI)
weatherForecastData = getWeatherForecast(APIKeyForWeatherAPI, 3)

print(f"現在地: {currentWeatherData['location']['name']}, {currentWeatherData['location']['region']}, {currentWeatherData['location']['country']}")
print(f"現在時刻: {currentWeatherData['location']['localtime']}")
print(f"現在の天気: {currentWeatherData['current']['condition']['icon']}")
print(f"気温: {currentWeatherData['current']['temp_c']} ℃")
print(f"湿度: {currentWeatherData['current']['humidity']} %")
print(f"風速: {currentWeatherData['current']['wind_kph']} km/h")
print(f"気圧: {currentWeatherData['current']['pressure_mb']} hPa")
print(f"体感温度: {currentWeatherData['current']['feelslike_c']} ℃")



#print(currentWeatherData)
print(weatherForecastData)



    