from fastavro import reader
import os

ruta = "/workspaces/Tarea3-INF339-BDDGE/output/file_avro1_-00000-of-00001.avro"

if os.path.exists(ruta):
    with open(ruta, "rb") as fo:
        avro_reader = reader(fo)
        count = 0
        for record in avro_reader:
            print(record)
            count += 1
        if count == 0:
            print("[lectura] El archivo se abrió correctamente, pero no contiene registros.")
else:
    print("[lectura] El archivo no existe:", ruta)