# --- 2. Errores Especificos (ValueError) ---

print("--- Conversor de Texto a Numero ---")

try:
    numero_texto = input("Ingresa un numero entero: ")
    
    # Esto fallara si el usuario escribe letras (ej. "hola")
    numero = int(numero_texto)
    
    print(f"El numero mas 10 es: {numero + 10}")

# 1. EXCEPT ESPECIFICO
#    En lugar de un 'except' vacio, especificamos 'ValueError'.
#    Esto solo atrapara errores de conversion de tipos.
#    Si ocurre otro tipo de error (ej. division por cero), este except NO lo atrapara.
except ValueError:
    print(f"ERROR: '{numero_texto}' no es un numero valido.")
    print("Por favor, usa digitos del 0 al 9.")