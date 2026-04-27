SELECT
    t.year,
    t.month,
    AVG(f.temperatura_c) AS avg_temp
FROM mart.fact_weather f  
JOIN mart.dim_time t ON f.time_id = t.time_id
GROUP BY t.year, t.month
ORDER BY t.year, t.month;