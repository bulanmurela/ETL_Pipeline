from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import papermill as pm

# Define the paths for the notebook
NOTEBOOK_PATH = '/opt/airflow/notebooks/ETL_Pipeline.ipynb'
OUTPUT_NOTEBOOK_PATH = '/opt/airflow/notebooks/output/ETL_Pipeline_Output.ipynb'

# Function to run the entire ETL pipeline notebook
def run_etl_notebook():
    pm.execute_notebook(
        NOTEBOOK_PATH,                # Input notebook path
        OUTPUT_NOTEBOOK_PATH,         # Output notebook path (with results)
        parameters={}                 # Pass parameters if needed
    )

# Define the DAG
with DAG(
    dag_id='etl_pipeline_dag',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:
    
    run_etl = PythonOperator(
        task_id='run_etl_pipeline',
        python_callable=run_etl_notebook
    )

    run_etl
