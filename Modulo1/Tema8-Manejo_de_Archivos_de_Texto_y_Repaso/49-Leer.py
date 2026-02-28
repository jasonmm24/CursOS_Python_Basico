# --- CODIGO 2: Lectura Completa (Modo 'r') ---

print("Intentando leer el archivo...\n")

try:
    # 1. Abrimos en modo 'r' (Lectura).
    #    Si el archivo no existe, esto lanzara un error FileNotFoundError.
    with open("Ensayo_Escuela_Botes.txt", "r", encoding="utf-8") as archivo:
        
        # 2. Leemos todo el contenido de una sola vez.
        contenido_completo = archivo.read()
        
        print("--- INICIO DEL ARCHIVO ---")
        print(contenido_completo)
        print("--- FIN DEL ARCHIVO ---")

except FileNotFoundError:
    print("Error: El archivo no existe. Asegurate de haber ejecutado el Codigo 1 primero.")