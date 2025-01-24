### Question 1

```bash

docker run -it python:3.12.8 bash
pip --version

pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)

```

### Question 2

- service name in docker-compose file is the host name of the database. - db
- 5433:5432 means 5433 on host computer, 5432 on docker container. - 5432

### Question 3

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

```

```sql
SELECT COUNT(1)
FROM green_tripdata_2019_10
WHERE lpep_pickup_datetime >= DATE '2019-10-01 00:00:00'
  AND lpep_pickup_datetime < DATE '2019-11-01 00:00:00'
  AND trip_distance <= 1;
```

```sql
SELECT COUNT(1)
FROM green_tripdata_2019_10
WHERE lpep_pickup_datetime >= DATE '2019-10-01 00:00:00'
  AND lpep_pickup_datetime < DATE '2019-11-01 00:00:00'
  AND trip_distance <= 1;
```
