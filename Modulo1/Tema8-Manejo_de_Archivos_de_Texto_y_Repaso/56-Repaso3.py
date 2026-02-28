# --- REPASO 3: El Bucle 'for' y 'range' ---

print("--- Tabla de Multiplicar del 7 ---")

# 'range(1, 11)' genera numeros desde el 1 hasta el 10.
# (El limite superior, 11, nunca se incluye).
for i in range(1, 11):
    
    resultado = 7 * i
    
    # En cada vuelta, 'i' vale: 1, luego 2, luego 3... hasta 10.
    print(f"7 x {i} = {resultado}")

print("\n--- Recorriendo texto ---")
palabra = "Python"
# Tambien podemos recorrer letras de un string
for letra in palabra:
    print(f"Letra: {letra}")