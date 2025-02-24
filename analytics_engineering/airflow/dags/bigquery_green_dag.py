import os
from datetime import datetime

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateExternalTableOperator,
)

from upload_to_gcs import upload_to_gcs


PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

# URL and file name templates
URL_PREFIX = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata"
URL_TEMPLATE = URL_PREFIX + "_{{ execution_date.strftime('%Y-%m') }}.csv.gz"
OUTPUT_FILE_TEMPLATE = (
    AIRFLOW_HOME + "/output_green{{ execution_date.strftime('%Y-%m') }}.csv.gz"
)
OUTPUT_FILE_CSV_TEMPLATE = (
    AIRFLOW_HOME + "/output_green{{ execution_date.strftime('%Y-%m') }}.csv"
)

TABLE_NAME = "green_tripdata"

path_to_creds = f"/.google/credentials/google_credentials.json"
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", "trips_data_all")


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
}

# DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="bigquery_dag",
    schedule_interval="0 6 2 * *",
    start_date=datetime(2020, 7, 1),
    end_date=datetime(2020, 12, 30),
    catchup=False,
    max_active_runs=1,
    tags=["dtc-de"],
) as dag:

    curl_task = BashOperator(
        task_id="curl",
        bash_command=f"curl -sSL {URL_TEMPLATE} > {OUTPUT_FILE_TEMPLATE}",
    )

    gunzip_task = BashOperator(
        task_id="gunzip", bash_command=f"gunzip -f {OUTPUT_FILE_TEMPLATE}"
    )

    local_to_gcs_task = PythonOperator(
        task_id="local_to_gcs_task",
        python_callable=upload_to_gcs,
        op_kwargs={
            "bucket": BUCKET,
            "object_name": OUTPUT_FILE_CSV_TEMPLATE,
            "local_file": f"{AIRFLOW_HOME}/{OUTPUT_FILE_CSV_TEMPLATE}",
        },
    )

    bigquery_external_table_task = BigQueryCreateExternalTableOperator(
        task_id="bigquery_external_table_task",
        table_resource={
            "tableReference": {
                "projectId": PROJECT_ID,
                "datasetId": BIGQUERY_DATASET,
                "tableId": "green_tripdata_2020_01",
            },
            "externalDataConfiguration": {
                "sourceFormat": "PARQUET",
                "sourceUris": [f"gs://{BUCKET}/{OUTPUT_FILE_CSV_TEMPLATE}"],
                "autodetect": True,
            },
        },
    )

    (curl_task >> gunzip_task >> local_to_gcs_task >> bigquery_external_table_task)
