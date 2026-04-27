INSERT INTO mart.dim_location (city, country)
SELECT DISTINCT city, country
FROM staging.weather_current
WHERE city IS NOT NULL
ON CONFLICT (city, country) DO NOTHING;