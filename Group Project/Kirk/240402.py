import requests as req
import json

def get_weather_forecast(lat, lon, api_key = "7884f12f73331ee09fc8f5a48633b801"):

    wf_api = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial'
    value = req.get(wf_api)
    json_response = value.json()
    # timezone = json_response['timezone']
    # current_temp = json_response['current']['temp']

    day_one = json_response['list'][0]
    day_one_dt = day_one['dt']
    day_one_temp = day_one['main']['temp']
    day_one_feels_like = day_one['main']['feels_like']
    day_one_temp_min = day_one['main']['temp_min']
    day_one_temp_max = day_one['main']['temp_max']
    day_one_humidity = day_one['main']['humidity']

#test code for commit purposes


    day_two = json_response['list'][0]
    day_two_dt = day_two['dt']
    day_two_temp = day_two['main']['temp']
    day_two_feels_like = day_two['main']['feels_like']
    day_two_temp_min = day_two['main']['temp_min']
    day_two_temp_max = day_two['main']['temp_max']
    day_two_humidity = day_two['main']['humidity']

    test_summary = f'Time: {day_one_dt}, Temperature: {day_one_temp}, Temperature Feels Like: {day_one_feels_like}, Temperature Min: {day_one_temp_min}, Temperature Max: {day_one_temp_max}, Humidity {day_one_humidity}'
    test_summary2 = f'Time: {day_two_dt}, Temperature: {day_two_temp}, Temperature Feels Like: {day_two_feels_like}, Temperature Min: {day_two_temp_min}, Temperature Max: {day_two_temp_max}, Humidity {day_two_humidity}'
    
    
    return [test_summary, test_summary2]


result = get_weather_forecast(33,34,"7884f12f73331ee09fc8f5a48633b801")
print(result)


"""ChatGPT show this as a replacement for a one line, but seems confusing
day_one_dt, day_one_temp, day_one_feels_like, day_one_temp_min, day_one_temp_max, day_one_humidity = (
    day_one.get('dt'),
    main_info.get('temp'),
    main_info.get('feels_like'),
    main_info.get('temp_min'),
    main_info.get('temp_max'),
    main_info.get('humidity')
)
"""

    

