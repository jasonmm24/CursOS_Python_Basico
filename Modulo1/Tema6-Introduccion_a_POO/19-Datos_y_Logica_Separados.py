# --- 1. El "Modo Antiguo" (Datos y Logica Separados) ---
# OBJETIVO: Entender por que existe la POO.

# 1. LOS DATOS: Guardamos el "estado" de un coche en un diccionario.
#    'encendido' es un "atributo" o "estado".
coche_1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "encendido": False
}

# 2. LA LOGICA: Creamos una funcion "suelta" que debe RECIBIR
#    el diccionario de datos para poder modificarlo.
def arrancar_coche(coche):
    # La funcion lee el estado del diccionario
    if not coche["encendido"]:
        # La funcion modifica el estado del diccionario
        coche["encendido"] = True
        print(f"El {coche['marca']} {coche['modelo']} ha arrancado.")
    else:
        print("El coche YA estaba encendido.")

# --- 3. USO ---
print(f"¿Coche 1 encendido? {coche_1['encendido']}")
arrancar_coche(coche_1) # Le "pasamos" los datos a la logica
print(f"¿Coche 1 encendido? {coche_1['encendido']}")

# PROBLEMA: Los datos (coche_1) y la logica (arrancar_coche)
# estan separados. La POO los *une* en un solo paquete.