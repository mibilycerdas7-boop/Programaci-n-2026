"""Microreto: limpiar y agrupar nombres de medicamentos."""

# Este diccionario contiene las equivalencias del ejercicio.
# La clave es el nombre que podría escribir la persona.
# El valor es el nombre que guardaremos en la lista.
# Las claves están en mayúsculas porque convertiremos la entrada a mayúsculas.
EQUIVALENCIAS = {
    "ACETAMINOFEN": "ACETAMINOFÉN",
    "PARACETAMOL": "ACETAMINOFÉN",
    "PANADOL": "ACETAMINOFÉN",
    "MOTRIN": "IBUPROFENO",
    "SALIR": "N",
}


def limpiar_nombre(nombre):
    """Limpia el texto y devuelve su nombre equivalente."""

    # upper() convierte las letras a mayúsculas.
    # strip() elimina los espacios al inicio y al final del texto.
    nombre = nombre.upper().strip()

    # get() busca el nombre dentro del diccionario.
    #
    # Si encuentra la clave, devuelve su equivalencia.
    # Por ejemplo, "PANADOL" devuelve "ACETAMINOFÉN".
    #
    # Si la clave no existe, devuelve el segundo argumento: nombre.
    # Por ejemplo, "AMOXICILINA" conserva su nombre limpio.
    nombre = EQUIVALENCIAS.get(nombre, nombre)

    # return entrega el resultado al lugar donde se llamó la función.
    return nombre


# La lista comienza vacía.
# Aquí guardaremos cada medicamento después de limpiarlo.
medicamentos = []

# El ciclo permite ingresar varios medicamentos.
# True mantiene el ciclo activo hasta que ejecutemos break.
while True:

    # input() recibe lo que escribe la persona como una cadena de texto.
    medicamento = input(
        "Ingrese el nombre del medicamento o 'n' para salir: "
    )

    # Llamamos a la función y guardamos el resultado en la misma variable.
    # En este punto se limpian los espacios, se convierten las mayúsculas
    # y se aplica la equivalencia cuando existe.
    medicamento = limpiar_nombre(medicamento)

    # Una entrada como "n", " N " o "salir" termina convertida en "N".
    # break termina el ciclo antes de agregar esa entrada a la lista.
    if medicamento == "N":
        break

    # Si la persona presiona Enter sin escribir un nombre, la cadena queda
    # vacía. continue vuelve al inicio del ciclo para pedir otra entrada.
    if medicamento == "":
        print("Escriba un nombre de medicamento.")
        continue

    # append() agrega el medicamento limpio al final de la lista.
    # Las entradas repetidas también se guardan para poder contarlas después.
    medicamentos.append(medicamento)

    # Mostramos el nombre que realmente quedó guardado.
    print("Medicamento registrado:", medicamento)


# Esta parte se ejecuta después de salir del ciclo.
print("\nMedicamentos registrados:")
print(medicamentos)

# Agrupamos y contamos cuántas veces aparece cada medicamento ya limpio.
resumen_medicamentos = {}
for item in medicamentos:
    resumen_medicamentos[item] = resumen_medicamentos.get(item, 0) + 1

print("\nResumen agrupado por medicamento:")
for nombre_med, cantidad in resumen_medicamentos.items():
    print(f"- {nombre_med}: {cantidad}")

# Mantiene abierta la terminal hasta que la persona presione Enter.
input("\nPresione Enter para salir...")