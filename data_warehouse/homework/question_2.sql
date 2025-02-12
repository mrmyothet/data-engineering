CREATE OR REPLACE TABLE `ny-rides-mt.ny_taxi.regular_yellow_tripdata`
AS SELECT * FROM `ny-rides-mt.ny_taxi.external_yellow_tripdata`;

SELECT DISTINCT(PULocationID, DOLocationID) FROM `ny-rides-mt.ny_taxi.regular_yellow_tripdata`;

SELECT DISTINCT(PULocationID) FROM `ny-rides-mt.ny_taxi.external_yellow_tripdata`;