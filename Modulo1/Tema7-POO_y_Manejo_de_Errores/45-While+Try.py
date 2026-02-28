# --- 7. Validacion Robusta (While + Try) ---

def pedir_entero_seguro():
    # Bucle infinito: No te dejo salir hasta que me des un numero.
    while True:
        try:
            entrada = input("Introduce un numero entero: ")
            numero = int(entrada)
            
            # Si llegamos a esta linea, es que int() funciono bien.
            return numero # 'return' rompe el bucle y devuelve el valor.
            
        except ValueError:
            # Si int() falla, caemos aqui.
            print(f"'{entrada}' no es valido. Intentalo de nuevo.")

# --- Uso ---
print("Necesito tu edad para continuar.")
edad = pedir_entero_seguro()
print(f"¡Gracias! Edad registrada: {edad}")