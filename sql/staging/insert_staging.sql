INSERT INTO staging.weather_current (
    ingestion_timestamp,
    source,
    city,
    country,
    observation_time,
    temperatura_c,
    wind_kph,
    humidity,
    condition,
    raw_id
)
SELECT
    r.ingestion_timestamp,
    r.source,

    -- città
    r.data ->> 'name',

    -- paese
    r.data -> 'sys' ->> 'country',

    -- timestamp UNIX → TIMESTAMP
    to_timestamp((r.data ->> 'dt')::BIGINT),

    -- temperatura
    (r.data -> 'main' ->> 'temp')::NUMERIC,

    -- vento (m/s → km/h)
    (r.data -> 'wind' ->> 'speed')::NUMERIC * 3.6,

    -- umidità
    (r.data -> 'main' ->> 'humidity')::INTEGER,

    -- condizione
    r.data -> 'weather' -> 0 ->> 'description',

    r.id

FROM raw.weather_api_data r
ON CONFLICT (raw_id) DO NOTHING;