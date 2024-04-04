"""
Here are some suggestions to improve your Python code:

Error Handling: Add error handling to manage potential issues, such as a failed API request or unexpected data structure.
API Key: Avoid hardcoding the API key in the function definition. It’s better to pass it as an argument or read it from a secure place.
Function Documentation: Add a docstring at the beginning of the function to explain what it does, its parameters, and its return value.
Code Readability: Use more descriptive variable names to make the code easier to understand.
Code Efficiency: Instead of accessing the dictionary values directly which might lead to KeyError, use the get() method which provides a default value when the key is missing.
"""

import requests as req
import json

def get_weather_forecast(lat, lon, api_key):
    """
    Fetches weather forecast data from the OpenWeatherMap API.
    
    Parameters:
    lat (float): Latitude of the location
    lon (float): Longitude of the location
    api_key (str): OpenWeatherMap API key

    Returns:
    str: A summary of the weather forecast
    """
    wf_api = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial'
    response = req.get(wf_api)
    
    # Check if the request was successful
    if response.status_code != 200:
        return "Error: Unable to fetch weather data"
    
    json_response = response.json()
    
    # Extract the required information
    day_one = json_response.get('list', [{}])[0]
    main_info = day_one.get('main', {})
    
    day_one_dt = day_one.get('dt')
    day_one_temp = main_info.get('temp')
    day_one_feels_like = main_info.get('feels_like')
    day_one_temp_min = main_info.get('temp_min')
    day_one_temp_max = main_info.get('temp_max')
    day_one_humidity = main_info.get('humidity')
    
    forecast_summary = f'Time: {day_one_dt}, Temperature: {day_one_temp}, Temperature Feels Like: {day_one_feels_like}, Temperature Min: {day_one_temp_min}, Temperature Max: {day_one_temp_max}, Humidity {day_one_humidity}'
    
    return forecast_summary

print(get_weather_forecast(51.5074, -0.1278, "7884f12f73331ee09fc8f5a48633b801"))