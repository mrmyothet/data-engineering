```bash

docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="root" \
 -e POSTGRES_DB="ny_taxi" \
 -v /Users/macos/repos/data-engineering/week_1_basics_n_setup/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgres/data \
 -p 5432:5432 \
 postgres:13

```

```bash

docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="root" \
 -e POSTGRES_DB="ny_taxi" \
 -v /home/myothet/repos/data-engineering/week_1_basics_n_setup/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgres/data \
 -p 5434:5434 \
 postgres:13

```

```bash
# On Windows 

docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="root" \
 -e POSTGRES_DB="ny_taxi" \
 -v C:/myothet/data-engineering/week_1_basics_n_setup/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgres/data \
 -p 5432:5432 \
 postgres:13

```


```bash

pgcli -h localhost -p 5432 -u root -d ny_taxi
pgcli -h 192.168.1.106 -p 5434 -u root -d ny_taxi


```
