import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io.avroio import WriteToAvro
import json
import time
from datetime import datetime, timezone
import fastavro
import argparse
import logging


AVRO_SCHEMA_PATH = 'resources/fan_engagement.avsc'
LOCAL_DATA_PATH = 'data/fan_engagement.json'

class _OutputFn(beam.DoFn):
    def __init__(self, label=None):
        super().__init__()
    
    def process(self, element):
        record = json.loads(element)

        try:
            # Convertir 'Timestamp' a datetime y luego a milisegundos
            dt = datetime.strptime(record["Timestamp"], "%Y-%m-%d %H:%M:%S")
            record["Timestamp_unix"] = dt.replace(tzinfo=timezone.utc)

            # Validar tipos
            record["FanID"] = str(record["FanID"])
            record["RaceID"] = str(record["RaceID"])
            record["ViewerLocationCountry"] = str(record["ViewerLocationCountry"])
            record["DeviceType"] = str(record["DeviceType"])
            record["EngagementMetric_secondswatched"] = int(record["EngagementMetric_secondswatched"])
            record["PredictionClicked"] = bool(record["PredictionClicked"])
            record["MerchandisingClicked"] = bool(record["MerchandisingClicked"])

            yield record

        except Exception as e:
            logging.getLogger().setLevel(e)
            pass  # Ignorar registros inválidos

def main(argv=None, save_main_session=True):
    parser = argparse.ArgumentParser()

    known_args, pipeline_args = parser.parse_known_args(argv)
    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(
        SetupOptions).save_main_session = save_main_session 

    # Load avro schema
    parsed_schema = fastavro.schema.load_schema(AVRO_SCHEMA_PATH)

    with beam.Pipeline(options=pipeline_options) as p:
        lines =(
            p
            | "Leer JSON" >> beam.io.ReadFromText(LOCAL_DATA_PATH)
            | "transformar" >> beam.ParDo(_OutputFn())
        )

        # Write the data to an Avro file
        lines | 'Write to Avro' >> WriteToAvro(
            'output/file_avro1_',
            schema=parsed_schema,
            file_name_suffix='.avro',
        )

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main()
