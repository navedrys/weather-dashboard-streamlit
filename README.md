# 🌤 Weather Dashboard using Streamlit, REST API & JSON

### Real-Time Weather Monitoring Application using Python, Streamlit & OpenWeather REST API

---

# 👨‍💻 Naved Shaikh

📧 **Email:** navedrys@gmail.com  
📱 **Phone:** +91 7414991107  
🔗 **LinkedIn:** https://linkedin.com/in/naved-shaikh-784776280  
💻 **GitHub:** https://github.com/navedrys

---

> A modern weather dashboard that consumes live weather data from a REST API, parses JSON responses, stores search history locally, and presents real-time weather information through an interactive Streamlit interface.

---

# 📌 Project Overview

Weather applications are one of the most common real-world examples of REST API integration.

This project demonstrates how a Python application communicates with an external REST API, processes JSON data, and displays meaningful information through a user-friendly dashboard.

The application allows users to search weather information for any city worldwide while maintaining a searchable history of previous requests.

---

# 🎯 Project Objectives

This project was built to demonstrate practical backend development skills including:

✨ REST API Integration

✨ JSON Parsing

✨ HTTP GET Requests

✨ Environment Variable Management

✨ File Handling using JSON

✨ Interactive Streamlit Dashboard

✨ Error Handling

✨ Data Persistence

---

# 💼 Business Problem

Many businesses require real-time weather information for planning and operational purposes.

Examples include:

- Logistics & Delivery Services
- Agriculture
- Tourism
- Aviation
- Event Management
- Ride Sharing Applications

Instead of manually checking weather websites, organizations can integrate weather APIs directly into their applications to automate decision making.

This project demonstrates exactly that workflow.

---

# ⚙️ Application Workflow

```text
                     ┌──────────────────────────┐
                     │     User Enters City     │
                     └─────────────┬────────────┘
                                   │
                                   ▼
                     ┌──────────────────────────┐
                     │  Streamlit User Interface │
                     └─────────────┬────────────┘
                                   │
                                   ▼
                     ┌──────────────────────────┐
                     │ Python Requests Library  │
                     │ Sends HTTP GET Request   │
                     └─────────────┬────────────┘
                                   │
                                   ▼
                     ┌──────────────────────────┐
                     │ OpenWeather REST API     │
                     └─────────────┬────────────┘
                                   │
                                   ▼
                     ┌──────────────────────────┐
                     │ JSON Response Received   │
                     └─────────────┬────────────┘
                                   │
                                   ▼
                     ┌──────────────────────────┐
                     │ JSON Parsing (Python)    │
                     └─────────────┬────────────┘
                                   │
                                   ▼
                     ┌──────────────────────────┐
                     │ Weather Information      │
                     │ Displayed in Streamlit   │
                     └─────────────┬────────────┘
                                   │
                                   ▼
                     ┌──────────────────────────┐
                     │ Save Search History      │
                     │ history.json             │
                     └──────────────────────────┘
```

---

# 🚀 Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Backend Programming |
| 🌐 OpenWeather REST API | Live Weather Data |
| 📦 Requests | HTTP API Communication |
| 📄 JSON | API Response & Local Storage |
| 🎨 Streamlit | Interactive Dashboard |
| 🔐 python-dotenv | API Key Management |
| 🐼 Pandas | Search History Table |
| 💻 Git & GitHub | Version Control |

---

# 📂 Project Structure

```bash
📦 weather-dashboard-streamlit
│
├── app.py
├── weather_api.py
├── file_handler.py
├── config.py
├── requirements.txt
├── history.json
├── .env.example
├── README.md
│
├── assets/
│   └── logo.png
│
└── screenshots/
    └── dashboard.png
```

---

# 🌍 REST API Used

### OpenWeather Current Weather API

Example Endpoint

```text
https://api.openweathermap.org/data/2.5/weather?q=Pune&appid=YOUR_API_KEY&units=metric
```

The application sends an HTTP GET request and receives a JSON response containing weather information.

---

# 📦 Example JSON Response

```json
{
  "name": "Pune",
  "main": {
    "temp": 28.5,
    "feels_like": 31.0,
    "humidity": 72
  },
  "weather": [
    {
      "main": "Clouds",
      "description": "broken clouds"
    }
  ],
  "wind": {
    "speed": 4.2
  },
  "sys": {
    "country": "IN"
  }
}
```

