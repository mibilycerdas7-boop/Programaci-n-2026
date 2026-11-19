"""Micro-reto 4: reunir datos hasta recibir una palabra de cierre.

Contexto: se registran resultados ficticios de una actividad universitaria.
La cantidad de registros no se conoce al iniciar.

Ingrese enteros positivos y escriba "fin" para terminar. No ingrese texto
distinto de "fin" ni números negativos en esta práctica.
"""

resultados = []
entrada = input("Resultado (o fin para terminar): ").strip().lower()

while entrada != "fin":
    resultado = int(entrada)
    # TODO: agregue el resultado a la lista.
    pass

    entrada = input("Resultado (o fin para terminar): ").strip().lower()

print("Resultados registrados:", resultados)
print("Cantidad de resultados:", len(resultados))

if resultados:
    promedio = sum(resultados) / len(resultados)
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron resultados.")

# Con las entradas 80, 65, 90 y fin, se espera:
# Resultados registrados: [80, 65, 90]
# Cantidad de resultados: 3
# Promedio: 78.33
