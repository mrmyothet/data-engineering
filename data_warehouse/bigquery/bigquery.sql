SELECT station_id, name
FROM bigquery-public-data.new_york_citibike.citibike_stations
LIMIT 100;


CREATE OR REPLACE EXTERNAL TABLE `ny-rides-mt.ny_taxi.external_yellow_tripdata`
OPTIONS(
  format = 'parquet',
  uris = ['gs://ny_taxi_data_mt/yellow_tripdata_2019-*.parquet', 'gs://ny_taxi_data_mt/yellow_tripdata_2020-*.parquet']
);

SELECT * FROM `ny-rides-mt.ny_taxi.external_yellow_tripdata` limit 10;