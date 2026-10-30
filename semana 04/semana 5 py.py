# Definición de la lista con los datos del producto
producto = ["Cafe", 5000, 20]

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