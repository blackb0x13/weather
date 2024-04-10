import requests as req
import json

def get_weather_forecast():

    # Define the weather API endpoint
    api_url = "https://api.openweathermap.org/data/2.5/forecast"
    api_key = "7884f12f73331ee09fc8f5a48633b801"  

    # Define the city and country code (hard code for now until we convert lat)
    city = "Vancouver"
    country_code = "CA"

    # Define the parameters for the API request
    params = {
    "q": f"{city},{country_code}",
    "appid": api_key,
    "units": "imperial",  # Use imperial units (Fahrenheit)
    #"cnt": 7,  # Retrieve data for 1 days 3hr intervals 8 times a day
    "cnt": 40,  # Retrieve data for 5 days 3hr intervals 8 times a day
    }

    # Make the API request
    response = req.get(api_url, params=params)
    data = response.json()

    # Extract and print weather data for the next 7 days
    for day in data["list"]:
        date = day["dt_txt"]
        temp = day["main"]["temp"]
        description = day["weather"][0]["description"]   #pulls in the data from API
        print(f"{date}: {temp}°F, {description}")

    return()

get_weather_forecast()

