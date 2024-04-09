import requests as req

def get_lat_long_by_city_state(city, state, country="US", limit=1):
   api_key = "c65721c8b8ebe44c49c4a61e38381ac5"
   api_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={api_key}'
   result = req.get(api_url)
   json_response = result.json()
   lat, long = json_response[0]['lat'], json_response[0]['lon']

   return (lat, long)

def get_lat_long_by_zip(zip, country="US"):
    api_key = "c65721c8b8ebe44c49c4a61e38381ac5"
    api_url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip},{country}&appid={api_key}'
    result = req.get(api_url)
    json_response = result.json()
    lat, long = json_response['lat'], json_response['lon']

    return (lat, long)
    
# lat, long = get_lat_long_by_city_state("pittsburgh", "pa")
# print(str(lat) + " " + str(long))
# lat, long = get_lat_long_by_zip("15228")
# print(str(lat) + " " + str(long))
