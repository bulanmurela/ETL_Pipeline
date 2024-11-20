from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from nbconvert import PythonExporter
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat

# Define the paths for the notebook
NOTEBOOK_PATH = '/opt/airflow/notebooks/ETL_Pipeline.ipynb'
OUTPUT_NOTEBOOK_PATH = '/opt/airflow/notebooks/output/ETL_Pipeline_Output.ipynb'

# Function to run the entire ETL pipeline notebook using nbconvert
def run_etl_notebook():
    # Baca notebook
    with open(NOTEBOOK_PATH) as f:
        nb = nbformat.read(f, as_version=4)

    # Tentukan preprocessor
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    # Jalankan notebook
    ep.preprocess(nb, {'metadata': {'path': '/opt/airflow/notebooks/'}})

    # Simpan hasilnya jika diperlukan
    with open(OUTPUT_NOTEBOOK_PATH, 'w') as f:
        nbformat.write(nb, f)

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
