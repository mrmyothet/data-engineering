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

```bash
brew install wget

wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz
gunzip green_tripdata_2019-10.csv.gz

wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv

```
