"""Microreto 4: guardar provincias sin repetirlas.

Un set conserva valores únicos. Se agrega con add(), sin posición ni índice.
"""

# También se puede iniciar vacío con set(); {} vacío crea un diccionario.
provincias = {"San Jose", "Cartago"}
print("Cantidad inicial:", len(provincias))
print("¿Está San Jose?:", "San Jose" in provincias)

# TODO: agregue otra vez "San Jose" mediante add().
print("Después de repetir San Jose:", len(provincias))

# TODO: agregue "Heredia" mediante add().
print("Después de agregar Heredia:", len(provincias))
print("¿Está Heredia?:", "Heredia" in provincias)

# Para explicar: ¿por qué repetir San Jose no aumenta la cantidad?
# Para comprobar: las cantidades son 2, 2 y 3; Heredia sí es un dato nuevo.
# Si imprime el set, el orden de las provincias puede variar.
