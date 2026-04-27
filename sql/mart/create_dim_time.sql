CREATE TABLE IF NOT EXISTS mart.dim_time (
    time_id SERIAL PRIMARY KEY,
    full_timestamp TIMESTAMP UNIQUE,
    date DATE,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER
);