from ingest.ingestion_weather import run_ingestion
from db.run_sql import run_sql_files
import time

SQL_PIPELINE = [
    "sql/staging/insert_staging.sql",
    "sql/mart/insert_dim_location.sql",
    "sql/mart/insert_dim_time.sql",
    "sql/mart/insert_fact_weather.sql",
]

def run_pipeline():
    # 1) ingestion RAW
    run_ingestion()

    # 2) trasformazioni SQL (staging + mart)
    run_sql_files(SQL_PIPELINE)

    print("Pipeline completa eseguita con successo")

def backfill(runs: int = 1, sleep_sec: float = 1.0):
    for i in range(runs):
        run_pipeline()
        time.sleep(sleep_sec)

#if __name__ == "__main__":
#    run_pipeline()

if __name__ == "__main__":
    backfill(runs=1, sleep_sec=1.0)