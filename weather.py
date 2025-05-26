import configparser
import requests

import sys

# Read config file
config = configparser.ConfigParser()
config.read(f"{sys.argv[1]}/config.ini")

dict_weather_group_icon = {
    200: "",
    300: "",
    500: "",
    600: "",
    700: "",
    800: ["", ""],
    801: ["", ""],
    802: "",
    803: "",
    804: "",
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
    print("")
    exit()

if current["cod"] != 200:
    print("")
    exit()

# get weather icon
weather_id = current["weather"][0]["id"]
weather_icon = dict_weather_group_icon.get(weather_id, (weather_id // 100) * 100)
if isinstance(weather_icon, int):
    weather_icon = dict_weather_group_icon.get((weather_id // 100) * 100, 'ERROR')

if isinstance(weather_icon, list):
    weather_icon = (
        weather_icon[0] if current["sys"]["sunrise"] < current["dt"] < current["sys"]["sunset"] else weather_icon[1]
    )

# get unit
unit = str(round(current["main"]["temp"])) + "°"
degree = unit + "C" if config["OPENWEATHERMAP"]["units"] == "METRIC" else unit + "F"

print(f"{weather_icon} {degree}")
