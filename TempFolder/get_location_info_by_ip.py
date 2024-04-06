import requests

def get_timezone_by_ip(ip_address):
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    data = response.json()
    return data.get('timezone', 'Timezone could not be determined.')

def get_public_ip():
    response = requests.get('https://api.ipify.org')
    if response.status_code == 200:
        return response.text
    else:
        return 'Could not obtain IP address'

public_ip = get_public_ip()

timezone = get_timezone_by_ip(public_ip)

def get_city_and_state_by_ip(ip_address):
    response = requests.get(f'https://ipinfo.io/{ip_address}?token=292716b5de2410')
    data = response.json()
    print(data)
    city = data['city']
    state = data['region']
    return city, state

city, state = get_city_and_state_by_ip(public_ip)
print(city+ ", " + state )