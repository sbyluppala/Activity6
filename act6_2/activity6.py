import urllib.parse
import requests
import pytemperature
from datetime import datetime

now = datetime.now()
now = datetime.strftime(now, '%A, %d %B, %Y')


def check_current_conditions(json_data):

    try:
        current_conditions = json_data['weather'][0]['description']
        return current_conditions

    except Exception:
        str = 'Please enter valid input'
        return str


def current_temperature(json_data):
    try:
        temp_fh = str(pytemperature.k2f(json_data['main']['temp']))
        return temp_fh

    except Exception:
        float = 'Please enter valid input'
        return float


def current_humidity(json_data):
    try:
        humidity = str(json_data['main']['humidity'])
        return humidity

    except Exception:
        int = 'Please enter valid input'
        return int


def current_pressure(json_data):
    try:
        pressure = str(round(((json_data['main']['pressure']) * 0.029529983071445), 2))
        return pressure

    except Exception:
        float = 'Please enter valid input'
        return float


def low_temperature(json_data):
    try:
        lowtemp_fh = str(pytemperature.k2f(json_data['main']['temp_min']))
        return lowtemp_fh

    except Exception:
        float = 'Please enter valid input'
        return float


def high_temperature(json_data):
    try:
        hightemp_fh = str(pytemperature.k2f(json_data['main']['temp_max']))
        return hightemp_fh

    except Exception:
        float = 'Please enter valid input'
        return float


if __name__ == '__main__':

    choice = 'y'
    while choice.lower() == 'y':
        print("ISQA 4900 Open Weather API")
        print(now)
        city = input('Enter city: \t')
        print('Use ISO letter country code like: https://countrycode.org/')
        country = input('Enter the country code: \t')
        api_start = 'https://api.openweathermap.org/data/2.5/weather?q='
        api_key = '&appid=19e9a25146ef7516044eb1d272dc6ec4'
        url = api_start + city + ',' + country + api_key
        json_data = requests.get(url).json()
        current_conditions = check_current_conditions(json_data)
        temp_fh = current_temperature(json_data)
        pressure = current_pressure(json_data)
        humidity = current_humidity(json_data)
        lowtemp_fh = low_temperature(json_data)
        hightemp_fh = high_temperature(json_data)
        print('Current conditions: ' + current_conditions)
        print('Current Temperature in Fahrenheit: ' + temp_fh)
        print('Current pressure in inHg: ' + pressure)
        print('Current % Humidity:  ' + humidity)
        print('Expected low temperature in Fahrenheit: ' + lowtemp_fh)
        print('Expected high temperature in Fahrenheit: ' + hightemp_fh)
        choice = input("Continue(y/n)?")
        if choice.lower() != "y" and choice.lower() != "n":
            print("Invalid response!")
            choice = input("Continue (y/n)?: ")
        print("Bye!")

