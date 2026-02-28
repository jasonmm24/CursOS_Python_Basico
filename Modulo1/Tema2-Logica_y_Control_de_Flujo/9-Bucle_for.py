# --- El Bucle for: Iterando sobre una lista ---

numeros = [20, 5, -8, 15, 0, 100]

print("Analizando la lista de números...")

# La variable 'numero' tomará el valor de cada elemento de la lista en cada repetición.
for numero in numeros:
    
    # Usamos un condicional DENTRO del bucle.
    if numero > 10:
        print(f"El número {numero} es mayor que 10.")
    elif numero == 0:
        print(f"El número es {numero}.")
    else:
        print(f"El número {numero} es pequeño (10 o menos).")

print("\nAnálisis completado.")

for a in range(11):
    print(a)


"""
a = 0
while a <= 10:
    print(a)
    a = a + 1
"""