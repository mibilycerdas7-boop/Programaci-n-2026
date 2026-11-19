"""Microreto independiente: sumar tiempos con una función y un acumulador."""


ESPERAS = [12, 20, 18]


def sumar_esperas(minutos):
    """Devuelve la suma de los minutos recibidos."""
    total = 0

    for minuto in minutos:
        # Acumulamos cada valor de la lista en la variable total
        total += minuto  # Esto equivale a: total = total + minuto

    return total


# Llamamos a la función pasando la lista ESPERAS y guardamos el resultado
total_minutos = sumar_esperas(ESPERAS)

# Imprimimos el resultado en pantalla
print("Total de minutos de espera:", total_minutos)