# --- Recibiendo datos del usuario con input() ---

# 1. Pedimos el nombre al usuario. Lo que se escribe se guarda en la variable.
nombre_usuario = input("Por favor, escribe tu nombre completo: ")

# 2. Pedimos el año de nacimiento.
año_nacimiento_str = input("Ahora, escribe tu año de nacimiento: ")

# 3. ¡Error común! input() devuelve texto. No podemos restar texto.
# Necesitamos convertir el año de texto a número (int).
año_nacimiento_int = int(año_nacimiento_str)

# 4. Calculamos la edad usando un operador aritmético.
año_actual = 2025
edad_calculada = año_actual - año_nacimiento_int

# 5. Mostramos un mensaje completo usando una f-string y todas las variables.
print(f"¡Hola, {nombre_usuario}! Si estamos en {año_actual}, entonces tienes o cumplirás {edad_calculada} años.")
