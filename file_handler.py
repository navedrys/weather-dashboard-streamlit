import json
import os
from datetime import datetime
import pandas as pd

HISTORY_FILE = "history.json"


def load_history():
    """
    Load weather search history.
    """

    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []


def save_history(weather_data):
    """
    Save a new weather record.
    """

    history = load_history()

    weather_data["searched_at"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    history.append(weather_data)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def history_dataframe():

    history = load_history()

    if not history:
        return pd.DataFrame()

    return pd.DataFrame(history)