# Weather

![Weather Module](/other/images/weather-module.png)

A small Python script that fetches current weather data from the [OpenWeatherMap API](https://openweathermap.org/api) and prints it to stdout as an icon and temperature (e.g. ` 21°C`). The output can be consumed by status bars, scripts, or anything that reads stdout.

## Dependencies

- Python 3
- [requests](https://pypi.org/project/requests/)
- A [Nerd Fonts](https://www.nerdfonts.com/) patched font (for weather icons)

## Configuration

Copy `config.ini.example` to `config.ini` and fill in your values:

- `APPID`: Your OpenWeatherMap API key. You can get one [here](https://openweathermap.org/).
- `LAT` and `LON`: The latitude and longitude of your location.
- `UNITS`: `METRIC` or `IMPERIAL`.

## Usage

```bash
# With venv already active:
python weather.py /path/to/this/repo

# Or use the wrapper script (activates .venv automatically):
./weather.sh /path/to/this/repo
```

The script expects `config.ini` to be in the directory passed as the first argument.

## License

This project is licensed under the MIT License - see the [LICENSE.md](/LICENSE.md) file for details. Note that this only extends to my code and other modules, fonts, etc. are licensed under their respective licenses and do not fall under this license. If you find any license violations, please contact me immediately, as this is not intended.
