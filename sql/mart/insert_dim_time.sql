INSERT INTO mart.dim_time (full_timestamp, date, year, month, day, hour)
SELECT DISTINCT 
    observation_time,
    observation_time::DATE,
    EXTRACT(YEAR FROM observation_time),
    EXTRACT(MONTH FROM observation_time),
    EXTRACT(DAY FROM observation_time),
    EXTRACT(HOUR FROM observation_time)
FROM staging.weather_current
WHERE observation_time IS NOT NULL
ON CONFLICT (full_timestamp) DO NOTHING;