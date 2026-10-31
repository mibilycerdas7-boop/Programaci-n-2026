"""Microreto 3: crear otro par cuando cambia un resultado.

Una tupla conserva el orden como una lista, pero sus posiciones no se cambian.
"""

# Este par guarda nombre y total semanal; 0 es el nombre y 1 es el total.
par_original = ("Soda San Pedro", 462000)
print("Nombre:", par_original[0])
print("Total original:", par_original[1])

# Otro ejemplo de la misma forma sería ("Panaderia Cartago", 351000).
# Se corrigió el total de Soda San Pedro a 470000.
# TODO: reemplace la línea provisional por una TUPLA NUEVA con nombre y total.
# No use par_original[1] = 470000: eso intenta modificar una tupla.
par_corregido = par_original
print("Total original después:", par_original[1])
print("Total del nuevo par:", par_corregido[1])

# Para explicar: ¿por qué se necesita un par nuevo?
# Para comprobar: el original conserva 462000; el nuevo muestra 470000.
