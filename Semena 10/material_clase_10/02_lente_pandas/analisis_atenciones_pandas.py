"""El mismo expediente, con Pandas y las mismas tres funciones."""

from pathlib import Path

ARCHIVO_CSV = Path(__file__).with_name("atenciones.csv")


def explorar_atenciones(atenciones):
    pass


def contar_categorias(atenciones):
    pass


def concluir(atenciones):
    pass


try:
    pass ##PANDAS.....
except FileNotFoundError:
    print(f"No encontramos el archivo: {ARCHIVO_CSV}")
    raise SystemExit(1)

if not atenciones.empty:
    explorar_atenciones(atenciones)
    contar_categorias(atenciones)
    concluir(atenciones)
else:
    print("El archivo no contiene atenciones.")
