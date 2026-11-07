"""Semana 8: informe de atenciones hospitalarias ficticias.

Complete las fases con el docente. La lectura de datos ya está preparada.
"""

# FASE 0: CONSUMIR LA CONEXIÓN PREPARADA
# conexion_api.py se encuentra junto a este archivo.
from conexion_api import cargar_datos

registros = cargar_datos()
print("Fuente: JSON público de GitHub")
print("Atenciones recibidas:", len(registros))

# La muestra solicitada usa range(3): deben existir las posiciones 0, 1 y 2.
if len(registros) < 3:
    raise SystemExit("Se necesitan al menos 3 registros. Publique la etapa 3.")

# FASE 1: MOSTRAR Y CONTAR LOS MEDICAMENTOS DE TRES ATENCIONES
conteo_medicamentos = {}
medicamentos_totales = 0
print("\n\tANALISIS FASE #1 MUESTRA 3")
for indice in range(3):
    registro = registros[indice]
    print(f"\nCédula: {registro['paciente_cedula']}"
        f"\n- Paciente: {registro['paciente_nombre']}"
        f"\n- Diagnóstico: {registro['diagnostico']}"
        f"\n- Medicamentos: {registro['medicamentos']}")

    for medicamento in registro['medicamentos']:
        print(medicamento)
        medicamentos_totales += 1
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1
        
print("Total de medicamentos recetados:", medicamentos_totales)

# FASE 2: CONTAR LOS MEDICAMENTOS DE TODAS LAS ATENCIONES
print("\nANALISIS FASE #2 MEDICAMENTOS Y ATENCIONES")
for registro in registros:
    print(registro['paciente_nombre'])

# FASE 3: CONTAR ATENCIONES POR HOSPITAL
print("\n" + "="*50)
print("  ANALISIS FASE #3 - ATENCIONES POR HOSPITAL")
print("="*50)

conteo_hospitales = {}

for registro in registros:
    hospital = registro['hospital']
    if hospital in conteo_hospitales:
        conteo_hospitales[hospital] += 1
    else:
        conteo_hospitales[hospital] = 1

for hospital, cantidad in conteo_hospitales.items():
    print(f"  Hospital {hospital}: {cantidad} pacientes atendidos")

print("\n" + "-"*50)
print("  Fin Fase 3")
print("-"*50)

# FASE 4: CONTAR ATENCIONES POR ENFERMEDAD DIAGNOSTICADA
print("\n" + "="*50)
print("  ANALISIS FASE #4 - ATENCIONES POR ENFERMEDAD DIAGNOSTICADA")
print("="*50)

conteo_enfermedades = {}

for registro in registros:
    diagnostico = registro['diagnostico']
    if diagnostico in conteo_enfermedades:
        conteo_enfermedades[diagnostico] += 1
    else:
        conteo_enfermedades[diagnostico] = 1

for enfermedad, cantidad in conteo_enfermedades.items():
    print(f"  Diagnóstico '{enfermedad}': {cantidad} casos")

print("\n" + "-"*50)
print("  Fin Fase 4")
print("-"*50)