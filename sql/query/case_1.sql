SELECT 
    t.date,
    l.city,
    AVG(f.temperatura_c) AS avg_time,
    AVG(f.wind_kph) AS avg_wind
FROM mart.fact_weather f 
JOIN mart.dim_time t ON f.time_id = t.time_id
JOIN mart.dim_location l ON f.location_id = l.location_id
GROUP BY t.date, l.city
ORDER BY t.date DESC;