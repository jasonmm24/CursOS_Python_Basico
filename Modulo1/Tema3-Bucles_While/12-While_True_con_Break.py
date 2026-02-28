print("\n--- Ejemplo 2: 'while True' con 'break' ---")
print("Este bucle se repetira hasta que escribas 'salir'.")

# 1. Un bucle 'while True' esta disenado para ejecutarse infinitamente...
while True:
    
    # 2. ...hasta que una condicion interna se cumpla y ejecutemos 'break'.
    texto = input("Escribe algo (o 'salir' para terminar): ")
    
    # 3. Verificamos la condicion de salida
    if texto == "salir":
        print("¡Detectada la palabra 'salir'!")
        break # Esta instruccion "rompe" el bucle y sale de el.
    
    # 4. Este codigo solo se ejecuta si el 'break' no ocurrio.
    print(f"Escribiste esto: {texto}")

print("Programa terminado.")