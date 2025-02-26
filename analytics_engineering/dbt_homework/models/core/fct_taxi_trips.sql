SELECT
    *,
    EXTRACT(YEAR FROM pickup_datetime) AS pickup_year,
    EXTRACT(QUARTER FROM pickup_datetime) AS pickup_quarter,
    EXTRACT(YEAR FROM pickup_datetime) || '/' || 'Q' || EXTRACT(QUARTER FROM pickup_datetime) AS pickup_year_quarter,
    EXTRACT(MONTH FROM pickup_datetime) AS pickup_month
FROM
    {{ ref('fact_trips') }} -- Replace 'stg_taxi_trips' with your actual source model