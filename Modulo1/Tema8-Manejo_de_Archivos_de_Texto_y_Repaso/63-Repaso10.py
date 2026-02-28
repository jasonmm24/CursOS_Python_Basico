# --- REPASO 10: Escritura y Lectura de Archivos ---

nombre_archivo = "bitacora.txt"

# --- ESCRITURA (Modo 'w' - Write) ---
# 'with' se encarga de abrir y CERRAR el archivo automaticamente.
with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write("Registro de eventos del sistema.\n")
    archivo.write("Evento 1: Inicio de sesion correcto.\n")
    archivo.write("Evento 2: Datos guardados.\n")

print(f"Datos escritos en '{nombre_archivo}'.")

# --- LECTURA (Modo 'r' - Read) ---
print("\nLeyendo el archivo guardado:")

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        # Recorremos linea por linea para ser eficientes
        for linea in archivo:
            # .strip() quita los espacios y saltos de linea sobrantes
            print(f"> {linea.strip()}")
            
except FileNotFoundError:
    print("El archivo no existe.")