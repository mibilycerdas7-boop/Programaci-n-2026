"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).

total_minutos = 0
total_casos = len(incidencias)

conteo_categorias = {
    "Acceso": 0,
    "Equipo": 0,
    "Red": 0
}

casos_pendientes = 0
provincias_pendientes = set()
casos_urgentes = []
caso_mas_largo = ("", 0)

for incidencia in incidencias:
    total_minutos += incidencia["minutos_atencion"]
    categoria = incidencia["categoria"]
    if categoria in conteo_categorias:
        conteo_categorias[categoria] += 1

    if not incidencia["resuelto"]:
        casos_pendientes += 1
        provincias_pendientes.add(incidencia["provincia"])

        if incidencia["minutos_atencion"] >= 60:
            casos_urgentes.append((incidencia["id"], incidencia["minutos_atencion"]))

    if incidencia["minutos_atencion"] > caso_mas_largo[1]:
        caso_mas_largo = (incidencia["id"], incidencia["minutos_atencion"])

promedio_minutos = total_minutos / total_casos if total_casos > 0 else 0
san_jose_pendiente = "San Jose" in provincias_pendientes

print("--- CASO 4: ANÁLISIS DE REGISTROS DE SOPORTE ---")
print(f"Total de casos: {total_casos}")
print(f"Total de minutos: {total_minutos}")
print(f"Promedio de minutos: {promedio_minutos:.1f}".replace(".", ","))
print("Conteo por categoría:")
for cat, conteo in conteo_categorias.items():
    print(f"  - {cat}: {conteo}")
print(f"Cantidad de pendientes: {casos_pendientes}")
print(f"Provincias con pendientes: {list(provincias_pendientes)}")
print("Casos urgentes (id, minutos):")
for urgente in casos_urgentes:
    print(f"  - {urgente[0]}: {urgente[1]} min")
print(f"Caso más largo: {caso_mas_largo[0]} con {caso_mas_largo[1]} minutos")
print(f"¿Hay pendientes en San Jose?: {'Sí' if san_jose_pendiente else 'No'}")