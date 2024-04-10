# you can use whatever libraries you like, but we recommend starting with these two
# import requests
# import numpy as np

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key. You will have to sign up and get your own key (visit the link below)
# OPENWEATHERMAP_API_KEY = 'YOUR_API_KEY'
# OPENWEATHERMAP_API_URL = 'http://api.openweathermap.org/data/2.5/weather'

# you can have your application run in the terminal or you can use a library like Tkinter to make it work on the desktop  
#
# Your application must meet the following requirements:
#
# 1- correctly displays data for a given user input (daily)
# 2- displays t-3 data for a given user input (past 3 days)
# 3- displays t+5 data for a given user input (weekly forecast)
# 4- displays 3-year-average for a given input to a particular day (historical data average)

# students will be graded based on attempted code. if no solution is attemped for a given criteria, minimum score will be given (5 points)
# MVP is 55 points across all four criteria 
# students are encouraged to read openweathermap.org documentation before attempting to write their solution



# import requests

# api_key = 'YOUR_API_KEY'

# city = input('Enter city name: ')

# url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     temp = data['main']['temp']
#     desc = data['weather'][0]['description']
#     print(f'Temperature: {temp} K')
#     print(f'Description: {desc}')
# else:
#     print('Error fetching weather data')



# weather.py
 2
 3# ...
 4
 5def display_weather_info(weather_data, imperial=False):
 6
 7    # ...
 8
 9    city = weather_data["name"]
10    weather_id = weather_data["weather"][0]["id"]
11    weather_description = weather_data["weather"][0]["description"]
12    temperature = weather_data["main"]["temp"]
13
14    style.change_color(style.REVERSE)
15    print(f"{city:^{style.PADDING}}", end="")
16    style.change_color(style.RESET)
17
18    if weather_id in THUNDERSTORM:
19        style.change_color(style.RED)
20    elif weather_id in DRIZZLE:
21        style.change_color(style.CYAN)
22    elif weather_id in RAIN:
23        style.change_color(style.BLUE)
24    elif weather_id in SNOW:
25        style.change_color(style.WHITE)
26    elif weather_id in ATMOSPHERE:
27        style.change_color(style.BLUE)
28    elif weather_id in CLEAR:
29        style.change_color(style.YELLOW)
30    elif weather_id in CLOUDY:
31        style.change_color(style.WHITE)
32    else:  # In case the API adds new weather codes
33        style.change_color(style.RESET)
34    print(
35        f"\t{weather_description.capitalize():^{style.PADDING}}",
36        end=" ",
37    )
38    style.change_color(style.RESET)
39
40    print(f"({temperature}°{'F' if imperial else 'C'})")
# Global Fishing Watch: This platform focuses on improving the management of the ocean through data analysis and sharing. They harness big data from satellites and other sources to monitor commercial fishing, transshipment at sea, shipping, and even forced labor abuses on vessels. Their technology stack includes AIS tracking, radar, optical and nighttime imagery combined with machine learning. They offer APIs for accessing their comprehensive vessel registry database, which is classified into various vessel categories like trawler, longliner, and cargo.

# Fishial.AI: Aimed at creating a highly accurate fish identification tool, Fishial.AI utilizes artificial intelligence for educational exploration and conservation awareness. They are building the largest open-source fish species image library labeled for AI machine learning, aiming to develop an open-source AI model for worldwide fish species identification. They offer a developer API that could be useful for projects requiring fish identification capabilities.

# API Fish Care: Although not directly offering an API for fishing locations or activities, API Fish Care is focused on aquarium and pond care products. They provide various resources, treatments, and testing kits for aquarium enthusiasts. While their main focus is on products for fish care rather than fishing activities, their resources might be beneficial for individuals interested in aquatic life.


# WeatherAPI.com: Offers a comprehensive API for weather data, including hourly and daily forecasts, historical data, astronomy, and more, with output in JSON and XML formats.

# Open-Meteo.com: Provides high-resolution weather data for free, sourced from national weather services. The data ranges from 1 to 11 kilometers in resolution, available via a user-friendly JSON API.

# OpenWeatherMap: Features a wide range of weather APIs, including current weather data, forecasts, historical data archives, and future predictions. It supports various data formats and integration methods, making it versatile for different project needs.

# Visual Crossing: Offers an easy-to-use global weather API that includes historical weather data, current conditions, up-to-date forecasts, and historical forecast information. It provides a single-endpoint forecast and weather history API.

# Weatherbit: This API provides detailed weather data, including forecasts, historical weather observations, and more. It's backed by multiple data sources and utilizes advanced methods for data accuracy.

