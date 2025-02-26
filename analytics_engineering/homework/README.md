### Module 4 - Homework

- Load parquet files from "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2020-{month}.parquet"
- Problem - No of records doest not match described at the homework 

---

- load data from bigquery public data - also number of records does not match

---

Now, I can upload csv files to gcs using airflow 

- analytics_engineering/airflow/dags/bigquery_green_dag.py

When using `BigQueryCreateExternalTableOperator` it only works for one csv file. 

-- 

Try using `GCSToBigQueryOperator`

Got error 
```bash
google.api_core.exceptions.BadRequest: 400 Provided Schema does not match Table ny-rides-mt:trips_data_all.green_tripdata. Field congestion_surcharge has changed type from STRING to INTEGER; 

reason: invalid, message: Provided Schema does not match Table ny-rides-mt:trips_data_all.green_tripdata. Field congestion_surcharge has changed type from STRING to INTEGER; 

reason: invalid, message: It looks like you are appending to an existing table with autodetect enabled. Disabling autodetect may resolve this.
```

---

- Upload csv files from https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata to gcs

- Create external table referring to gcs path

```sql
CREATE OR REPLACE EXTERNAL TABLE `ny-rides-mt.trips_data_all.ext_green_taxi`
OPTIONS (
  format = 'CSV',
  uris = ['gs://ny_taxi_data_mt/green_2019-*.csv', 'gs://ny_taxi_data_mt/green_2020-*.csv']
);

```

- You should have exactly 7,778,101 records in your Green Taxi table
```sql
SELECT COUNT(*) FROM `ny-rides-mt.trips_data_all.ext_green_taxi`; --7778101

```

- Create Table from External tables not to depend on csv files sources

```sql
CREATE TABLE `ny-rides-mt.trips_data_all.green_tripdata` as 
SELECT * FROM `ny-rides-mt.trips_data_all.ext_green_taxi`;

```

- Delete external table - ext_green_taxi 
- Delete csv files from GCS

---

- Upload yellow tripdata csv files from https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata to GCS
- Create external table referring to gcs path
```sql
CREATE OR REPLACE EXTERNAL TABLE `ny-rides-mt.trips_data_all.ext_yellow_taxi`
OPTIONS (
  format = 'CSV',
  uris = ['gs://ny_taxi_data_mt/yellow_2019-*.csv', 'gs://ny_taxi_data_mt/yellow_2020-*.csv']
);
```
- You should have exactly 109,047,518 records in your Yellow Taxi table
```sql
SELECT COUNT(*) FROM `ny-rides-mt.trips_data_all.ext_yellow_taxi`; -- 109047518
```

- Create Table from External tables not to depend on csv files sources
```sql
CREATE TABLE `ny-rides-mt.trips_data_all.yellow_tripdata` as 
SELECT * FROM `ny-rides-mt.trips_data_all.ext_yellow_taxi`;

```

- Delete external table - ext_yellow_taxi 
- Delete csv files from GCS

---

- Upload for hire vehical (FHV) csv files from 
https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-01.csv.gz