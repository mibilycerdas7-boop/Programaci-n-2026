# Definición de la lista con los datos del producto
#             0       1    2 
producto = ["Café", 5000, 20]

# Definir la variable para el escenario del porcentaje de aumento (puedes cambiarlo a 10, 15 o 20)
porcentaje_aumento = 20

# 1. Cálculos basados estrictamente en los índices de la lista
# Índice 0: Nombre | Índice 1: Precio | Índice 2: Unidades vendidas
descuento = producto[1] * 15 / 100
precio_promocional = producto[1] - descuento

# Corregido: se usa "ingreso_actual" para que coincida con el resto del código
ingreso_actual = producto[1] * producto[2]

# 2. Cálculo de unidades proyectadas usando el porcentaje de aumento
aumento_unidades = producto[2] * porcentaje_aumento / 100
unidades_proyectadas = producto[2] + aumento_unidades

# 3. Cálculo de ingresos proyectados y diferencia
ingreso_con_promocion = precio_promocional * unidades_proyectadas
diferencia = ingreso_con_promocion - ingreso_actual

# 4. Evaluación de la condición para la recomendación
if diferencia > 0:
    recomendacion = "lanzar"
else:
   recomendacion = "no lanzar"
   
# 5. Salida esperada en consola con formato exacto
print("ANÁLISIS DE PROMOCIÓN\n")
print(f"Producto: {producto[0]}")
print(f"Precio actual: ₡{producto[1]:,.2f}")
print(f"Unidades actuales: {producto[2]}")
print(f"Ingreso actual: ₡{ingreso_actual:,.2f}")
print(f"Descuento: ₡{descuento:,.2f}")
print(f"Precio promocional: ₡{precio_promocional:,.2f}")
print(f"Aumento esperado en ventas: {porcentaje_aumento}%")
print(f"Unidades proyectadas: {unidades_proyectadas}")
print(f"Ingreso con promoción: ₡{ingreso_con_promocion:,.2f}")
print(f"Diferencia: ₡{diferencia:,.2f}\n")
print(f"RECOMENDACIÓN: {recomendacion}.")