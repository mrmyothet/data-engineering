import os
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateExternalTableOperator,
)
from airflow import DAG

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", "trips_data_all")

default_args = {
    "owner": "airflow",
}

with DAG(
    dag_id="bigquery_external_table", tags=["BigQuery"], default_args=default_args
) as dag:

    bigquery_external_table_task = BigQueryCreateExternalTableOperator(
        task_id="bigquery_external_table_task",
        table_resource={
            "tableReference": {
                "projectId": PROJECT_ID,
                "datasetId": BIGQUERY_DATASET,
                "tableId": "green_tripdata",
            },
            "externalDataConfiguration": {
                "sourceFormat": "CSV",
                "sourceUris": [f"gs://{BUCKET}/green_tripdata_*.csv"],  # Use wildcard
                "autodetect": True,
            },
        },
    )

    (bigquery_external_table_task)
