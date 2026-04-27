CREATE TABLE IF NOT EXISTS mart.fact_weather (
    fact_id SERIAL PRIMARY KEY,
    location_id INTEGER REFERENCES mart.dim_location(location_id),
    time_id INTEGER REFERENCES mart.dim_time(time_id),
    temperatura_c NUMERIC,
    wind_kph NUMERIC,
    humidity INTEGER,
    raw_id INTEGER UNIQUE
);