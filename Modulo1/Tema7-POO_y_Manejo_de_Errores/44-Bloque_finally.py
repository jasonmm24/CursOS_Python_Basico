# --- 6. El Bloque 'finally' ---

try:
    print("1. Abriendo conexion a la base de datos...")
    # Simulamos una operacion que falla
    x = 10 / 0 
    print("2. Guardando datos...") # Esto nunca pasara

except ZeroDivisionError:
    print("3. ¡Error! La operacion fallo.")

finally:
    # ESTE BLOQUE ES SAGRADO.
    # Se ejecuta SIEMPRE, falle o no falle el programa.
    # Se usa para "limpiar el desastre" (cerrar archivos, desconectar, etc).
    print("4. Cerrando conexion y liberando recursos...")

print("5. Fin del proceso.")