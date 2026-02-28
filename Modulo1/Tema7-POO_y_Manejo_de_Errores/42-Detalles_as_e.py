# --- 4. Obteniendo detalles tecnicos (as e) ---

lista_frutas = ["Manzana", "Banana", "Pera"] # Indices: 0, 1, 2

try:
    indice = int(input("Elige un indice de fruta (0-2): "))
    print(f"Elegiste: {lista_frutas[indice]}")

# 'Exception' es la clase madre de todos los errores.
# 'as e' guarda el objeto del error en la variable 'e'.
except Exception as e:
    print("\n--- REPORTE DE ERROR ---")
    print("¡Ups! Algo fallo.")
    # Imprimimos 'e' para ver que dice Python internamente
    print(f"Mensaje Tecnico: {e}") 
    # Ejemplo: Si pones indice 10, 'e' dira: "list index out of range"
    print(f"Tipo de error: {type(e).__name__}")