# --- Métodos y Slicing de Listas ---

frutas = ["manzana", "banana", "cereza", "naranja"]

# Usamos el método .append() para agregar un nuevo elemento al FINAL de la lista.
frutas.append("uva")
print(f"Después de usar .append('uva'), la lista 'frutas' es: {frutas}")

# El "slicing" nos permite obtener una porción de la lista 'frutas'.
# Sintaxis -> lista[inicio:fin] (el 'fin' no se incluye)
# Aquí creamos la variable 'dos_frutas_del_medio' a partir de 'frutas'.
dos_frutas_del_medio = frutas[1:3] # Del índice 1 hasta ANTES del índice 3.
print(f"La nueva lista 'dos_frutas_del_medio' contiene: {dos_frutas_del_medio}")

# Si omites el inicio, comienza desde el principio.
primeras_dos_frutas = frutas[:2]
print(f"Las primeras dos frutas: {primeras_dos_frutas}")
