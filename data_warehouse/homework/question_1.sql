CREATE OR REPLACE EXTERNAL TABLE `ny-rides-mt.ny_taxi.external_yellow_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://ny_taxi_data_mt/yellow_tripdata_2024-*.parquet']
);

SELECT COUNT(*) FROM `ny-rides-mt.ny_taxi.external_yellow_tripdata`