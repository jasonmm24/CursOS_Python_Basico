# --- CODIGO 1: Escribir un archivo nuevo (Modo 'w') ---

# 1. Definimos el nombre del archivo
nombre_archivo = "Ensayo_Escuela_Botes.txt"

print(f"Creando el archivo '{nombre_archivo}'...")

# 2. Usamos 'with open(...)'.
#    - 'w': Write (Escribir).
#    - encoding='utf-8': VITAL para soportar acentos y ñ en español.
#    - 'as archivo': Creamos una variable temporal para manipular el fichero.
with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
    #archivo.write("HOLA")
    # 3. Escribimos lineas de texto.
    #    ¡OJO! .write() no agrega el 'Enter' automaticamente.
    #    Debemos agregar '\n' al final de cada linea.
    archivo.write("Lo que aprendi en la escuela de botes fue...\n")
    archivo.write("The...\n")

# 4. Al salir del bloque 'with', el archivo se GUARDA y se CIERRA solo.
print("¡Archivo escrito exitosamente!")