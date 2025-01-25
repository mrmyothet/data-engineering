### Question 1. Understanding docker first run

```bash

docker run -it python:3.12.8 bash
pip --version

pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)

```

### Question 2. Understanding Docker networking and docker-compose

- service name in docker-compose file is the host name of the database. - db
- 5433:5432 means 5433 on host computer, 5432 on docker container. - 5432

```bash
DtypeWarning: Columns (3) have mixed types. Specify dtype option on import or set low_memory=False.  for batch in df_iter:
```

### Question 3. Trip Segmentation Count

During the period of October 1st 2019 (inclusive) and November 1st 2019 (exclusive), how many trips, respectively, happened:

1. Up to 1 mile
2. In between 1 (exclusive) and 3 miles (inclusive),
3. In between 3 (exclusive) and 7 miles (inclusive),
4. In between 7 (exclusive) and 10 miles (inclusive),
5. Over 10 miles

```bash
brew install wget

wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz
gunzip green_tripdata_2019-10.csv.gz

wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv

curl -kLSs https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz -o green_tripdata_2019-10.csv.gz
curl -kLSs https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv -o taxi_zone_lookup.csv

```

```sql
SELECT COUNT(1)
FROM green_tripdata_2019_10
WHERE lpep_pickup_datetime >= DATE '2019-10-01 00:00:00'
  AND lpep_pickup_datetime < DATE '2019-11-01 00:00:00'
  AND trip_distance <= 1;


SELECT COUNT(1)
FROM green_tripdata_2019_10
WHERE lpep_pickup_datetime >= DATE '2019-10-01'
  AND lpep_pickup_datetime < DATE '2019-11-01'
  AND trip_distance > 1.0
  AND trip_distance <= 3.0;


SELECT COUNT(1)
FROM green_tripdata_2019_10
WHERE lpep_pickup_datetime >= DATE '2019-10-01'
  AND lpep_pickup_datetime < DATE '2019-11-01'
  AND trip_distance > 3.0
  AND trip_distance <= 7.0;


SELECT COUNT(1)
FROM green_tripdata_2019_10
WHERE lpep_pickup_datetime >= DATE '2019-10-01'
  AND lpep_pickup_datetime < DATE '2019-11-01'
  AND trip_distance > 7.0
  AND trip_distance <= 10.0;


SELECT COUNT(1)
FROM green_tripdata_2019_10
WHERE lpep_pickup_datetime >= DATE '2019-10-01'
  AND lpep_pickup_datetime < DATE '2019-11-01'
  AND trip_distance > 10;
```

### Question 4. Longest trip for each day

Which was the pick up day with the longest trip distance? Use the pick up time for your calculations.

Tip: For every day, we only care about one single trip with the longest distance.

- 2019-10-11
- 2019-10-24
- 2019-10-26
- 2019-10-31

```sql
select MAX(trip_distance)
from green_tripdata_2019_10
where lpep_pickup_datetime >= date '2019-10-11'
and lpep_pickup_datetime < date '2019-10-12'
--95.78

select MAX(trip_distance)
from green_tripdata_2019_10
where lpep_pickup_datetime >= date '2019-10-24'
and lpep_pickup_datetime < date '2019-10-25'
--90.75

select MAX(trip_distance)
from green_tripdata_2019_10
where lpep_pickup_datetime >= date '2019-10-26'
and lpep_pickup_datetime < date '2019-10-27'
--91.56

select MAX(trip_distance)
from green_tripdata_2019_10
where lpep_pickup_datetime >= date '2019-10-31'
and lpep_pickup_datetime < date '2019-11-01'
--515.89

```
