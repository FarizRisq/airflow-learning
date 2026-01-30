from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@once",
    catchup=False,
) as dag:

    say_hello = BashOperator(
        task_id="say_hello",
        bash_command="echo 'Hello Airflow from GitHub Codespaces'"
    )
