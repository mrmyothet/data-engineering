-- models/fct_fhv_monthly_zone_traveltime_p90.sql

{{ config(materialized='table') }}

WITH trip_data AS (
    SELECT * FROM {{ ref('dim_fhv_trips') }}
)
SELECT
    year,
    month,
    pickup_location_id,
    pickup_zone,
    dropoff_location_id,
    dropoff_zone,
    APPROX_QUANTILES(trip_duration, 100)[OFFSET(90)] AS p90_trip_duration
FROM
    trip_data
GROUP BY
    year,
    month,
    pickup_location_id,
    pickup_zone,
    dropoff_location_id,
    dropoff_zone