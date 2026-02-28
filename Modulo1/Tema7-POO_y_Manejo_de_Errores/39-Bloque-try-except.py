# --- 1. Bloque Basico try-except ---

print("--- Inicio del programa ---")

# 1. BLOQUE TRY (INTENTAR)
#    Aqui colocamos el codigo "peligroso" o propenso a fallar.
#    Python intentara ejecutarlo linea por linea.
try:
    print("Intentando dividir por cero...")
    resultado = 10 / 2
    # Esta linea NO se ejecutara porque la anterior falla.
    print(f"El resultado es: {resultado}")

# 2. BLOQUE EXCEPT (EXCEPCION)
#    Este bloque es la "red de seguridad".
#    Si OCURRE un error dentro del 'try', Python salta inmediatamente aqui.
#    Si NO ocurre error, este bloque se ignora.
except:
    print("¡ALERTA! Ocurrio un error y lo hemos atrapado.")
    print("No se puede dividir entre cero.")

# 3. FLUJO CONTINUO
#    Gracias al try-except, el programa NO se cierra de golpe (crash).
print("--- Fin del programa (El programa sobrevivio) ---")