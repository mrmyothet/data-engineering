### Running Docker

```bash
docker run hello-world

docker run -it ubuntu bash

docker run -it python:3.9
```

```bash

docker run -it --entrypoint=bash python:3.9
pip install pandas
python
import pandas
pandas.__version__

```

### Build Dockerfile

```bash

docker build -t test:pandas .
docker run -it test:pandas

docker run -it test:pandas 2025-01-18

```

### 1.2.3 Connecting pgAdmin and Postgres

```bash

docker pull dpage/pgadmin4

docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  - p 8080:80 \
  dpage/pgadmin4

```

```bash
docker network create pg-network
```

```bash

docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="root" \
 -e POSTGRES_DB="ny_taxi" \
 -v /Users/macos/repos/data-engineering/week_1_basics_n_setup/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgres/data \
 -p 5432:5432 \
 --network pg-network \
 --name pg-database \
 postgres:13

 docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  - p 8080:80 \
  --network pgadmin \
  --name pgadmin
  dpage/pgadmin4

```
