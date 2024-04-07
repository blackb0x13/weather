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
    "cnt": 7,  # Retrieve data for 7 days
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

# JSON code from openweathermap.org
# {
#   "cod": "200",
#   "message": 0,
#   "cnt": 40,
#   "list": [
#     {
#       "dt": 1661871600,
#       "main": {
#         "temp": 296.76,
#         "feels_like": 296.98,
#         "temp_min": 296.76,
#         "temp_max": 297.87,
#         "pressure": 1015,
#         "sea_level": 1015,
#         "grnd_level": 933,
#         "humidity": 69,
#         "temp_kf": -1.11
#       },
#       "weather": [
#         {
#           "id": 500,
#           "main": "Rain",
#           "description": "light rain",
#           "icon": "10d"
#         }
#       ],
#       "clouds": {
#         "all": 100
#       },
#       "wind": {
#         "speed": 0.62,
#         "deg": 349,
#         "gust": 1.18
#       },
#       "visibility": 10000,
#       "pop": 0.32,
#       "rain": {
#         "3h": 0.26
#       },
#       "sys": {
#         "pod": "d"
#       },
#       "dt_txt": "2022-08-30 15:00:00"
#     },
#         {
#       "dt": 1661882400,
#       "main": {
#         "temp": 295.45,
#         "feels_like": 295.59,
#         "temp_min": 292.84,
#         "temp_max": 295.45,
#         "pressure": 1015,
#         "sea_level": 1015,
#         "grnd_level": 931,
#         "humidity": 71,
#         "temp_kf": 2.61
#       },
#       "weather": [
#         {
#           "id": 500,
#           "main": "Rain",
#           "description": "light rain",
#           "icon": "10n"
#         }
#       ],
#       "clouds": {
#         "all": 96
#       },
#       "wind": {
#         "speed": 1.97,
#         "deg": 157,
#         "gust": 3.39
#       },
#       "visibility": 10000,
#       "pop": 0.33,
#       "rain": {
#         "3h": 0.57
#       },
#       "sys": {
#         "pod": "n"
#       },
#       "dt_txt": "2022-08-30 18:00:00"
#     },
#     {
#       "dt": 1661893200,
#       "main": {
#         "temp": 292.46,
#         "feels_like": 292.54,
#         "temp_min": 290.31,
#         "temp_max": 292.46,
#         "pressure": 1015,
#         "sea_level": 1015,
#         "grnd_level": 931,
#         "humidity": 80,
#         "temp_kf": 2.15
#       },
#       "weather": [
#         {
#           "id": 500,
#           "main": "Rain",
#           "description": "light rain",
#           "icon": "10n"
#         }
#       ],
#       "clouds": {
#         "all": 68
#       },
#       "wind": {
#         "speed": 2.66,
#         "deg": 210,
#         "gust": 3.58
#       },
#       "visibility": 10000,
#       "pop": 0.7,
#       "rain": {
#         "3h": 0.49
#       },
#       "sys": {
#         "pod": "n"
#       },
#       "dt_txt": "2022-08-30 21:00:00"
#     },
#     {
#       "dt": 1662292800,
#       "main": {
#         "temp": 294.93,
#         "feels_like": 294.83,
#         "temp_min": 294.93,
#         "temp_max": 294.93,
#         "pressure": 1018,
#         "sea_level": 1018,
#         "grnd_level": 935,
#         "humidity": 64,
#         "temp_kf": 0
#       },
#       "weather": [
#         {
#           "id": 804,
#           "main": "Clouds",
#           "description": "overcast clouds",
#           "icon": "04d"
#         }
#       ],
#       "clouds": {
#         "all": 88
#       },
#       "wind": {
#         "speed": 1.14,
#         "deg": 17,
#         "gust": 1.57
#       },
#       "visibility": 10000,
#       "pop": 0,
#       "sys": {
#         "pod": "d"
#       },
#       "dt_txt": "2022-09-04 12:00:00"
#     }
#   ],
#   "city": {
#     "id": 3163858,
#     "name": "Zocca",
#     "coord": {
#       "lat": 44.34,
#       "lon": 10.99
#     },
#     "country": "IT",
#     "population": 4593,
#     "timezone": 7200,
#     "sunrise": 1661834187,
#     "sunset": 1661882248
#   }
# }

# Notes:

