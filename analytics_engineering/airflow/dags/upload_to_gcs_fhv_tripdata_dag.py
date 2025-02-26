import os
from datetime import datetime

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


from airflow.providers.google.cloud.transfers.gcs_to_bigquery import (
    GCSToBigQueryOperator,
)

from upload_to_gcs import upload_to_gcs


# path_to_creds = f"/.google/credentials/google_credentials.json"

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", "trips_data_all")

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

# URL and file name templates
URL_PREFIX = (
    "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata"
)
URL_TEMPLATE = URL_PREFIX + "_{{ execution_date.strftime('%Y-%m') }}.csv.gz"
OUTPUT_FILE_TEMPLATE = (
    AIRFLOW_HOME + "/output_fhv_{{ execution_date.strftime('%Y-%m') }}.csv.gz"
)
OUTPUT_FILE_CSV_TEMPLATE = (
    AIRFLOW_HOME + "/output_fhv_{{ execution_date.strftime('%Y-%m') }}.csv"
)
GCS_OUTPUT_FILE_CSV_FILE_NAME = "fhv_{{ execution_date.strftime('%Y-%m') }}.csv"

TABLE_NAME = "fhv_tripdata"


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
}

# DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="upload_to_gcs_fhv_tripdata",
    tags=["GCS"],
    schedule_interval="0 6 2 * *",
    start_date=datetime(2019, 2, 1),
    end_date=datetime(2019, 12, 31),
    max_active_runs=1,
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
            "object_name": GCS_OUTPUT_FILE_CSV_FILE_NAME,
            "local_file": f"{OUTPUT_FILE_CSV_TEMPLATE}",
        },
    )

    (curl_task >> gunzip_task >> local_to_gcs_task)
