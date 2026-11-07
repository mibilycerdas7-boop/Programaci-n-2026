"""Lectura sencilla de los registros públicos de la Semana 8."""

import json
from urllib.error import URLError
from urllib.request import Request, urlopen

# Esta dirección apunta al JSON de atenciones publicado en GitHub.
URL_DATOS = (
    "https://api.github.com/repos/amenaactppp/td10-datos-publicos/contents/datos/registros.json?ref=main"
)


def cargar_datos():
    """Lee el JSON público y devuelve una lista de atenciones."""
    # GitHub recibe la dirección y estas cabeceras para entregar el JSON.
    solicitud = Request(URL_DATOS, headers={
        "Accept": "application/vnd.github.raw+json",
        "User-Agent": "TD10-Semana08-Clase",
    })

    try:
        # Abrimos la conexión y convertimos el JSON en datos de Python.
        with urlopen(solicitud, timeout=10) as respuesta:
            registros = json.load(respuesta)

        # El análisis necesita una lista: cada elemento es una atención.
        if not isinstance(registros, list):
                raise TypeError("La fuente no contiene una lista de atenciones")
    except (URLError, TimeoutError, json.JSONDecodeError, TypeError, OSError) as error:
        raise SystemExit(f"No se pudieron leer los datos públicos: {error}") from error

    return registros
