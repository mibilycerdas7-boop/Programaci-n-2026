"""Semana 10: resolvemos juntos el caso pendiente de la Semana 9."""

from lector_csv import cargar_atenciones


def explorar_atenciones(atenciones):
    """Decisión 1: ¿qué leímos y cuántas atenciones hay?"""
    # Contamos las filas con un for. Luego miramos los campos de la primera.
    cantidad = 0
    for atencion in atenciones:
        # Completamos aquí el contador.
        pass

    print("Atenciones:", cantidad)
    print("Campos:", list(atenciones[0]))


def contar_categorias(atenciones):
    """Decisión 2: ¿qué medicamentos, hospitales y diagnósticos aparecen?"""
    medicamentos = {}
    hospitales = {}
    diagnosticos = {}

    for atencion in atenciones:
        # Los nombres ya vienen uniformes en el CSV.
        # Contamos cada categoría en su diccionario con .get().
        pass

    print("Medicamentos:", medicamentos)
    print("Hospitales:", hospitales)
    print("Diagnósticos:", diagnosticos)


def concluir(atenciones):
    """Decisiones 3 y 4: ¿cuántas personas hay y cuánto esperaron?"""
    visitas = {}
    total_minutos = 0

    for atencion in atenciones:
        # Contamos la cédula y acumulamos los minutos de espera.
        pass

    print("Personas:", len(visitas))
    print("Minutos de espera:", total_minutos)
    print("Promedio:", total_minutos / len(atenciones))


atenciones = cargar_atenciones()
if atenciones:
    explorar_atenciones(atenciones)
    contar_categorias(atenciones)
    concluir(atenciones)
else:
    print("Revisamos los TODO de lector_csv.py.")
