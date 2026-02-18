import configparser
import sys

import requests

# Read config file
config = configparser.ConfigParser()
config.read(f"{sys.argv[1]}/config.ini")

dict_weather_group_icon = {
    200: "\ue31d",
    300: "\ue316",
    500: "\ue318",
    600: "\ue31a",
    700: "\ue313",
    800: ["\uf522", "\uf4ee"],
    801: ["\ue302", "\ue32e"],
    802: "\ue33d",
    803: "\ue33d",
    804: "\ue33d",
}

URL = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units={}&exclude=minutely,hourly,daily,alerts&appid={}"
url_formatted = URL.format(
    config["OPENWEATHERMAP"]["lat"],
    config["OPENWEATHERMAP"]["lon"],
    config["OPENWEATHERMAP"]["units"],
    config["OPENWEATHERMAP"]["appid"],
)

# get data
try:
    current = requests.get(url_formatted).json()
except:
    print("\udb80\udd64")
    exit()

if current["cod"] != 200:
    print("\udb80\udd64")
    exit()

# get weather icon
weather_id = current["weather"][0]["id"]
weather_icon = dict_weather_group_icon.get(weather_id, (weather_id // 100) * 100)
if isinstance(weather_icon, int):
    weather_icon = dict_weather_group_icon.get((weather_id // 100) * 100, "ERROR")

if isinstance(weather_icon, list):
    weather_icon = (
        weather_icon[0]
        if current["sys"]["sunrise"] < current["dt"] < current["sys"]["sunset"]
        else weather_icon[1]
    )

# get unit
unit = str(round(current["main"]["temp"])) + "°"
degree = unit + "C" if config["OPENWEATHERMAP"]["units"] == "METRIC" else unit + "F"

print(f"{weather_icon} {degree}")
