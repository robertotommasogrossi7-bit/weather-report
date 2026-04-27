import psycopg2
from psycopg2.extras import RealDictCursor
from config.config import DB_CONFIG

def get_connection():
    """
    Restituisce una connessione PostgreSQL configurata.
    Usa RealDictCursor per avere i risultati come dizionari.
    """
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            database=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        return conn
    except Exception as e:
        print(f"Errore connessione DB: {e}")
        raise
    