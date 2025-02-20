CREATE TABLE `ny-rides-mt.trips_data_all.green_tripdata` as 
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2019`;

INSERT INTO `ny-rides-mt.trips_data_all.green_tripdata` 
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2020`;


-- select count(*) from `trips_data_all.green_tripdata`

CREATE TABLE `ny-rides-mt.trips_data_all.yellow_tripdata` as 
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2019`;

INSERT INTO `ny-rides-mt.trips_data_all.yellow_tripdata` 
SELECT * FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2020`;