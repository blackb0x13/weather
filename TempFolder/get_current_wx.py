import requests as req

def get_current_wx_by_lat_long(lat, long):
    api_key = "c65721c8b8ebe44c49c4a61e38381ac5"
    api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}&units=imperial'
    result = req.get(api_url)
    json_response = result.json()
    weather = json_response['weather']
    main = json_response['main']
    curr_wx_dict = dict([
        ('temp', main['temp']),
        ('feels_like', main['feels_like']), 
        ('temp_min', main['temp_min']), 
        ('temp_max', main['temp_max']), 
        ('humidity', main['humidity']),
        ('description', weather[0]['description'])
        ])
    return curr_wx_dict

# temp_dict = (get_current_wx_by_lat_long(33,34))
# temp = list(str(round(float(temp_dict['temp']))))
# print(temp)