from datetime import datetime
import requests
import pytemperature

now = datetime.now()
now = datetime.strftime(now, '%A, %d %B, %Y')

print("ISQA 3900 Open Weather API")
print(now)

print()
choice = "y"
while choice.lower() == "y":
    city = input("Enter city:     ")
    print("Use ISO letter country code like: https://countrycode.org/")
    country = input("Enter country code:     ")

    api_start = 'https://api.openweathermap.org/data/2.5/weather?q='

    api_key = '&appid=19e9a25146ef7516044eb1d272dc6ec4'

    url = api_start + city + ',' + country + api_key

    json_data = requests.get(url).json()
    weather_description = json_data['weather'][0]['description']
    temp_fh = pytemperature.k2f(json_data['main']['temp'])
    pressure = str(round(((json_data['main']['pressure'])*0.029529983071445), 2))
    humidity = json_data['main']['humidity']
    lowtemp_fh = pytemperature.k2f(json_data['main']['temp_min'])
    hightemp_fh = pytemperature.k2f(json_data['main']['temp_max'])

    print("Current conditions:  ", weather_description)
    print("Current Temperature in Fahrenheit:  ", temp_fh)
    print("Current pressure in inHg:  ", pressure)
    print("Current % Humidity:  ", humidity)
    print("Expected low temperature in Fahrenheit:  ", lowtemp_fh)
    print("Expected high temperature in Fahrenheit:  ", hightemp_fh)

    choice = input("Continue (y/n)?: ")
    print()
print('Bye')

