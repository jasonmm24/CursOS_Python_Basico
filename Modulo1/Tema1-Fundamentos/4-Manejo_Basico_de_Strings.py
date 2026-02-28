# --- Manejo Básico de Strings ---

nombre = "Pedro"
apellido = "Pascal"

# 1. Concatenación con el símbolo '+'
# Es necesario agregar el espacio " " manualmente.
nombre_y_apellido = nombre + " " + apellido
print("Nombre completo (con +):", nombre_y_apellido)

# 2. F-strings (la forma moderna y recomendada)
# Es más legible y práctico. Se pone una 'f' antes de las comillas.
# Las variables se insertan directamente dentro de llaves {}.
mensaje_bienvenida = f"Hola, bienvenido al curso {nombre}!"
print("Mensaje (sin f-string):", mensaje_bienvenida)

print(f"Mensaje (con f-string): {mensaje_bienvenida}")
