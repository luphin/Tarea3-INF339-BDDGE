# Tarea3-INF339-BDDGE

Tarea 3 INF399 Base de Datos a Gran Escala

## Integrantes

1. Diego Moyano 202004509-7
2. Luis Zegarra 202073628-6
3. Nicolas Cancino 202004680-8

## Install airflow

Use the script in scripts/install-airflow.sh to install Apache Airflow

### Configurations in scripts/airflow.cfg

This installation change the default configurations of Airflow, the changes are:

- dags_folder: changed to current src folder
- simple_auth_manager_all_admins: changed to True to disable login screen
- load_examples: changed to False to avoid the load of examples in our Airflow installation
- port: changed to 8081 to access Airflow using http://localhost:8081

## Run Airflow

Just execute
```
airflow standalone
```

## Services UI links

### PG Admin

<http://localhost:8082>

### Kafka UI

<http://localhost:8083>

### Minio

<http://localhost:9001>

### Redis 

<http://localhost:5540/>


## Dag examples

## fan_dag
Estructura del DAG