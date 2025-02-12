CREATE OR REPLACE TABLE `ny-rides-mt.ny_taxi.regular_yellow_tripdata`
AS SELECT * FROM `ny-rides-mt.ny_taxi.external_yellow_tripdata`;

SELECT DISTINCT(PULocationID) FROM `ny-rides-mt.ny_taxi.regular_yellow_tripdata`;
--This query will process 155.12 MB when run.


SELECT DISTINCT(PULocationID) FROM `ny-rides-mt.ny_taxi.external_yellow_tripdata`;
--This query will process 0 B when run.
