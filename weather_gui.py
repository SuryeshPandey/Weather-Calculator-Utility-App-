# weather_gui.py

import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as ttkb
import xml.etree.ElementTree as ET
from logger import log_event

# 🌐 Fetch weather from OpenWeatherMap API
def fetch_weather(location):
    API_KEY = "05f4ee67848cc2f2685db6e4c1cf5f3e"

    if "," in location:
        try:
            lat, lon = map(str.strip, location.split(","))
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&mode=xml&appid={API_KEY}"
        except:
            messagebox.showerror("Invalid Format", "Please use format: latitude,longitude")
            return None
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&mode=xml&appid={API_KEY}"

    response = requests.get(url)

    if response.status_code == 404:
        messagebox.showerror("Error", "City not found or invalid coordinates!")
        return None

    try:
        xml_root = ET.fromstring(response.content)

        return {
            "city": xml_root.find("city").get("name"),
            "country": xml_root.find("city/country").text,
            "temp": float(xml_root.find("temperature").get("value")) - 273.15,
            "feels": float(xml_root.find("feels_like").get("value")) - 273.15,
            "humidity": xml_root.find("humidity").get("value"),
            "pressure": xml_root.find("pressure").get("value"),
            "wind": xml_root.find("wind/direction").get("name"),
            "desc": xml_root.find("weather").get("value"),
            "icon_url": f"https://openweathermap.org/img/wn/{xml_root.find('weather').get('icon')}@2x.png"
        }
    except Exception as e:
        messagebox.showerror("Error", f"Data could not be parsed: {e}")
        return None

# 🎨 Set background image based on weather
def update_background(desc, root, background_label):
    themes = {
        "clear sky": "images/sunny.png",
        "rain": "images/rainy.png",
        "clouds": "images/cloudy.png",
        "mist": "images/mist.png",
        "haze": "images/haze.png"
    }
    bg_file = themes.get(desc.lower(), "images/default.png")
    img = Image.open(bg_file).resize((root.winfo_width(), root.winfo_height()), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(img)
    background_label.configure(image=bg_photo)
    background_label.image = bg_photo

# 🚀 Launch the GUI
def launch_weather_gui():
    root = ttkb.Window(themename="journal")
    root.title("Weather Forecast App 🌍")
    root.geometry("420x780")
    root.resizable(False, False)

    background_label = tk.Label(root)
    background_label.place(relwidth=1, relheight=1)

    # Set default background
    default_img = Image.open("images/default.png").resize((420, 780), Image.LANCZOS)
    default_photo = ImageTk.PhotoImage(default_img)
    background_label.configure(image=default_photo)
    background_label.image = default_photo

    # Input Field
    entry = ttkb.Entry(root, font="Helvetica 16")
    entry.insert(0, "Enter City or lat,lon")
    entry.bind("<FocusIn>", lambda e: entry.delete(0, tk.END))
    entry.pack(pady=12)

    # Labels setup
    label_style = {'font': "Helvetica 16", 'bg': root.cget("bg"), 'fg': 'black'}
    location_label = tk.Label(root, **label_style)
    icon_label = tk.Label(root, **label_style)
    temperature_label = tk.Label(root, **label_style)
    feels_label = tk.Label(root, **label_style)
    desc_label = tk.Label(root, **label_style)
    humidity_label = tk.Label(root, **label_style)
    pressure_label = tk.Label(root, **label_style)
    wind_label = tk.Label(root, **label_style)

    weather_widgets = [
        location_label, icon_label, temperature_label, feels_label,
        desc_label, humidity_label, pressure_label, wind_label
    ]

    for w in weather_widgets:
        w.pack_forget()

    # 🔍 Search handler
    def search_weather():
        user_input = entry.get()
        result = fetch_weather(user_input)
        if result is None:
            return

        update_background(result['desc'], root, background_label)

        try:
            icon_img = Image.open(requests.get(result["icon_url"], stream=True).raw)
            weather_icon = ImageTk.PhotoImage(icon_img)
            icon_label.configure(image=weather_icon)
            icon_label.image = weather_icon
        except:
            icon_label.configure(image='')

        location_label.configure(text=f"{result['city']}, {result['country']}")
        temperature_label.configure(text=f"Temperature: {result['temp']:.1f}°C")
        feels_label.configure(text=f"Feels Like: {result['feels']:.1f}°C")
        desc_label.configure(text=f"Condition: {result['desc']}")
        humidity_label.configure(text=f"Humidity: {result['humidity']}%")
        pressure_label.configure(text=f"Pressure: {result['pressure']} hPa")
        wind_label.configure(text=f"Wind Direction: {result['wind']}")

        log_event(f"Weather Request: {user_input} → {result['temp']:.1f}°C, {result['humidity']}%")

        for widget in weather_widgets:
            widget.pack()

    search_button = ttkb.Button(root, text="Get Weather 🌦️", command=search_weather, bootstyle="primary")
    search_button.pack(pady=10)

    root.mainloop()
