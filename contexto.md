El objetivo de esta tarea es aplicar tus conocimientos en Apache Beam y Apache
Airflow para construir una ETL que permita convertir los datos de participaci´on de fans
de la Liga de Carreras de Helic´opteros (HRL) de Json a Avro, para su posterior uso en el
entrenamiento de modelos de Machine Learning.
2. Descripci´on
La Liga de Carreras de Helic´opteros (HRL) recolecta informaci´on de la participaci´on
de sus fans en sus aplicaciones durante sus transmisiones. El objetivo es entrenar modelos
de Machine Learning que permitan predecir si un fan utilizar´a el servicio de predicciones
y/o comprar´a art´ıculos de Merchandising con el fin de ofrecer banners de publicidad
personalizados.
Los datos se recolectan en formato Json, con la siguiente estructura:
FanID: identificador ´unico del fan.
RaceID: identificador de la carrera visualizada por el fan.
Timestamp: momento en el que el fan inicio la transmisi´on de la carrera, en formato
’ %Y- %m- %d %H: %M: %S’.
ViewerLocationCountry: pa´ıs desde donde visualiza la carrera.
DeviceType: tipo de dispositivo desde el cual visualiza la carrera.
EngagementMetric secondswatched: cantidad de segundos que un fan ha visualizado
la carrera.
PredictionClicked: True si accedi´o a la secci´on de predicciones, False en caso
contrario.
MerchandisingClicked: True si accedi´o a la secci´on de compra de Merchandising,
False en caso contrario.
Los ingenieros de ML le han pedido convertir la columna Timestamp a Unix timestamp
en milisegundos, por lo que se ha agregado una nueva columna: Timestamp unix.
La plataforma de ML soporta datos en formato Avro, los datos de salida deben utilizar
el siguiente esquema Avro:
1
{
"type": "record",
"name": "FanEngagement",
"fields": [
{"name": "FanID", "type": "string"},
{"name": "RaceID", "type": "string"},
{"name": "Timestamp", "type": "string"},
{"name": "Timestamp_unix", "type":{
"type": "long",
"logicalType": "timestamp-millis"
}},
{"name": "ViewerLocationCountry", "type": "string"},
{"name": "DeviceType", "type": "string"},
{"name": "EngagementMetric_secondswatched", "type": "int"},
{"name": "PredictionClicked", "type": "boolean"},
{"name": "MerchandisingClicked", "type": "boolean"}
]
}
Se incluye un fichero JsonL con datos de prueba.
3. Actividades
Para los requerimientos mencionados, deber´as (100 puntos):
1. Construir una ETL en Apache Beam que realice la conversi´on de los archivos Json a
Avro con el esquema entregado. Su ETL deber´a calcular el campo Timestamp unix.
Debe tener en cuenta que los datos de entrada y de salida pueden estar en un bucket
y/o en el sistema de ficheros local. (40 puntos)
2. Construir un Dag en Airflow que permita ejecutar en forma diaria el procesamiento
de los archivos Json de entrada. (40 puntos) Al finalizar el job de Apache Beam
deber´a notificar a un t´opico de Kafka que lo datos est´an disponibles para consumo,
con el siguiente mensaje Json:
{
"event_type": "data_processing_completed",
"data_entity": "FanEngagement",
"status": "success",
"location": path_or_bucket,
"processed_at": processed_timestamp,
"source_system": pipeline_name
}
Con
2
path or bucket: path o URI de los datos procesados.
processed timestamp: momento en el que se termin´o el procesamiento de
los datos y se envi´o el mensaje, en formato ’ %Y- %m- %d %H: %M: %S’.
pipeline name: nombre de su Dag.
3. Construya un workspace usando Visual Studio Code y devcontainers en el cual
se pueda ejecutar su c´odigo en local, incluyendo los servicios necesarios para su
correcto funcionamiento, debe agregar un archivo Readme.md con las indicaciones
para ejecutar su Dag. (10 puntos)
4. Conclusiones: desarrolle un peque˜no informe con los principales desafios a los que
se enfrent´o para resolver esta actividad. (10 puntos)