# --- REPASO 5: Manejo de Listas ---

# 1. Creacion de una lista vacia
carrito_compras = []

# 2. Agregar elementos (.append)
print("Agregando productos...")
carrito_compras.append("Leche")
carrito_compras.append("Huevos")
carrito_compras.append("Pan")

# 3. Acceso por Indice (Posicion)
#    Recuerda: Los indices empiezan en 0.
print(f"El primer producto es: {carrito_compras[0]}") # Leche

# 4. Modificar un elemento
carrito_compras[1] = "Huevos Organicos" # Cambiamos 'Huevos'

# 5. Eliminar un elemento (.remove)
carrito_compras.remove("Pan")

print(f"Carrito final: {carrito_compras}")