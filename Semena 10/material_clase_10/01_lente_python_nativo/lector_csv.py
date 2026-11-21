"""Plantilla para leer el CSV preparado para la Semana 10."""

import csv
from pathlib import Path


ARCHIVO_CSV = Path(__file__).with_name("atenciones.csv")


def cargar_atenciones(ruta_csv=ARCHIVO_CSV):
    """Devuelve las atenciones del CSV como una lista de diccionarios."""
    atenciones = []

    try:
        with open(ruta_csv, mode="r", encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                # TODO 1A: convierta edad y minutos_espera a números enteros.
                fila["edad"] = int(fila["edad"])
                fila["minutos_espera"] = int(fila["minutos_espera"])
                # TODO 1B: agregue cada fila a la lista atenciones.
                atenciones.append(fila)

    except FileNotFoundError:
        print(f"No se encontró el archivo de datos: {ruta_csv}")
        raise SystemExit(1)

    return atenciones
