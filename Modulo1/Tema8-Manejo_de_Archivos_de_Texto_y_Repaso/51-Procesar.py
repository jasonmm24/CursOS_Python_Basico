# --- CODIGO 4: Procesar linea por linea (Recomendado) ---

print("Analizando el archivo linea por linea...\n")

with open("Ensayo_Escuela_Botes.txt", "r", encoding="utf-8") as archivo:
    
    numero_linea = 1
    
    # 1. El objeto 'archivo' es "iterable".
    #    Podemos usar un for para recorrerlo renglon por renglon.
    for linea in archivo:
        
        # 2. Limpieza de texto (.strip())
        #    Cada linea leida trae un caracter invisible de "Enter" al final.
        #    .strip() elimina espacios y Enters sobrantes.
        linea_limpia = linea.strip()
        
        # 3. Solo imprimimos si la linea tiene contenido
        if linea_limpia:
            print(f"Renglon {numero_linea}: {linea_limpia}")
        
        numero_linea += 1

print("\nAnalisis terminado.")