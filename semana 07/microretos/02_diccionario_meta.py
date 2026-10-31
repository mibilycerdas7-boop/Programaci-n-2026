"""Microreto 2: leer y cambiar un campo de un diccionario.

Un diccionario guarda campos con nombre; cada nombre es una clave.
"""

# A diferencia de ventas[1], aquí se usa una clave como sede["meta"].
# La lista de ventas puede ser uno de los valores del diccionario.
sede = {
    "nombre": "Soda San Pedro",
    "provincia": "San Jose",
    "ventas": [85000, 92000, 78000],
    "meta": 450000,
}
print("Nombre:", sede["nombre"])
print("Primera venta:", sede["ventas"][0])
print("Meta inicial:", sede["meta"])

# La meta registrada cambió a 470000.
# TODO: actualice solo el valor asociado con la clave "meta".

print("Meta corregida:", sede["meta"])
print("Nombre después del cambio:", sede["nombre"])

# Para explicar: ¿por qué el nombre y las ventas siguen iguales?
# Para comprobar: la meta pasa de 450000 a 470000.
