import tkinter as tk
from tkinter import ttk, Label
from get_lat_lon_by_loc import get_lat_long_by_zip, get_lat_long_by_city_state
from get_current_wx import get_current_wx_by_lat_long
from get_weather_forecast import get_wx_forecast
from get_location_info_by_ip import get_public_ip, get_city_and_state_by_ip
from PIL import Image, ImageTk
from PlaceholderEntry import PlaceholderEntry

#TODO:move windows, add display?, add forecast?, add reverse geocoding


def get_local_weather(city, state):
     lat, long = get_lat_long_by_city_state(city, state)
     current_weather_dict = get_current_wx_by_lat_long(lat, long)
     current_weather = f"{current_weather_dict['description'].capitalize()}, {current_weather_dict['temp']}°F"
     return current_weather
     

def get_current_weather():
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_entry.get()

    
    if zip_code is not None and zip_code != "" and zip_code != "Enter ZIP":
         print(f'zip: {zip_code}')
         lat, long = get_lat_long_by_zip(zip_code)
         local_city_var.set(f"ZIP Code: {zip_code}")
    elif state not in (None, "") and city not in (None, ""):
         local_city_var.set(f'{city}, {state}') #sets local city, 
         lat, long = get_lat_long_by_city_state(city, state)
    else:
         current_weather_var.set(f"Please enter a city and state, or a ZIP code.")   

    current_weather_dict = get_current_wx_by_lat_long(lat, long)

    description_var.set(current_weather_dict['description'].capitalize())

    #Description Lable at top
    current_weather = f"{current_weather_dict['description'].capitalize()}, {current_weather_dict['temp']}°F"
    unit = "°F"

    #Temp Digits
    temperature_list = list(str(round(float(current_weather_dict['temp']))))
    left_digit_var.set(temperature_list[0])
    right_digit_var.set(temperature_list[1])
    unit_digit_var.set(unit)


def get_forecast():
     city = city_entry.get()
     print(f'City: {city}')
     state = state_entry.get()

     zip_code = zip_entry.get()

     if zip_code is not None and zip_code != "":
         lat, long = get_lat_long_by_zip(zip_code)
     elif state not in (None, "") and city not in (None, ""):
         local_city_var.set(f'{city}, {state}') #sets local city, 
         lat, long = get_lat_long_by_city_state(city, state)
     else:
         current_weather_var.set(f"Please enter a city and state, or a ZIP code.")

     forecast_weather = f'NOT IMPLEMENTED: {get_wx_forecast(lat, long)}'    
     forecast_var.set(forecast_weather)


# Creating the main window
root = tk.Tk()
root.geometry("800x1200")
root.title("Weather App")
image = Image.open('TempFolder/slotmachine.jpg')
photo = ImageTk.PhotoImage(image)

background_label = Label(root, image=photo)
background_label.place(relwidth=1, relheight=1)

# Creating StringVars to hold input and output values
current_weather_var = tk.StringVar()
forecast_var = tk.StringVar()
local_city_var = tk.StringVar()
local_weather_var=tk.StringVar()
description_var=tk.StringVar()
right_digit_var = tk.StringVar()
left_digit_var = tk.StringVar()
unit_digit_var = tk.StringVar()

# City Input Field
city_entry = PlaceholderEntry(root, placeholder="Enter City")
city_entry.place(relx=0.37, rely=0.70, anchor='center')

# State Input Field
state_entry = PlaceholderEntry(root, placeholder="Enter State")
state_entry.place(relx=0.37, rely=0.73, anchor='center')

#ZIP Input Field
zip_entry = PlaceholderEntry(root, placeholder="Enter ZIP")
zip_entry.place(relx=0.37, rely=0.76, anchor='center')


# Button to fetch and display the weather
get_current_weather_button = tk.Button(root, text="Current Wx", command=get_current_weather)
get_current_weather_button.place(relx=0.68, rely=0.72, anchor='center')

get_forecast_button = tk.Button(root, text="Forecast Wx", command=get_forecast)
get_forecast_button.place(relx=0.68, rely=0.75, anchor='center')

#Label for top description
description_label = tk.Label(root, textvariable=description_var, font=("Arial", 30, "bold"), foreground="white")
description_label.place(relx=0.5, rely=0.325, anchor='center')

#Lable for temp digits
left_digit_label = tk.Label(root, textvariable=left_digit_var, font=("Arial", 100, "bold"), foreground="white")
left_digit_label.place(relx=0.35, rely=0.5, anchor='center')

right_digit_label = tk.Label(root, textvariable=right_digit_var, font=("Arial", 100, "bold"), foreground="white")
right_digit_label.place(relx=0.5, rely=0.5, anchor='center')

unit_digit_label = tk.Label(root, textvariable=unit_digit_var, font=("Arial", 100, "bold"), foreground="white")
unit_digit_label.place(relx=0.63, rely=0.5, anchor='center')

# forecast_label = tk.Label(root, textvariable=forecast_var)
# forecast_label.grid(row=6, column=0, columnspan=10)

# local_city_label = tk.Label(root, textvariable=local_city_var)
# local_city_label.grid(row=7, column=0, columnspan=10)

local_weather_label=tk.Label(root, textvariable=local_weather_var)
local_weather_label.grid(row=8, column=0, columnspan=10)

center_city_label = tk.Label(root, textvariable=local_city_var, font=("Arial", 40, "bold"), foreground="white") 
center_city_label.place(relx=0.5, rely=0.94, anchor='center')


ip_address = get_public_ip()
local_city, local_state = get_city_and_state_by_ip(ip_address)
local_city_var.set(f'{local_city}, {local_state}')
local_weather = get_local_weather(local_city, local_state)

local_weather_var.set(f'Your wx by IP location ({local_city}):\n{local_weather}')

# Running the app
root.mainloop()
