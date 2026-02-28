# --- 5. El Bloque 'else' ---

try:
    # Codigo peligroso
    edad_str = input("¿Cuantos años tienes? ")
    edad = int(edad_str)

except ValueError:
    # Si FALLA el try...
    print("Eso no parece un numero.")

else:
    # Si el try fue EXITOSO...
    # Este bloque se ejecuta SOLO si no hubo errores.
    # Es buena practica poner aqui la logica que depende del exito del try.
    print(f"Entendido, tienes {edad} años.")
    
    if edad >= 18:
        print("Acceso permitido.")
    else:
        print("Acceso denegado.")