---

# 🧠 JSON Parsing

The application extracts only the required fields from the API response:

- City
- Country
- Temperature
- Feels Like
- Humidity
- Weather Condition
- Description
- Wind Speed

The parsed data is displayed on the dashboard and saved locally in `history.json`.


---

# ✨ Application Features

The Weather Dashboard includes the following functionality:

✅ Search weather by city

✅ Real-time weather information

✅ REST API integration

✅ JSON response parsing

✅ Search history stored locally

✅ Download search history as CSV

✅ Error handling for invalid city names

✅ Secure API key management using `.env`

✅ Interactive Streamlit dashboard

---

# 📊 Dashboard Preview

> Add screenshots of your application inside the `screenshots/` folder.

## Home Page

```
🌤 Weather Dashboard

Enter City

[ Pune                    ]

[ Get Weather ]

---------------------------------------

📍 Pune, IN

🌡 Temperature : 29°C

🤗 Feels Like : 31°C

💧 Humidity : 72%

☁ Condition : Clouds

🌬 Wind Speed : 4.5 m/s
```

---

## Search History

| City | Temperature | Condition | Time |
|------|------------|-----------|------|
| Pune | 29°C | Clouds | 04-07-2026 |
| Mumbai | 31°C | Clear | 04-07-2026 |

---

# ⚙️ Installation

## Clone the repository

```bash
git clone https://github.com/navedrys/weather-dashboard-streamlit.git
```

---

## Move into the project directory

```bash
cd weather-dashboard-streamlit
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Create a `.env` file

```env
OPENWEATHER_API_KEY=YOUR_API_KEY
```

---

## Run the application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

# 💾 Search History

Every successful search is automatically stored inside:

```
history.json
```

Example:

```json
[
  {
    "city": "Pune",
    "country": "IN",
    "temperature": 29.2,
    "humidity": 72,
    "condition": "Clouds",
    "wind_speed": 4.5,
    "searched_at": "04-07-2026 10:42:31"
  }
]
```

---

# 🚨 Error Handling

The application handles several common scenarios:

- Invalid city names
- Empty search input
- Internet connection issues
- API request failures
- Missing API key
- Corrupted `history.json` file

---

# 📈 Skills Demonstrated

| Skill | Demonstrated |
|--------|--------------|
| Python Programming | ✅ |
| REST API Integration | ✅ |
| HTTP GET Requests | ✅ |
| JSON Parsing | ✅ |
| Environment Variables | ✅ |
| File Handling | ✅ |
| Exception Handling | ✅ |
| Streamlit Development | ✅ |
| Data Persistence | ✅ |
| Git & GitHub | ✅ |

---

# 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Building Python applications
- Consuming REST APIs
- Working with JSON responses
- Secure API key management
- Reading and writing JSON files
- Creating interactive web applications with Streamlit
- Structuring Python projects
- Version control using Git & GitHub

---

# 🚀 Future Enhancements

Some ideas for future improvements:

- 🌤 5-Day Weather Forecast
- 📍 Detect Current Location
- 🌅 Sunrise & Sunset Times
- 🌎 Interactive Weather Maps
- 🌡 Temperature Trend Charts
- 📊 Weather Analytics Dashboard
- 🌙 Dark / Light Theme Toggle
- ☁ Deploy to Streamlit Community Cloud
- 🐳 Docker Support
- 🔍 Search Suggestions

---

# 📷 Screenshots

Store screenshots inside:

```
screenshots/
```

Example:

```
screenshots/
│
├── home.png
├── weather_result.png
├── history.png
└── dashboard.png
```

---

# 📌 Resume Project Description

**Weather Dashboard using Streamlit, REST API & JSON**

Developed an interactive weather dashboard using Python and Streamlit that consumes live weather data from the OpenWeather REST API. Implemented HTTP GET requests, parsed nested JSON responses, securely managed API keys using environment variables, stored search history in a local JSON file, and provided a user-friendly interface with error handling and downloadable search history.

---

# 🤝 Connect With Me

👨‍💻 **Naved Shaikh**

📧 Email: navedrys@gmail.com

💻 GitHub: https://github.com/navedrys

🔗 LinkedIn: https://linkedin.com/in/naved-shaikh-784776280

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

Your support is greatly appreciated.
