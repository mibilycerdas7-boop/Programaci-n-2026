"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

consumo_total = sum(consumos_litros)
promedio_diario = consumo_total / len(consumos_litros)

primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[-1]

litros_ahorrados = primer_dia - ultimo_dia
porcentaje_reduccion = (litros_ahorrados / primer_dia) * 100

if porcentaje_reduccion >= 15:
    clasificacion_agua = "reducción alta"
elif porcentaje_reduccion > 0:
    clasificacion_agua = "reducción moderada"
else:
    clasificacion_agua = "sin reducción"

print("--- CASO 1: CONSUMO DIARIO DE AGUA ---")
print(f"Consumo total: {consumo_total} L")
print(f"Promedio diario: {promedio_diario:.1f} L".replace(".", ","))
print(f"Litros ahorrados (primer vs. último día): {litros_ahorrados} L")
print(f"Porcentaje de reducción: {int(porcentaje_reduccion)} %")
print(f"Clasificación: {clasificacion_agua}\n")