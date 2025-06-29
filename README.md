# Tarea3-INF339-BDDGE

Tarea 3 INF399 Base de Datos a Gran Escala

## Integrantes

1. Diego Moyano 202004509-7
2. Luis Zegarra 202073628-6
3. Nicolas Cancino 202004680-8

## Ejecutar
1. ejecutar el contendor desde visul studio `command + shif + p` y buscar Dev Containers: Reopen in container
2. al terminar la carga del contenedor, abrir nueva terminal y ejecutar `airflow standalone` para levantar airflow
3. en airflow (http://localhost:8081) loguearse, con `admin` y la password que se encuentra en la terminal cuando se termina de ejecutar el comando anterior
4. para probar el funcionamiento del DAG "run_beam_dag" se debe dar en el botón de play que aparece en la fila.
5. se actualizara/agregara el archivo de salida en la carpeta `output/file_avro1_-00000-of-00001.avro` y se enviará menaje a kafka
6. abrir UI de kafka (http://localhost:8083), en menú lateral seleccionar "Topics", luego "fan-engagement-topic" y "message" en la parte superior. Ahí estará el mensaje luego de la ejecucion de la pipeline.

### Run Airflow http://localhost:8081

Just execute
```
airflow standalone
```

### Services UI links

#### PG Admin

<http://localhost:8082>

#### Kafka UI

<http://localhost:8081>

#### Minio

<http://localhost:9001>

#### Redis 

<http://localhost:5540/>


#### Dag

##### fan_dag
Estructura del DAG