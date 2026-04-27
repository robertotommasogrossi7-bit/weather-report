--SELECT COUNT(*) FROM mart.dim_location;
--SELECT COUNT(*) FROM mart.dim_time;

SELECT COUNT(*) FROM mart.fact_weather;
SELECT COUNT(*) FROM raw.weather_api_data;

--SELECT
    --(SELECT COUNT(*) FROM mart.fact_weather) AS fact_rows,
    --(SELECT COUNT(DISTINCT raw_id) FROM staging.weather_current) AS staging_unique;

--SELECT 
--    (SELECT COUNT(*) FROM raw.weather_api_data) AS raw_rows,
--    (SELECT COUNT(*) FROM staging.weather_current) AS staging_rows,
--    (SELECT COUNT(*) FROM mart.fact_weather) AS fact_rows;

--SELECT * FROM mart.fact_weather;

--SELECT table_schema, table_name 
--FROM information_schema.tables 
--WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
--ORDER BY table_schema, table_name;