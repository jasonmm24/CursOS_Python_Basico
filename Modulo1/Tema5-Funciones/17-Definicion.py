import numpy as np
#from numpy import divide

print("\n--- 1. Funciones (def) ---")

# 1. DEFINICION de una funcion simple.
# 'def' es la palabra clave para 'definir' una funcion.
def saludar():
    print("¡Hola! Voy a dividir.")

# 2. 'Llamar' a la funcion para que se ejecute.
print("Llamando a la funcion 'saludar':")
saludar()


print("\n--- 2. Funciones con PARAMETROS ---")

# 1. 'nombre_usuario' es un 'parametro' (una variable que la funcion espera recibir).
def saludar_a_alguien(nombre_usuario):
    print(f"¡Hola, {nombre_usuario}! Que tengas un buen dia.")
    
# 2. 'Llamamos' a la funcion y le pasamos un 'argumento' ("Maria").
# "Maria" se copia dentro de la variable 'nombre_usuario'.
saludar_a_alguien("Maria")
saludar_a_alguien(1)


print("\n--- 3. Funciones que DEVUELVEN un valor (return) ---")

# 1. Esta funcion NO imprime nada. Procesa datos y 'devuelve' un resultado.
def sumar_numeros(num1, num2):
    total = num1 + num2
    # 'return' es la palabra clave para enviar un valor de vuelta.
    return total

# 2. Llamamos a la funcion y guardamos el valor devuelto en una variable.
resultado_suma = sumar_numeros(10, 5)

print(f"El resultado de sumar 10 + 5 es: {resultado_suma}")
print(f"El doble del resultado es: {resultado_suma * 2}")

# Tambien podemos usarla directamente
print(f"3 + 8 es: {sumar_numeros(3, 8)}")

def division(dividendo, divisor):
    saludar()
    resultado = np.divide(dividendo, divisor)

    return resultado

resultado_division = division(10, 2)

print(f"El resultado de la division es: {resultado_division}")