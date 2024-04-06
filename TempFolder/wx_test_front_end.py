import tkinter as tk
from tkinter import ttk
from get_lat_lon_by_loc import get_lat_long_by_zip, get_lat_long_by_city_state
from get_current_wx import get_current_wx_by_lat_long
from get_weather_forecast import get_wx_forecast
from get_location_info_by_ip import get_public_ip, get_city_and_state_by_ip

def get_local_weather(city, state):
     lat, long = get_lat_long_by_city_state(city, state)
     current_weather_dict = get_current_wx_by_lat_long(lat, long)
     current_weather = f"{current_weather_dict['description'].capitalize()}, {current_weather_dict['temp']}°F"
     return current_weather
     

def get_weather():
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_entry.get()

    if zip_code is not None and zip_code != "":
         lat, long = get_lat_long_by_zip(zip_code)
    elif state not in (None, "") and city not in (None, ""):
         lat, long = get_lat_long_by_city_state(city, state)
    else:
         current_weather_var.set(f"Please enter a city and state, or a ZIP code.")
         
    current_weather_dict = get_current_wx_by_lat_long(lat, long)
    current_weather = f"{current_weather_dict['description'].capitalize()}, {current_weather_dict['temp']}°F"
    forecast_weather = f'NOT IMPLEMENTED: {get_wx_forecast(lat, long)}'    
    current_weather_var.set(f"Current Weather for\nSelected Location:\n{current_weather}")
    forecast_var.set(forecast_weather)

# Creating the main window
root = tk.Tk()
root.title("Weather App")

# Creating StringVars to hold input and output values
current_weather_var = tk.StringVar()
forecast_var = tk.StringVar()
local_city_var = tk.StringVar()
local_weather_var=tk.StringVar()

# Creating and placing input fields for city, state, and zip
tk.Label(root, text="City:").grid(row=0, column=0)
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1)

tk.Label(root, text="State:").grid(row=1, column=0)
state_entry = tk.Entry(root)
state_entry.grid(row=1, column=1)

tk.Label(root, text="Zip:").grid(row=2, column=0)
zip_entry = tk.Entry(root)
zip_entry.grid(row=2, column=1)


# Button to fetch and display the weather
weather_button = tk.Button(root, text="Get Weather", command=get_weather)
weather_button.grid(row=3, column=0, columnspan=10)

# Labels to display the weather and forecast
current_weather_label = tk.Label(root, textvariable=current_weather_var)
current_weather_label.grid(row=4, column=0, columnspan=10)

forecast_label = tk.Label(root, textvariable=forecast_var)
forecast_label.grid(row=5, column=0, columnspan=10)

local_city_label = tk.Label(root, textvariable=local_city_var)
local_city_label.grid(row=6, column=0, columnspan=10)

local_weather_label=tk.Label(root, textvariable=local_weather_var)
local_weather_label.grid(row=7, column=0, columnspan=10)

ip_address = get_public_ip()
local_city, local_state = get_city_and_state_by_ip(ip_address)
local_city_var.set(f'Current Weather in\n{local_city}, {local_state}:')
local_weather = get_local_weather(local_city, local_state)

local_weather_var.set(local_weather)

# Running the app
root.mainloop()
