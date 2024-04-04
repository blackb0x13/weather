import requests
import json

def get_pollution_data(api_url):
    """
    Retrieves pollution data from an API and returns relevant fields.

    Args:
        api_url (str): The URL of the pollution API.

    Returns:
        dict: A dictionary containing relevant pollution data fields.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception if the response status code is not 200

        data = response.json()

        # Extract relevant fields (modify as needed based on the API response structure)
        pollution_data = {
            "city": data.get("city", ""),
            "pm25": data.get("pm25", ""),
            "pm10": data.get("pm10", ""),
            "o3": data.get("o3", ""),
            "aqi": data.get("aqi", ""),
        }

        return pollution_data
    except requests.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        return None

# Example usage: Replace with the actual pollution API URL
pollution_api_url = "https://api.example.com/pollution"
pollution_result = get_pollution_data(pollution_api_url)

if pollution_result:
    print("Pollution data:")
    for key, value in pollution_result.items():
        print(f"{key}: {value}")
else:
    print("Failed to retrieve pollution data.")
