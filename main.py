from weather import get_weather
from file_handler import save_history
city=input("Enter city: ")
try:
    d=get_weather(city)
    print(f"City: {d['city']}")
    print(f"Temp: {d['temp']}°C")
    print(f"Humidity: {d['humidity']}%")
    print(f"Condition: {d['condition']}")
    print(f"Wind: {d['wind']} m/s")
    save_history(d)
    print("Saved to history.json")
except Exception as e:
    print(e)
