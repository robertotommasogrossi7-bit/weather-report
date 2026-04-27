from openai import OpenAI
from db.connection import get_connection
from config.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

# Descrizione del tuo schema — questo è il "contesto" che dai alla LLM
SCHEMA = """
Hai accesso a un database PostgreSQL con questo schema:

mart.dim_location (location_id, city, country)
mart.dim_time (time_id, full_timestamp, date, year, month, day, hour)
mart.fact_weather (fact_id, location_id, time_id, temperatura_c, wind_kph, humidity, raw_id)

Per fare query complete unisci sempre fact_weather con dim_location e dim_time.
Esempio join: 
  FROM mart.fact_weather f
  JOIN mart.dim_location l ON f.location_id = l.location_id
  JOIN mart.dim_time t ON f.time_id = t.time_id

Quando una domanda riguarda la temperatura più alta o più bassa senza specificare un orario,
usa una finestra temporale delle ultime 2 ore rispetto al MAX(full_timestamp) presente nel database,
in modo da includere tutte le città anche se hanno timestamp leggermente diversi.
Esempio: WHERE t.full_timestamp >= (SELECT MAX(full_timestamp) FROM mart.dim_time) - INTERVAL '2 hours'
Se ti faccio una domanda su un orario specifico, cerca il timestamp più vicino a quello richiesto.

Rispondi SOLO con la query SQL, senza spiegazioni, senza markdown, senza backtick.
"""
def format_text(righe):
    if not righe:
        return "Nessun risultato."

    r = righe[0]

    if "temperatura_c" in r:
        return f"La città più calda è {r['city']} con {r['temperatura_c']}°C."

    if "wind_kph" in r:
        return f"La città con il vento più forte è {r['city']} con {r['wind_kph']} km/h."

    return "Risultato trovato."


def ask(domanda: str) -> str:
    # 1) Chiedi a OpenAI di generare la SQL
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": SCHEMA},
            {"role": "user", "content": domanda}
        ]
    )

    sql = response.output_text.strip()

    print("SQL:", sql)

    if not sql.strip().lower().startswith("select"):
        return "Query non consentita"
    print(f"\nSQL generata:\n{sql}\n")
    
    # 2) Esegui la query sul tuo PostgreSQL
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(sql)
        risultati = cursor.fetchall()
        colonne = [desc[0] for desc in cursor.description]
    except Exception as e:
        return f"Errore nell'esecuzione della query: {e}"
    finally:
        cursor.close()
        conn.close()
    
    # 3) Formatta la risposta
    if not risultati:
        return "Nessun risultato trovato."
    
    righe = [dict(zip(colonne, riga)) for riga in risultati]

    summary = format_text(righe)

    return {
        "summary": summary,
        "data": righe
    }

if __name__ == "__main__":
    while True:
        domanda = input("Fai una domanda sul meteo: ")
        if domanda.lower() in ["exit", "quit"]:
            break
        risposta = ask(domanda)
        print("Risposta:", risposta)