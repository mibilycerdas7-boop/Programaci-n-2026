"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

suma_precios = sum(precios)
promedio_precios = suma_precios / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo

contador_sobre_promedio = 0
indice = 0

while indice < len(precios):
    if precios[indice] > promedio_precios:
        contador_sobre_promedio += 1
    indice += 1

if rango >= 300:
    clasificacion_rango = "variación alta"
elif rango >= 150:
    clasificacion_rango = "moderada"
else:
    clasificacion_rango = "baja"

print(f"--- CASO 3: ANÁLISIS DE PRECIOS: {producto.upper()} ---")
print(f"Promedio: ₡{promedio_precios:,.0f}".replace(",", "."))
print(f"Mínimo: ₡{minimo:,.0f}".replace(",", "."))
print(f"Máximo: ₡{maximo:,.0f}".replace(",", "."))
print(f"Rango: ₡{rango:,.0f}".replace(",", "."))
print(f"Precios sobre el promedio: {contador_sobre_promedio}")
print(f"Variación del rango: {clasificacion_rango}\n")