# Collapse lines of code in VS Code 
# Pull live data out of a API, or do I plan to pull it initially in this function? Pull todays temp when clicking a button, should I pull and have that info ready and prepared or show them how?
 
 
 
 
 
 
   # wf_api = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial'
    # value = req.get(wf_api)
    # json_response = value.json()
    # timezone = json_response['timezone']
    # current_temp = json_response['current']['temp']

    # day_one = json_response['list'][0]
    # day_one_dt = day_one['dt']
    # day_one_temp = day_one['main']['temp']
    # day_one_feels_like = day_one['main']['feels_like']
    # day_one_temp_min = day_one['main']['temp_min']
    # day_one_temp_max = day_one['main']['temp_max']
    # day_one_humidity = day_one['main']['humidity']

    # day_two = json_response['list'][1]
    # day_two_dt = day_two['dt']
    # day_two_temp = day_two['main']['temp']
    # day_two_feels_like = day_two['main']['feels_like']
    # day_two_temp_min = day_two['main']['temp_min']
    # day_two_temp_max = day_two['main']['temp_max']
    # day_two_humidity = day_two['main']['humidity']

    # day_three = json_response['list'][2]
    # day_three_dt = day_three['dt']
    # day_three_temp = day_three['main']['temp']
    # day_three_feels_like = day_three['main']['feels_like']
    # day_three_temp_min = day_three['main']['temp_min']
    # day_three_temp_max = day_three['main']['temp_max']
    # day_three_humidity = day_three['main']['humidity']

    # day_four = json_response['list'][3]
    # day_four_dt = day_four['dt']
    # day_four_temp = day_four['main']['temp']
    # day_four_feels_like = day_four['main']['feels_like']
    # day_four_temp_min = day_four['main']['temp_min']
    # day_four_temp_max = day_four['main']['temp_max']
    # day_four_humidity = day_four['main']['humidity']

    # day_five = json_response['list'][4]
    # day_five_dt = day_five['dt']
    # day_five_temp = day_five['main']['temp']
    # day_five_feels_like = day_five['main']['feels_like']
    # day_five_temp_min = day_five['main']['temp_min']
    # day_five_temp_max = day_five['main']['temp_max']
    # day_five_humidity = day_five['main']['humidity']

    # day_six = json_response['list'][5]
    # day_six_dt = day_six['dt']
    # day_six_temp = day_six['main']['temp']
    # day_six_feels_like = day_six['main']['feels_like']
    # day_six_temp_min = day_six['main']['temp_min']
    # day_six_temp_max = day_six['main']['temp_max']
    # day_six_humidity = day_six['main']['humidity']

    # day_seven = json_response['list'][6]
    # day_seven_dt = day_seven['dt']
    # day_seven_temp = day_seven['main']['temp']
    # day_seven_feels_like = day_seven['main']['feels_like']
    # day_seven_temp_min = day_seven['main']['temp_min']
    # day_seven_temp_max = day_seven['main']['temp_max']
    # day_seven_humidity = day_seven['main']['humidity']

    # Extract relevant information
    # date_time = day_one_dt["dt"]
    # temperature = weather_data["temp"]
    # feels_like = weather_data["feels_like"]
    # pressure = weather_data["pressure"]
    # humidity = weather_data["humidity"]
    # dew_point = weather_data["dew_point"]
    # uvi = weather_data["uvi"]
    # clouds = weather_data["clouds"]
    # visibility = weather_data["visibility"]
    # wind_speed = weather_data["wind_speed"]
    # wind_deg = weather_data["wind_deg"]
    # wind_gust = weather_data["wind_gust"]



    # day_one = f'Time: {day_one_dt}, Temperature: {day_one_temp}, Temperature Feels Like: {day_one_feels_like}, Temperature Min: {day_one_temp_min}, Temperature Max: {day_one_temp_max}, Humidity {day_one_humidity}'
    # day_two = f'Time: {day_two_dt}, Temperature: {day_two_temp}, Temperature Feels Like: {day_two_feels_like}, Temperature Min: {day_two_temp_min}, Temperature Max: {day_two_temp_max}, Humidity {day_two_humidity}'
    # day_three = f'Time: {day_three_dt}, Temperature: {day_three_temp}, Temperature Feels Like: {day_three_feels_like}, Temperature Min: {day_three_temp_min}, Temperature Max: {day_three_temp_max}, Humidity {day_three_humidity}'
    # day_four = f'Time: {day_four_dt}, Temperature: {day_four_temp}, Temperature Feels Like: {day_four_feels_like}, Temperature Min: {day_four_temp_min}, Temperature Max: {day_four_temp_max}, Humidity {day_four_humidity}'
    # day_five = f'Time: {day_five_dt}, Temperature: {day_five_temp}, Temperature Feels Like: {day_five_feels_like}, Temperature Min: {day_five_temp_min}, Temperature Max: {day_five_temp_max}, Humidity {day_five_humidity}'
    # day_six = f'Time: {day_six_dt}, Temperature: {day_six_temp}, Temperature Feels Like: {day_six_feels_like}, Temperature Min: {day_six_temp_min}, Temperature Max: {day_six_temp_max}, Humidity {day_six_humidity}'
    # day_seven = f'Time: {day_seven_dt}, Temperature: {day_seven_temp}, Temperature Feels Like: {day_seven_feels_like}, Temperature Min: {day_seven_temp_min}, Temperature Max: {day_seven_temp_max}, Humidity {day_seven_humidity}'

    

