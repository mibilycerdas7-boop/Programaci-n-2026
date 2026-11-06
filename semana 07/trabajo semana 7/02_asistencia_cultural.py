"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

total_asistencias = 0
bloques_altos = 0
limite_70 = capacidad * 0.70  # 70% de 300 = 210

for asistencia in asistencias:
    total_asistencias += asistencia
    if asistencia > limite_70:
        bloques_altos += 1

promedio_asistencia = total_asistencias / len(asistencias)
porcentaje_ocupacion = (promedio_asistencia / capacidad) * 100

if porcentaje_ocupacion >= 80:
    estado_asistencia = "alta"
elif porcentaje_ocupacion >= 50:
    estado_asistencia = "media"
else:
    estado_asistencia = "baja"

print("--- CASO 2: ANÁLISIS DE ASISTENCIAS ---")
print(f"Total de asistentes: {total_asistencias}")
print(f"Promedio de asistencia: {promedio_asistencia:.1f}".replace(".", ","))
print(f"Porcentaje de ocupación: {int(porcentaje_ocupacion)} %")
print(f"Bloques que superan el 70%: {bloques_altos}")
print(f"Estado de ocupación: {estado_asistencia}\n")