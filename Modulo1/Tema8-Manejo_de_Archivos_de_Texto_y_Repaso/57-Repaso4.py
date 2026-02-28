# --- REPASO 4: El Bucle 'while' (Validación) ---

contrasena_secreta = "1234"
intento = ""

# El bucle se repetira MIENTRAS el intento sea DIFERENTE a la contraseña.
while intento != contrasena_secreta:
    
    intento = input("Introduce la contraseña: ")
    
    if intento != contrasena_secreta:
        print("Contraseña incorrecta. Intenta de nuevo.")

# Esta linea solo se ejecuta cuando el bucle termina (condicion falsa).
print("¡Acceso Concedido!")