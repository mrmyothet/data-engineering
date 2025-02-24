-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `ny-rides-mt.trips_data_all.ext_green_taxi`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://ny_taxi_data_mt/green_tripdata_2019-*.parquet', 'gs://ny_taxi_data_mt/green_tripdata_2020-*.parquet']
);

--SELECT COUNT(*) FROM `ny-rides-mt.trips_data_all.ext_green_taxi`; --8035161

-- It does not match with the number of rows described at the homework