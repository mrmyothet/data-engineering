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