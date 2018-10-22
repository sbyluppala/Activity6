# Activity 6 - Working with API’s and JSON

## Objectives
* Demonstrate a your knowledge of how to sign up for an **Application Programming Interface (API)** service and understand the documentation and use the API to solve a problem in Python. 
* Demonstrate a your knowledge of how to work with **JSON** which is treated as a dictionary in Python and extract data from the JSON returned in a program and present the output in a printed format. 
* Demonstrate a your knowledge of how to `pip install` useful addon python tools to your python program. 
* Demonstrate your knowledge of modular programming using Python. 

## Background
As a web application developer you will frequently be asked to work with many different Application Programming Interfaces in external services.  You are likely familiar with adding a location service by embedding a Google Map widget. However there are many other services that are available to the developer. A partial list of these apis are available at [Programmable Web](https://www.programmableweb.com). We will use a service that provides current weather information. This can be very useful for a number of applications such as travel websites. We will use the service from [Open Weather Map](https://openweathermap.org). You will sign up for the API and obtain an api key and will use it to provide current weather for a given city. 

The format that is returned from older API’s was XML. However modern API’s today typically use JSON today. **JSON** (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. Link to [json.org](https://www.json.org)

## Directions
There is an activity6.py program file. Erase the current code in the file and create the code to complete the following requirements.

1. Now go to [Open Weather Map](https://openweathermap.org) and sign up for an account and obtain a free key for the api’s. We will use the api in a python program to allow the city and country to be identified and will return the current weather for that day in JSON. The output of the [Open Weather Map](https://openweathermap.org) program will look like this:

![openweathermaps-json-output](https://github.com/uno-isqa-4900/activity6/blob/master/images/openweathermap-json-output.png)

2. Once you are sure that the key is working and you are bringing back data in [Postman](https://www.getpostman.com) or your browser then your are ready to develop a program which will generate the following:
 
![activity6-output](https://github.com/uno-isqa-4900/activity6/blob/master/images/activity6-output.png)
 
3. Now that you have a good API key tested using Postman or even a browser, you are now ready to begin. We will need to install an important tool to allow python to interact with an API. This is requests. See: [Python-Requests](http://docs.python-requests.org/en/master). It is a simply library which allows python to interact with APIs and is one of the most downloaded python libraries.. To install requests in your virtual machine issue the following command: `pip install requests`. 

4. Optionally you can use one of many python conversion tools or you can convert degrees Kelvin to degrees Fahrenheit manually. The one I chose was [pytemperature](https://pypi.org/project/pytemperature). Simply `pip install pytemperature` and follow the conversion directions in the website.

5. Since these kind of programs may be new to you if you have never worked with an API, I will provide you with some of the sample code I used to solve this problem.  Your job will be to complete the program so your program operates as shown in the above illustration. Below is the starter code:

```Python
import urllib.parse
import requests
import pytemperature


def check_current_conditions(json_data):

    try:
        current_conditions = json_data['weather'][0]['description']
        return current_conditions

    except Exception:
        str = 'Please enter valid input'
        return str


def current_temperature(json_data):
    pass
    
def current_humidity(json_data):
    pass
    
def low_temperature(json_data):
    pass
   
def high_temperature(json_data):
    pass
   
if __name__ == '__main__':

    choice = 'y'
    while choice.lower() == 'y':
        print("ISQA 4900 Open Weather API")
        city = input('Enter city: ')
        print('Use ISO letter country code like: https://countrycode.org/')
        country = input('Enter the country code: ')
        api_start = 'https://api.openweathermap.org/data/2.5/weather?q='
        api_key = '&appid=YOUR API KEY HERE!!!'
        url = api_start + city + ',' + country + api_key
        json_data = requests.get(url).json()
        current_conditions = check_current_conditions(json_data)
        print('Current conditions: '+ current_conditions)
        choice = input("Continue(y/n)?")
        print()
        print("Bye!")
```

6. If you add your key you should see a small part of the working as shown below:

![activity6-partial-output](https://github.com/uno-isqa-4900/activity6/blob/master/images/activity6-partial-output.png)

7. Make sure to write your logic within the respective functions inside your program and also check for exceptions if the user inputs incorrect data for city and country by showing 'Please enter valid input'

8. check_current_conditions returns the parsed JSON response for the current conditions. You have to write the logic inside functions current_temperature, current_humidity, low_temperature, high_temperature to retrieve current temperature, current_humidity, low temperature and high temperature values respectively.

8. All the functions should return value to the main function and print the value in the main function.

9. Make sure to enter the API key in the TestActivity6.py file as well

Your job will be to complete the code so that it prints out as shown at the beginning of this exercise with properly formatted dates, numbers and values. You will need to do some additional conversions manually. To parse the JSON fields use your knowledge of python dictionaries. When python works with a JSON object it treats it like a dictionary.

## Submitting your assignment
1. When you are happy with your working code push the code to GitHub and be sure your GitHub repository is updated.
2. Create a markdown file/document and make one or more  screenshots of the code working in the command line. Run several different cities in different countries to test it out. Add it to the markdown file/document labeled 4900_Activity6.

## Rubric

| Items | Exemplary  (90% - 100%) | Competent  (80% - 89%) | Acceptable  (70% - 79%) | Insufficient  (below 70%) |
|:--------------------------:|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------:|:------------------------------------------------------------------------:|:-------------------------------------------------------:|
| Python Code (max 15 pts) | Functions as described above and has appropriate comments in the code | Generally functions as described above and has some but not all comments | Partially functions as described above and may lack appropriate comments | Does not function as described above and lacks comments |
| Git and GitHub (max 5 pts) | One or more commits with all code replicated and appropriate commit comment | Code updated in GitHub but lacking an appropriate commit comment | Code not updated in GitHub | Code not updated in GitHub |
|  |  |  |  |  |
