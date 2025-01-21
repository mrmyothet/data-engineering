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
 -v ./ny_taxi_postgres_data:/var/lib/postgres/data \
 -p 5432:5432 \
 --network pg-network \
 --name pg-database \
 postgres:13

docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network pg-network \
  --name pgadmin \
  dpage/pgadmin4

```

---

### Convert Jupyter Notebook into python script

```bash
jupyter nbconvert --to=script upload-data.ipynb
```

---

### 1.2.4 Dockerizing the Ingestion script

```bash

URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

python ingest_data.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --tb=yellow_taxi_trips \
  --url=${URL}

```

```bash

docker build -t taxi_ingest:v001 .

docker run -it \
  --network=pg-network \
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --tb=yellow_taxi_trips \
    --url=${URL}

```

```bash

python -m http.server

```

### 1.2.5 Running Postgres and pgAdmin with Docker-Compose

```bash
docker-compose up

docker-compose down

docker-compose up -d
```
