import requests
from airflow.decorators import dag, task
from datetime import datetime


@dag(schedule="@daily", start_date=datetime(2021, 12, 1), catchup=False)
def sample_dag():
    @task(task_id="print_the_context")
    def print_context(ds=None, **kwargs):
        """Print the Airflow context and ds variable from the context."""
        print(ds)
        return "Whatever you return gets printed in the logs"

    print_context()


sample_dag()
