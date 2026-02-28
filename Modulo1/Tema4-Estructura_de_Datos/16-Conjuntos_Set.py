print("\n--- 3. Conjuntos (set) ---")
print("Son colecciones SIN ORDEN y SIN ELEMENTOS REPETIDOS. Se usan llaves {}.\n")

# 1. Creacion de un conjunto a partir de una lista con duplicados.
lista_invitados = ["Ana", "Juan", "Pedro", "Ana", "Maria", "Juan"]
print(f"Lista original: {lista_invitados}")

# 2. Al convertirla a 'set', los duplicados se eliminan automaticamente.
invitados_unicos = set(lista_invitados)
print(f"Invitados unicos (set): {invitados_unicos}") # El orden puede variar

# 3. Agregar un elemento con .add()
invitados_unicos.add("Luis")
invitados_unicos.add("Ana") # 'Ana' ya existe, el set no cambia.
print(f"Set actualizado: {invitados_unicos}")

# 4. Comprobar si un elemento existe (es mucho mas rapido que en las listas).
print(f"¿Esta 'Pedro' en el set? {'Pedro' in invitados_unicos}")
print(f"¿Esta 'Miguel' en el set? {'Miguel' in invitados_unicos}")