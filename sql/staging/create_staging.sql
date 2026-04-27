CREATE SCHEMA IF NOT EXISTS staging;

CREATE TABLE IF NOT EXISTS staging.weather_current(
    id SERIAL PRIMARY KEY,

    -- metadata
    ingestion_timestamp TIMESTAMP NOT NULL,
    source VARCHAR(50) NOT NULL,

    -- dimensioni logiche
    city VARCHAR(100),
    country VARCHAR(100),

    -- tempo evento (non ingestion)
    observation_time TIMESTAMP,

    -- misure 
    temperatura_c NUMERIC,
    wind_kph NUMERIC,
    humidity INTEGER,
    condition TEXT,

    -- controllo qualità
    raw_id INTEGER UNIQUE
);