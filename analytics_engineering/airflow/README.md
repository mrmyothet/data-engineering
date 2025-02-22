### Pre-Reqs

``` bash

cd ~ && mkdir -p ~/.google/credentials/
cp .google/credentials/google_credentials.json ~/.google/credentials/google_credentials.json

```

### Set the Airflow user

```bash
mkdir -p ./dags ./logs ./plugins

echo -e "AIRFLOW_UID=$(id -u)" > .env
```