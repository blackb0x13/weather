import requests as req

def get_current_air_quality(lat, long):
    api_key = "9f5c9e267e333f4b42865fe875533b3e"
    api_url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={long}&appid={api_key}'
    response = req.get(api_url)
    if response.status_code == 200:
        json_response = response.json()
        # print(json_response)
        air = list(json_response.values())
        # aqi = air[0]['main']['aqi']
        # print(aqi)
        final_aqi = str(air[1][0]['main']['aqi'])
        print("AQI: " + final_aqi)
        return final_aqi
    else:
        print('Error fetching air quality data')


get_current_air_quality(33, 34)

# api_key = "9f5c9e267e333f4b42865fe875533b3e"
# zip_code = input('Enter the zip code of the city you want the weather for: ')
# country_code = input('What is the country code? ')
# limit = 0
# geo_url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}'
# response = req.get(geo_url)

# if response.status_code == 200:
#     data = response.json()
#     location = list(data.values())
#     lat = location[2]
#     long = location[3]
#     # print(lat)
#     # print(long)
#     get_current_air_quality(lat, long)  # Call the function with lat and long
# else:
#     print('Error fetching geo data')
