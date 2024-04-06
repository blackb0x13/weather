import requests as req
from time_converter import time_converter

def get_wx_forecast(lat, lon):
    api_key = "c65721c8b8ebe44c49c4a61e38381ac5"
    wf_api = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial'
    value = req.get(wf_api)
    json_response = value.json()

    for i in range(len(json_response['list'])):
        json_response_list_val = json_response['list'][i]
        timestamp = time_converter(json_response_list_val['dt'])
    
    return timestamp