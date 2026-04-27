CREATE SCHEMA IF NOT EXISTS mart;

CREATE TABLE IF NOT EXISTS mart.dim_location (
    location_id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    country VARCHAR(100),
    UNIQUE(city, country)
);
