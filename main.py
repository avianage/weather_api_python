import os
import requests
from datetime import datetime
from geopy.geocoders import Nominatim
from dotenv import load_dotenv

load_dotenv()
user_api = os.getenv("OPEN_WEATHER_MAP_KEY")

city = input("Enter the city name: ")

geolocator = Nominatim(user_agent="weather_api")
location = geolocator.geocode(city)

lat = location.latitude
lon = location.longitude

print(lat, lon)


complete_api_link = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lon, user_api)

api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == 404:
    print("Invalid City: {}, Please Check your city name.".format(city))

else:
    temp_city = ((api_data['main']['temp']) - 273.15) # temperature in kelvin - 273.15 give temp in Celsius
    weather_desc = api_data['weather'][0]['description']
    humid = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-------------------------------------------------")
    print("Weather Stats for {} || {}".format(city.upper(), date_time))
    print("-------------------------------------------------")

    print("Current temperature: {} deg C".format(temp_city))
    print("Current weather: {}".format(weather_desc))
    print("Current Humidity: {}".format(humid))
    print("Current Wind Speed: {}".format(wind_spd))


