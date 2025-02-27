WITH filtered_data AS (
  SELECT
    pickup_zone,
    dropoff_zone,
    p90_trip_duration,
    ROW_NUMBER() OVER(PARTITION BY pickup_zone ORDER BY p90_trip_duration DESC) AS rn
  FROM
    {{ ref('fct_fhv_monthly_zone_traveltime_p90') }}
  WHERE
    year = 2019
    AND month = 11
    AND pickup_zone IN ('Newark Airport', 'SoHo', 'Yorkville East')
)
SELECT
  pickup_zone,
  dropoff_zone,
  p90_trip_duration
FROM
  filtered_data
WHERE
  rn = 2
ORDER BY
  pickup_zone;