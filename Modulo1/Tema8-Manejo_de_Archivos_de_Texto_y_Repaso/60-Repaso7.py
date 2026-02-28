# --- REPASO 7: Funciones y Retorno de Valores ---

# Definimos la funcion 'calcular_area' que espera 2 parametros.
def calcular_area(base, altura):
    """Calcula el area de un rectangulo."""
    area = base * altura
    return area  # Devolvemos el resultado al programa principal

# --- Programa Principal ---
print("Calculadora de Areas")

b = 10
h = 5

# Llamamos a la funcion y GUARDAMOS lo que nos devuelve en 'resultado'.
resultado = calcular_area(b, h)

print(f"Un rectangulo de {b}x{h} tiene area de: {resultado}")

# Podemos reutilizarla
print(f"Area de 2x2: {calcular_area(2, 2)}")