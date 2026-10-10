"""Microreto: el portero del café"""

nombre = input("¿Cómo te llamas?: ").strip()

# Validación simple para que la energía sea un número válido
try:
    energia = int(input(f"Hola {nombre}, ¿cuánta energía tienes de 0 a 100?: "))
except ValueError:
    energia = -1  # Valor por defecto si ingresan letras

# Limpiar entrada de café
trae_cafe_input = input("¿Traes café? (si / no): ").lower().strip()
trae_cafe = (trae_cafe_input == "si")

mensaje = ""

# Reglas estrictas del microreto
if energia < 0 or energia > 100:
    mensaje = "-> Error: Energía inválida (debe ser entre 0 y 100)"
elif energia < 30 and not trae_cafe:
    mensaje = "-> Resultado: Mensaje de apoyo (Energía baja y sin café)"
elif energia >= 30 or trae_cafe:
    mensaje = "-> Resultado: Bienbenido Acceso permitido"
else:
    mensaje = "-> Resultado: Verifique los datos"

print(mensaje)