-- Partition by tpep_dropoff_datetime and Cluster on VendorID

CREATE OR REPLACE TABLE `ny-rides-mt.ny_taxi.partition_yellow_tripdata`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS (
  SELECT * FROM `ny-rides-mt.ny_taxi.regular_yellow_tripdata`
);