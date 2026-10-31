from sedes import sedes

# Acceso a listas de sede de emprendimientos
print("Sedes registradas:", len(sedes))
print("Primera sede:", sedes[0]["nombre"])
print("Ventas de la primera sede:", sedes[0]["ventas"])

print("\nANALISIS SEMANAL DE EMPRENDIMIENTOS")

for sede in sedes:
    total = sum(sede["ventas"])
    porcentaje = total / sede["meta"] * 100

    # Clasificación
    if porcentaje >= 100:
        estado = "Meta Alcanzada"
    elif porcentaje >= 80:
        estado = "Cerca de la meta"
    else:
        estado = "Requiere atención"

    print(
        f"{sede['nombre']} | Total:{total:,.2f} | "
        f"Cumplimiento: {porcentaje:.2f}% | {estado}"
    )