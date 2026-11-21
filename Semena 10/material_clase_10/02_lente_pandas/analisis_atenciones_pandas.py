"""El mismo expediente, con Pandas y las mismas tres funciones."""

from pathlib import Path
import pandas as pd

ARCHIVO_CSV = Path(__file__).with_name("atenciones.csv")


def explorar_atenciones(atenciones):
    print(len(atenciones))
    print(list(atenciones.columns))
    print(atenciones.head(1))


def contar_categorias(atenciones):
    for col in atenciones.select_dtypes(include=["object", "string"]).columns:
        print(atenciones[col].value_counts())


def concluir(atenciones):
    print(atenciones.describe())


try:
    atenciones = pd.read_csv(ARCHIVO_CSV, encoding="utf-8-sig")
except FileNotFoundError:
    print(f"No encontramos el archivo: {ARCHIVO_CSV}")
    raise SystemExit(1)

if not atenciones.empty:
    explorar_atenciones(atenciones)
    contar_categorias(atenciones)
    concluir(atenciones)
else:
    print("El archivo no contiene atenciones.")