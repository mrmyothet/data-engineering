import os
from dotenv import load_dotenv

load_dotenv()

from datetime import datetime

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from ingest_yellow_callable import ingest_yellow_callable


AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")


PG_HOST = os.getenv("PG_HOST")
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_PORT = os.getenv("PG_PORT")
PG_DATABASE = os.getenv("PG_DATABASE")


local_workflow = DAG(
    "Ingest_Yellow_TripData",
    schedule_interval="0 6 2 * *",
    start_date=datetime(2019, 1, 1),
    end_date=datetime(2019, 3, 31),
)


URL_PREFIX = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata"

URL_TEMPLATE = URL_PREFIX + "_{{ execution_date.strftime('%Y-%m') }}.csv.gz"

OUTPUT_FILE_TEMPLATE = (
    AIRFLOW_HOME + "/output_yellow_{{ execution_date.strftime('%Y-%m') }}.csv.gz"
)

OUTPUT_FILE_CSV_TEMPLATE = (
    AIRFLOW_HOME + "/output_yellow_{{ execution_date.strftime('%Y-%m') }}.csv"
)
# TABLE_NAME_TEMPLATE = "yellow_taxi_{{ execution_date.strftime('%Y_%m') }}"
TABLE_NAME = "yellow_tripdata"

with local_workflow:
    curl_task = BashOperator(
        task_id="curl",
        bash_command=f"curl -sSL {URL_TEMPLATE} > {OUTPUT_FILE_TEMPLATE}",
    )

    gunzip_task = BashOperator(
        task_id="gunzip", bash_command=f"gunzip -f {OUTPUT_FILE_TEMPLATE}"
    )

    ingest_task = PythonOperator(
        task_id="ingest",
        python_callable=ingest_yellow_callable,
        op_kwargs=dict(
            user=PG_USER,
            password=PG_PASSWORD,
            host=PG_HOST,
            port=PG_PORT,
            db=PG_DATABASE,
            table_name=TABLE_NAME,
            csv_file=OUTPUT_FILE_CSV_TEMPLATE,
        ),
    )

    curl_task >> gunzip_task >> ingest_task
