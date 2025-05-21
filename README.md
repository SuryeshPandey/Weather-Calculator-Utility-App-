# Weather & Calculator Utility App 🌤️➗

## 📌 Project Overview

This Python-based desktop application provides two utilities:
- **Real-Time Weather App** (GUI using Tkinter)
- **Calculator** (Console-based)

You can:
- Fetch current temperature, humidity, and wind conditions by city or coordinates
- Perform basic arithmetic operations (add, subtract, multiply, divide) with error handling
- Maintain logs of all user operations for record-keeping

---

## 📂 Folder Structure

    WEATHER-APPLICATION-MAIN/
    ├── main.py # Console entry point to switch between modes
    ├── calculator.py # CLI calculator with validation and logging
    ├── weather_gui.py # Weather GUI app using OpenWeatherMap API
    ├── logger.py # Logger module (logs activity to activity_log.txt)
    ├── activity_log.txt # Auto-generated log file
    ├── requirements.txt # Required libraries
    ├── README.md # Documentation
    └── images/ # Weather backgrounds (sunny.png, rainy.png, etc.)


---

## 🌐 Weather App Features

- Fetch live weather using **OpenWeatherMap API**
- Input city name (`London`) or coordinates (`28.61,77.23`)
- Shows:
  - Temperature (°C)
  - Humidity (%)
  - Wind direction
- Weather icon + dynamic background
- Errors handled (e.g., city not found)
- All requests logged

---

## ➕ Calculator Features

- CLI-based input
- Supports: `+`, `-`, `*`, `/`, `()`, decimals
- Validates expressions using regex
- Handles errors:
  - Invalid input
  - Divide by zero
  - Incomplete expressions
- Logs every calculation and error

---

## 🧾 Log File Example (`activity_log.txt`)

    2025-05-22 14:07:23 - Weather Request: Delhi -> 32.1 deg, 48%
    2025-05-22 14:08:10 - Calculation: 5 + 3 = 8
    2025-05-22 14:08:35 - Calculation error (divide by zero): 10 / 0


---

## 🛠️ Technologies Used

- Python 3.8+
- Tkinter + ttkbootstrap (GUI)
- Pillow (image handling)
- requests (API integration)
- logging (event tracking)

---
## 🙌 Author

Internship Project by **[Suryesh Pandey]**  
Guided by **Vertunexa Technologies**

---

## 🚀 How to Run

1. **Install requirements:**

```bash
pip install -r requirements.txt
```

2. **Launch the app:**

```bash

python main.py

```
---

### Choose mode when prompted:

- 1 → Weather Info (GUI)
- 2 → Calculator (Console)
