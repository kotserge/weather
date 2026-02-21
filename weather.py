import configparser
import sys

import requests

# Read config file
config = configparser.ConfigParser()
config.read(f"{sys.argv[1]}/config.ini")

WEATHER_ICONS = {
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

ERROR_ICON = "\udb80\udd64"


def get_weather_icon(weather_id, is_daytime):
    """Look up icon by exact code, then fall back to weather group (hundreds)."""
    icon = WEATHER_ICONS.get(weather_id) or WEATHER_ICONS.get((weather_id // 100) * 100)
    if icon is None:
        return ERROR_ICON
    if isinstance(icon, list):
        return icon[0] if is_daytime else icon[1]
    return icon


URL = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units={}&exclude=minutely,hourly,daily,alerts&appid={}"
url_formatted = URL.format(
    config["OPENWEATHERMAP"]["lat"],
    config["OPENWEATHERMAP"]["lon"],
    config["OPENWEATHERMAP"]["units"],
    config["OPENWEATHERMAP"]["appid"],
)

# get data
try:
    current = requests.get(url_formatted, timeout=10).json()
except requests.RequestException:
    print(ERROR_ICON)
    exit()

if current["cod"] != 200:
    print(ERROR_ICON)
    exit()

# get weather icon
weather_id = current["weather"][0]["id"]
is_daytime = current["sys"]["sunrise"] < current["dt"] < current["sys"]["sunset"]
weather_icon = get_weather_icon(weather_id, is_daytime)

# get unit
unit = str(round(current["main"]["temp"])) + "°"
degree = unit + "C" if config["OPENWEATHERMAP"]["units"].upper() == "METRIC" else unit + "F"

print(f"{weather_icon} {degree}")
