print("\n--- 2. Tuplas ---")
print("Son listas que NO SE PUEDEN MODIFICAR (inmutables). Se usan parentesis ().\n")

# 1. Creacion de una tupla.
# Se usa a menudo para datos fijos: coordenadas (X, Y), colores (R, G, B), etc.
coordenadas_gps = (40.7128, -74.0060)

# 2. Acceder a los valores (igual que las listas, con indices).
print(f"Latitud: {coordenadas_gps[0]}")
print(f"Longitud: {coordenadas_gps[1]}")

# 3. Desempaquetado de tuplas (una forma muy comun de asignar variables).
latitud, longitud = coordenadas_gps
print(f"Latitud desempaquetada: {latitud}")

print(f"Longitud desempaquetada: {longitud}")

# 4. Intento de modificacion (¡Esto dara un error!)
# Si descomentas la siguiente linea, el programa fallara.

coordenadas_gps[0] = 50.0 
# Genera: TypeError: 'tuple' object does not support item assignment