-- models/core/dim_fhv_trips.sql

{{ config(materialized='table') }}

WITH fhv_data AS (
    SELECT * FROM {{ ref('stg_fhv_tripdata_2019') }}
),
dim_zones AS (
    SELECT * FROM {{ ref('dim_zones') }}
)
SELECT
    fhv_data.trip_id,
    fhv_data.dispatching_base_num,
    fhv_data.pickup_datetime,
    fhv_data.dropoff_datetime,
    TIMESTAMP_DIFF(fhv_data.dropoff_datetime, fhv_data.pickup_datetime, SECOND) AS trip_duration,
    fhv_data.pickup_location_id,
    pickup_zone.zone AS pickup_zone,
    fhv_data.dropoff_location_id,
    dropoff_zone.zone AS dropoff_zone,
    EXTRACT(YEAR FROM fhv_data.pickup_datetime) AS year,
    EXTRACT(MONTH FROM fhv_data.pickup_datetime) AS month
FROM
    fhv_data
LEFT JOIN
    dim_zones AS pickup_zone ON fhv_data.pickup_location_id = pickup_zone.location_id
LEFT JOIN
    dim_zones AS dropoff_zone ON fhv_data.dropoff_location_id = dropoff_zone.location_id