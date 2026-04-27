INSERT INTO mart.fact_weather (
    location_id,
    time_id,
    temperatura_c,
    wind_kph,
    humidity,
    raw_id
)
SELECT
    dl.location_id,
    dt.time_id,
    s.temperatura_c,
    s.wind_kph,
    s.humidity,
    s.raw_id
FROM staging.weather_current s
JOIN mart.dim_location dl
    ON s.city = dl.city AND s.country = dl.country
JOIN mart.dim_time dt 
    On s.observation_time = dt.full_timestamp
ON CONFLICT (raw_id) DO NOTHING;