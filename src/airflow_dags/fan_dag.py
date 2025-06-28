from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from kafka import KafkaProducer
import json

default_args = {
    'start_date': datetime(2024, 1, 1),
}

def notify_kafka():
    producer = KafkaProducer(bootstrap_servers='kafka:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    message = {
        "event_type": "data_processing_completed",
        "data_entity": "FanEngagement",
        "status": "success",
        "location": "/app/etl/output/",
        "processed_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "source_system": "fan_engagement_dag"
    }
    producer.send("fan-engagement-topic", message)
    producer.flush()

with DAG("fan_engagement_dag", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
    run_beam = BashOperator(
        task_id="run_beam_pipeline",
        bash_command="python /app/etl/main.py"
    )

    notify = PythonOperator(
        task_id="notify_kafka",
        python_callable=notify_kafka
    )

    run_beam >> notify
