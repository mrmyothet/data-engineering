### Install Anaconda

```bash 
sudo apt update && sudo apt upgrade -y

cd /temp
wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh

bash Anaconda3-2024.10-1-Linux-x86_64.sh

```

### Install packages 
```bash 
pip install pandas
pip install pyarrow

pip install python-dotenv

pip install psycopg2-binary
pip install sqlalchemy
pip install pgcli

pip install google-cloud-storage

pip install dlt

```




### Instal dbt Core

```bash
pip install dbt-core

dbt init 
Enter a name for your project(letters, digits, underscore): taxi_rides_ny

Runtime Error
  No adapters available. Learn how to install an adapter by going to https://docs.getdbt.com/docs/connect-adapters#install-using-the-cli

```

```bash 
pip install dbt-postgres

dbt --version 
Core:
  - installed: 1.9.2
  - latest:    1.9.2 - Up to date!

Plugins:
  - postgres: 1.9.0 - Up to date!
```

Profile taxi_rides_ny written to /home/myothet/.dbt/profiles.yml

### load data hacks

```sql
SELECT COUNT(*) FROM `trips_data_all.green_tripdata`; --8,035,139

SELECT COUNT(*) FROM `trips_data_all.yellow_tripdata`; --109,247,514
```