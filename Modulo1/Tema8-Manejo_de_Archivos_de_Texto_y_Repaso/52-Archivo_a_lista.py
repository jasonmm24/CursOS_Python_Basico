# --- CODIGO 5: De Archivo a Lista y viceversa ---

nombre = "lista_compras.txt"

# --- PASO 1: Crear una lista y guardarla en archivo ---
compras = ["Manzanas", "Leche", "Pan", "Huevos"]

print(f"Guardando lista: {compras}")

with open(nombre, "w", encoding="utf-8") as f:
    for item in compras:
        f.write(f"{item}\n") # Importante agregar \n

# --- PASO 2: Leer el archivo y convertirlo de nuevo a lista ---
lista_recuperada = []

with open(nombre, "r", encoding="utf-8") as f:
    # .readlines() lee todo y devuelve una LISTA de strings
    lineas = f.readlines()
    
    for linea in lineas:
        # Quitamos el \n y agregamos a nuestra lista limpia
        lista_recuperada.append(linea.strip())

print(f"Lista recuperada desde el disco: {lista_recuperada}")

# Verificamos que es una lista real
print(f"El segundo elemento es: {lista_recuperada[1]}")