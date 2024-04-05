import tkinter as tk
from tkinter import ttk
# Function to simulate fetching weather data
def fetch_weather_data(city, state, zip_code):
    # Here, you would fetch data from a weather API based on the inputs
    # For demonstration, we'll just return a mock response
    current_weather = "Sunny, 75°F"
    forecast = [
        "Tomorrow: Rainy, 65°F",
        "Day after: Cloudy, 70°F",
        "3 days out: Sunny, 77°F",
        "4 days out: Thunderstorms, 72°F",
        "5 days out: Partly Cloudy, 75°F"
    ]
    return current_weather, forecast

# Function called when the 'Get Weather' button is pressed
def get_weather():
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_entry.get()
    
    current_weather, forecast = fetch_weather_data(city, state, zip_code)
    
    current_weather_var.set(f"Current Weather: {current_weather}")
    forecast_var.set("\n".join(forecast))

# Creating the main window
root = tk.Tk()
root.title("Weather App")

# Creating StringVars to hold input and output values
current_weather_var = tk.StringVar()
forecast_var = tk.StringVar()

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
weather_button.grid(row=3, column=0, columnspan=2)

# Labels to display the weather and forecast
current_weather_label = tk.Label(root, textvariable=current_weather_var)
current_weather_label.grid(row=4, column=0, columnspan=2)

forecast_label = tk.Label(root, textvariable=forecast_var)
forecast_label.grid(row=5, column=0, columnspan=2)

# Running the app
root.mainloop()
