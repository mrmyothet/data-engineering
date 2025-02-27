-- models/staging/stg_fhv_tripdata_2019.sql

SELECT
    *,
    ROW_NUMBER() OVER(ORDER BY pickup_datetime) AS trip_id  -- Add a trip_id for easier referencing
FROM
    `bigquery-public-data.new_york_taxi_trips.fhv_tripdata_2019`
WHERE
    dispatching_base_num IS NOT NULL