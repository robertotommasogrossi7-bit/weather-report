import requests
import json
from config.config import WEATHER_API_KEY
from config.config import CITIES
from db.connection import get_connection

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(response.text)

    return response.json()


def run_ingestion():
    conn = get_connection()
    cursor = conn.cursor()

    for city in CITIES:
        data = fetch_weather(city["lat"], city["lon"])

        cursor.execute("""
            INSERT INTO raw.weather_api_data (source, data)
            VALUES (%s, %s)
        """, ("openweathermap", json.dumps(data)))

    conn.commit()
    cursor.close()
    conn.close()

    print("Ingestion multi-city completata")