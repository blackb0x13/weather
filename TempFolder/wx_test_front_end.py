import tkinter as tk
from tkinter import ttk, Label
from get_lat_lon_by_loc import get_lat_long_by_zip, get_lat_long_by_city_state
from get_current_wx import get_current_wx_by_lat_long
from get_weather_forecast import get_wx_forecast
from get_location_info_by_ip import get_public_ip, get_city_and_state_by_ip
from PIL import Image, ImageTk
from PlaceholderEntry import PlaceholderEntry
import requests
from get_pollution import get_current_air_quality

#TODO:move windows, add display?, add forecast?, add reverse geocoding

def get_local_weather(city, state):
     lat, long = get_lat_long_by_city_state(city, state)
     current_weather_dict = get_current_wx_by_lat_long(lat, long)
     current_weather = f"{current_weather_dict['description'].capitalize()}, {current_weather_dict['temp']}°F"
     return current_weather

def open_forecast():
    new_window = tk.Toplevel(root)
    new_window.title("Forecast Sportsbook")
    new_window.geometry("400x800")  # Width x Height

    # Run the function and display its output in the new window
    output = get_forecast()

    for i, string in enumerate(output):
        text_color = "white" if i % 3 == 0 else "green"
        label = tk.Label(new_window, text=string, fg=text_color, bg="black")
        label.pack(anchor='w', fill=tk.X)


def get_pollution():
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_entry.get()
    if zip_code is not None and zip_code != "" and zip_code != "Enter ZIP":
         print(f'zip: {zip_code}')
         lat, long = get_lat_long_by_zip(zip_code)
         local_city_var.set(f"ZIP Code: {zip_code}")
    elif state not in (None, "") and city not in (None, ""):
         local_city_var.set(f'{city}, {state}')
         lat, long = get_lat_long_by_city_state(city, state)
    else:
         current_weather_var.set(f"Please enter a city and state, or a ZIP code.")
    air_quality = get_current_air_quality(lat, long)
    new_window = tk.Toplevel(root)
    new_window.resizable(False, False)
    new_window.title("Smoking Section")
    new_window.geometry("400x600")
    smoker_image = Image.open('TempFolder/slot_smoker.jpg')
    smoker_photo = ImageTk.PhotoImage(smoker_image)
    # background_label = Label(new_window, image=photo)
    # background_label.place(relwidth=1, relheight=1)
    aqi_label = tk.Label(new_window, image=smoker_photo)
    aqi_label.pack()
    #Don't repeat code. Refactor later


def get_current_weather():
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_entry.get()


    if zip_code is not None and zip_code != "" and zip_code != "Enter ZIP":
         print(f'zip: {zip_code}')
         lat, long = get_lat_long_by_zip(zip_code)
         local_city_var.set(f"ZIP Code: {zip_code}")
    elif state not in (None, "") and city not in (None, ""):
         local_city_var.set(f'{city}, {state}')
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
     state = state_entry.get()
     zip_code = zip_entry.get()

     if zip_code is not None and zip_code != "" and zip_code != "Enter ZIP":
         lat, long = get_lat_long_by_zip(zip_code)
     elif state not in (None, "") and city not in (None, ""):
         local_city_var.set(f'{city}, {state}') #sets local city,
         lat, long = get_lat_long_by_city_state(city, state)
     else:
         current_weather_var.set(f"Please enter a city and state, or a ZIP code.")

     forecast_weather = get_wx_forecast(lat, long)
     return forecast_weather


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
local_city_var = tk.StringVar()
local_weather_var=tk.StringVar()
description_var=tk.StringVar()
right_digit_var = tk.StringVar()
left_digit_var = tk.StringVar()
unit_digit_var = tk.StringVar()

# City Input Field
city_entry = PlaceholderEntry(root, placeholder="Enter City",)
city_entry.place(relx=0.37, rely=0.67, anchor='center')

# State Input Field
state_entry = PlaceholderEntry(root, placeholder="Enter State")
state_entry.place(relx=0.37, rely=0.70, anchor='center')

#ZIP Input Field
zip_entry = PlaceholderEntry(root, placeholder="Enter ZIP")
zip_entry.place(relx=0.37, rely=0.73, anchor='center')


# Button to fetch and display the weather
get_current_weather_button = tk.Button(root, text="Current Wx", command=get_current_weather)
get_current_weather_button.place(relx=0.68, rely=0.73, anchor='center')

get_forecast_button = tk.Button(root, text="Forecast Wx", command=open_forecast)
get_forecast_button.place(relx=0.68, rely=0.70, anchor='center')

get_pollution_button = tk.Button(root, text="Air Quality", command=get_pollution)
get_pollution_button.place(relx=0.68, rely=0.67, anchor='center')

# smoker = Image.open('TempFolder/slot_smoker.jpg')
# slot_smoker = ImageTk.PhotoImage(smoker)
# new_label = tk.Label(root, image=slot_smoker)
# new_label.place(relx=0.5, rely=0.2, anchor='center')
#Can put this information into the new window for background and put AQI on top

#Label for top description
description_label = tk.Label(root, textvariable=description_var, font=("Arial", 30, "bold"), background="black", foreground="white")
description_label.place(relx=0.5, rely=0.325, anchor='center')

#Lable for temp digits
left_digit_label = tk.Label(root, textvariable=left_digit_var, font=("Arial", 100, "bold"), background="black", foreground="white")
left_digit_label.place(relx=0.35, rely=0.5, anchor='center')

right_digit_label = tk.Label(root, textvariable=right_digit_var, font=("Arial", 100, "bold"), background="black", foreground="white")
right_digit_label.place(relx=0.5, rely=0.5, anchor='center')

unit_digit_label = tk.Label(root, textvariable=unit_digit_var, font=("Arial", 100, "bold"), background="black", foreground="white")
unit_digit_label.place(relx=0.63, rely=0.5, anchor='center')

local_weather_label=tk.Label(root, textvariable=local_weather_var)
local_weather_label.grid(row=8, column=0, columnspan=10)

center_city_label = tk.Label(root, textvariable=local_city_var, font=("Arial", 40, "bold"), background="black",foreground="white")
center_city_label.place(relx=0.5, rely=0.85, anchor='center')




ip_address = get_public_ip()
local_city, local_state = get_city_and_state_by_ip(ip_address)
local_city_var.set(f'{local_city}, {local_state}')
local_weather = get_local_weather(local_city, local_state)

local_weather_var.set(f'Your wx by IP location ({local_city}):\n{local_weather}')

# Running the app
root.mainloop()
