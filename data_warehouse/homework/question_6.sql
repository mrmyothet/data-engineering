-- Regular Table 
SELECT DISTINCT VendorID
FROM `ny-rides-mt.ny_taxi.regular_yellow_tripdata`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';
--This query will process 310.24 MB when run.

-- Partitioned Table 
SELECT DISTINCT VendorID
FROM `ny-rides-mt.ny_taxi.regular_yellow_tripdata`
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';
--This query will process 26.84 MB when run.
