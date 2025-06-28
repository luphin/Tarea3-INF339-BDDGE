from apache_beam.dataframe.io import read_csv

import argparse
import logging
import re
import json
import pyarrow as pa
from datetime import datetime
from decimal import Decimal
import csv
import fastavro

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io.avroio import WriteToAvro