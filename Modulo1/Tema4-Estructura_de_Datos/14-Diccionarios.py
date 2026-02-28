print("\n--- 1. Diccionarios (dict) ---")
print("Se usan para guardar datos con una 'clave' y un 'valor'.\n")

# 1. Creacion de un diccionario.
# Usamos llaves {}. Las claves suelen ser strings (texto).
estudiante = {
    "nombre": "Ana",
    "edad": 22,
    "curso": "Python de 0 a GUI",
    "esta_activa": True
}

#*como eliminar elementos
# 2. Acceder a un valor usando su clave (con corchetes []).
print(f"Nombre del estudiante: {estudiante['nombre']}")
print(f"Edad: {estudiante['edad']}")

# 3. Modificar un valor existente.
estudiante["edad"] = 23
print(f"Edad actualizada: {estudiante['edad']}")

# 4. Agregar un nuevo par clave-valor.
estudiante["promedio"] = 9.5
print(f"Diccionario con nuevo dato: {estudiante}")

# 5. Recorrer un diccionario con un bucle 'for' (usando .items()).
print("\nRecorriendo el diccionario:")
for clave, valor in estudiante.items():
    print(f"  - Clave: {clave}, Valor: {valor}")

#*
estudiante2 = {}
estudiante = estudiante2
estudiante2["nombre"] = "Juan"
