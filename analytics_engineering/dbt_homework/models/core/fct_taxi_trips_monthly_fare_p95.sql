{{ config(materialized='table') }}

WITH valid_trips AS (
    SELECT
        *,
        CASE
            WHEN vendor_id = 1 THEN 'Yellow Taxi'
            WHEN vendor_id = 2 THEN 'Green Taxi'
            ELSE NULL  -- or some other appropriate handling for unexpected vendor_ids
        END AS service_type
    FROM
        {{ ref('stg_taxi_trips') }}
    WHERE fare_amount > 0
    AND trip_distance > 0
    AND payment_type_description IN ('Cash', 'Credit Card')
),

trip_percentiles AS (
    SELECT
        service_type,
        EXTRACT(YEAR FROM pickup_datetime) AS pickup_year,
        EXTRACT(MONTH FROM pickup_datetime) AS pickup_month,
        fare_amount,
        PERCENT_RANK() OVER (PARTITION BY service_type, EXTRACT(YEAR FROM pickup_datetime), EXTRACT(MONTH FROM pickup_datetime) ORDER BY fare_amount) AS fare_percentile
    FROM
        valid_trips
)

SELECT
    service_type,
    pickup_year,
    pickup_month,
    APPROX_PERCENTILE(fare_amount, 0.97) AS p97,
    APPROX_PERCENTILE(fare_amount, 0.95) AS p95,
    APPROX_PERCENTILE(fare_amount, 0.90) AS p90
FROM
    trip_percentiles
WHERE pickup_year = 2020
AND pickup_month = 4
GROUP BY 1,2,3