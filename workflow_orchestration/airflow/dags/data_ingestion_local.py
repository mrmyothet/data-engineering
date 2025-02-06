from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

local_workflow = DAG("LocalIngestionDag")

with local_workflow:

    wget_task = BashOperator(
        task_id="wget_task",
        bash_command='echo "hello world"',
    )
