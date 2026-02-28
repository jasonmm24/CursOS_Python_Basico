print("--- Ejemplo 1: Bucle 'while' simple (Contador) ---")

# 1. Inicializamos una variable 'contador' en 0.
# Esta variable controlara la condicion del bucle.
contador = 0

# 2. El bucle 'while' se ejecutara MIENTRAS la condicion (contador < 5) sea Verdadera.
while contador < 5:
    print(f"El contador vale: {contador}")
    
    # 3. IMPORTANTE: Debemos modificar la variable de condicion dentro del bucle.
    # Si olvidamos esta linea, (contador < 5) siempre sera verdadero
    # y crearemos un bucle infinito.
    contador = contador + 1 # Tambien se puede escribir: contador += 1

print(f"El bucle ha terminado. El contador final es: {contador}")