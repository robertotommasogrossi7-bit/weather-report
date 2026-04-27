import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def _get_host():
    # Prova a ottenere l'IP di Windows da WSL
    try:
        result = subprocess.run(
            ["ip", "route", "show"],
            capture_output=True, text=True
        )
        for line in result.stdout.splitlines():
            if "default" in line:
                return line.split()[2]
    except Exception:
        pass
    # Se non funziona (siamo su Windows), usa DB_HOST dal .env
    return os.getenv("DB_HOST", "localhost")

DB_CONFIG = {
    "host": _get_host(),
    "port": int(os.getenv("DB_PORT")),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}


WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
URL = os.getenv("URL")
CITIES = [

    # --- ITALIA (30) ---
    {"name": "Roma", "lat": 41.9028, "lon": 12.4964},
    {"name": "Milano", "lat": 45.4642, "lon": 9.1900},
    {"name": "Napoli", "lat": 40.8518, "lon": 14.2681},
    {"name": "Torino", "lat": 45.0703, "lon": 7.6869},
    {"name": "Palermo", "lat": 38.1157, "lon": 13.3615},
    {"name": "Genova", "lat": 44.4056, "lon": 8.9463},
    {"name": "Bologna", "lat": 44.4949, "lon": 11.3426},
    {"name": "Firenze", "lat": 43.7696, "lon": 11.2558},
    {"name": "Bari", "lat": 41.1171, "lon": 16.8719},
    {"name": "Catania", "lat": 37.5079, "lon": 15.0830},
    {"name": "Venezia", "lat": 45.4408, "lon": 12.3155},
    {"name": "Verona", "lat": 45.4384, "lon": 10.9916},
    {"name": "Messina", "lat": 38.1938, "lon": 15.5540},
    {"name": "Padova", "lat": 45.4064, "lon": 11.8768},
    {"name": "Trieste", "lat": 45.6495, "lon": 13.7768},
    {"name": "Taranto", "lat": 40.4644, "lon": 17.2470},
    {"name": "Brescia", "lat": 45.5416, "lon": 10.2118},
    {"name": "Prato", "lat": 43.8777, "lon": 11.1022},
    {"name": "Reggio Calabria", "lat": 38.1140, "lon": 15.6500},
    {"name": "Modena", "lat": 44.6471, "lon": 10.9252},
    {"name": "Parma", "lat": 44.8015, "lon": 10.3279},
    {"name": "Reggio Emilia", "lat": 44.6983, "lon": 10.6313},
    {"name": "Perugia", "lat": 43.1107, "lon": 12.3908},
    {"name": "Livorno", "lat": 43.5485, "lon": 10.3106},
    {"name": "Ravenna", "lat": 44.4184, "lon": 12.2035},
    {"name": "Cagliari", "lat": 39.2238, "lon": 9.1217},
    {"name": "Foggia", "lat": 41.4622, "lon": 15.5446},
    {"name": "Salerno", "lat": 40.6824, "lon": 14.7681},
    {"name": "Sassari", "lat": 40.7259, "lon": 8.5557},
    {"name": "Latina", "lat": 41.4676, "lon": 12.9037},

    # --- CAPITALI (10) ---
    {"name": "Paris", "lat": 48.8566, "lon": 2.3522},
    {"name": "London", "lat": 51.5074, "lon": -0.1278},
    {"name": "Berlin", "lat": 52.5200, "lon": 13.4050},
    {"name": "Madrid", "lat": 40.4168, "lon": -3.7038},
    {"name": "New York", "lat": 40.7128, "lon": -74.0060},
    {"name": "Tokyo", "lat": 35.6895, "lon": 139.6917},
    {"name": "Moscow", "lat": 55.7558, "lon": 37.6173},
    {"name": "Beijing", "lat": 39.9042, "lon": 116.4074},
    {"name": "Ottawa", "lat": 45.4215, "lon": -75.6972},
    {"name": "Canberra", "lat": -35.2809, "lon": 149.1300},
]

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")