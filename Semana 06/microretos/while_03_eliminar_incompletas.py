"""Micro-reto 5: eliminar registros incompletos con while y remove().

Contexto: respuestas ficticias de una encuesta universitaria sobre recursos
de estudio. Para este resumen se excluirán las respuestas "Sin respuesta".

Prediga la lista final y cuántas respuestas incompletas se eliminarán.
"""

respuestas = ["Bueno", "Sin respuesta", "Excelente", "Sin respuesta", "Regular"]
cantidad_incompletas = respuestas.count("Sin respuesta")

while "Sin respuesta" in respuestas:
    # TODO: elimine una respuesta "Sin respuesta" de la lista.
    pass

print("Respuestas para analizar:", respuestas)
print("Respuestas incompletas eliminadas:", cantidad_incompletas)

# Resultado esperado:
# Respuestas para analizar: ['Bueno', 'Excelente', 'Regular']
# Respuestas incompletas eliminadas: 2
