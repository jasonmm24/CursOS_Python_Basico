# --- REPASO 6: Diccionarios ---

# Definimos un diccionario con datos de un estudiante
estudiante = {
    "nombre": "Ana Lopez",      # Clave: "nombre", Valor: "Ana Lopez"
    "matricula": "A00123",
    "promedio": 9.5,
    "activo": True
}

# 1. Acceder a un valor usando su CLAVE
print(f"Estudiante: {estudiante['nombre']}")
print(f"Promedio: {estudiante['promedio']}")

# 2. Modificar un valor
estudiante["promedio"] = 9.8

# 3. Agregar un NUEVO par clave-valor
estudiante["carrera"] = "Ingeniería"

# 4. Ver el diccionario completo
print("Datos actualizados:", estudiante)