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

    day_two = json_response['list'][1]
    day_two_dt = day_two['dt']
    day_two_temp = day_two['main']['temp']
    day_two_feels_like = day_two['main']['feels_like']
    day_two_temp_min = day_two['main']['temp_min']
    day_two_temp_max = day_two['main']['temp_max']
    day_two_humidity = day_two['main']['humidity']

    day_three = json_response['list'][2]
    day_three_dt = day_three['dt']
    day_three_temp = day_three['main']['temp']
    day_three_feels_like = day_three['main']['feels_like']
    day_three_temp_min = day_three['main']['temp_min']
    day_three_temp_max = day_three['main']['temp_max']
    day_three_humidity = day_three['main']['humidity']

    day_four = json_response['list'][3]
    day_four_dt = day_four['dt']
    day_four_temp = day_four['main']['temp']
    day_four_feels_like = day_four['main']['feels_like']
    day_four_temp_min = day_four['main']['temp_min']
    day_four_temp_max = day_four['main']['temp_max']
    day_four_humidity = day_four['main']['humidity']

    day_five = json_response['list'][4]
    day_five_dt = day_five['dt']
    day_five_temp = day_five['main']['temp']
    day_five_feels_like = day_five['main']['feels_like']
    day_five_temp_min = day_five['main']['temp_min']
    day_five_temp_max = day_five['main']['temp_max']
    day_five_humidity = day_five['main']['humidity']

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

    day_one = f'Time: {day_one_dt}, Temperature: {day_one_temp}, Temperature Feels Like: {day_one_feels_like}, Temperature Min: {day_one_temp_min}, Temperature Max: {day_one_temp_max}, Humidity {day_one_humidity}'
    day_two = f'Time: {day_two_dt}, Temperature: {day_two_temp}, Temperature Feels Like: {day_two_feels_like}, Temperature Min: {day_two_temp_min}, Temperature Max: {day_two_temp_max}, Humidity {day_two_humidity}'
    day_three = f'Time: {day_three_dt}, Temperature: {day_three_temp}, Temperature Feels Like: {day_three_feels_like}, Temperature Min: {day_three_temp_min}, Temperature Max: {day_three_temp_max}, Humidity {day_three_humidity}'
    day_four = f'Time: {day_four_dt}, Temperature: {day_four_temp}, Temperature Feels Like: {day_four_feels_like}, Temperature Min: {day_four_temp_min}, Temperature Max: {day_four_temp_max}, Humidity {day_four_humidity}'
    day_five = f'Time: {day_five_dt}, Temperature: {day_five_temp}, Temperature Feels Like: {day_five_feels_like}, Temperature Min: {day_five_temp_min}, Temperature Max: {day_five_temp_max}, Humidity {day_five_humidity}'
    # day_six = f'Time: {day_six_dt}, Temperature: {day_six_temp}, Temperature Feels Like: {day_six_feels_like}, Temperature Min: {day_six_temp_min}, Temperature Max: {day_six_temp_max}, Humidity {day_six_humidity}'
    # day_seven = f'Time: {day_seven_dt}, Temperature: {day_seven_temp}, Temperature Feels Like: {day_seven_feels_like}, Temperature Min: {day_seven_temp_min}, Temperature Max: {day_seven_temp_max}, Humidity {day_seven_humidity}'

    
    return(day_one, day_two, day_three, day_four, day_five)






    

