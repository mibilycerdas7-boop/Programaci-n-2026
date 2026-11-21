"""Semana 10: resolvemos juntos el caso pendiente de la Semana 9."""

from lector_csv import cargar_atenciones


def explorar_atenciones(atenciones):
    """Decisión 1: ¿qué leímos y cuántas atenciones hay?"""
    # Contamos las filas con un for. Luego miramos los campos de la primera.
    cantidad = 0
    for atencion in atenciones:
        # Completamos aquí el contador.
        cantidad += 1

    print("Atenciones:", cantidad)
    print("Campos:", list(atenciones[0]))


def contar_categorias(atenciones):
    """Decisión 2: ¿qué medicamentos, hospitales y diagnósticos aparecen?"""
    medicamentos = {}
    hospitales = {}
    diagnosticos = {}
    
def concluir(atenciones):
    print("Pacientes:", atenciones["cedula"].nunique())
    print("Minutos espera:", atenciones["minutos_espera"].sum())
    print("Promedio espera:", atenciones["minutos_espera"].mean())
    print("Mediana espera:", atenciones["minutos_espera"].median())
    
    for atencion in atenciones:
        # Los nombres ya vienen uniformes en el CSV.
        # Contamos cada categoría en su diccionario con .get().
        medicamento = atencion["medicamento"]
        if medicamento not in medicamentos:
            medicamentos[medicamento] = 0
        medicamentos[medicamento] += 1 
        
        
        
    #get()
    hospital = atencion["hospital"]
    #hospital["san juan"]
    hospitales[hospital] =  hospitales.get(hospital, 0) + 1




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
