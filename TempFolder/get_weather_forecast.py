import requests as req
from time_converter import time_converter
import random

def get_wx_forecast(lat, lon):
    api_key = "c65721c8b8ebe44c49c4a61e38381ac5"
    wf_api = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial'
    value = req.get(wf_api)
    json_response = value.json()

    forecast_list = list()
    for i in range(len(json_response['list'])):
        json_response_list_val = json_response['list'][i]
        timestamp = time_converter(json_response_list_val['dt'])
        max_temp = json_response_list_val['main']['temp_max']
        min_temp = json_response_list_val['main']['temp_min']
        humidity = json_response_list_val['main']['humidity']

        fc_line = f"{timestamp} MAX: {max_temp} MIN: {min_temp} HUM: {humidity}?"
        forecast_list.append(fc_line)
        #add fake odds
        #random 10XXX and 10XXX+1, random plus 300, random minus 300]
        random_ticket = random.randint(10000, 10999)
        ticket_pair = [random_ticket, random_ticket+1]
        random_yes = random.randint(100, 300)
        random_no = random.randint(100, 300)
        sign = random.choice(["+", "-"])
        if sign == "+":
            opposite_sign = "-"
        elif sign == "-":
            opposite_sign = "+"
        odds_pair = [sign+str(random_yes), opposite_sign+str(random_no)]

        forecast_list.append(f"{ticket_pair[0]} YES                                                                      {odds_pair[0]}")
        forecast_list.append(f"{ticket_pair[1]} NO                                                                       {odds_pair[1]}")
                             
    
    return forecast_list


print(get_wx_forecast(33,34))

