SELECT COUNT(*) 
FROM `ny-rides-mt.ny_taxi.external_yellow_tripdata`
WHERE fare_amount = 0
-- 8333