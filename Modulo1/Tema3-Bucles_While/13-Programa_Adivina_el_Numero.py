# 1. Importamos el modulo 'random' para poder generar numeros aleatorios.
#import random as rd
from random import randint

print("\n--- Programa1: ¡Adivina el Numero (del 1 al 20)! ---")
print("He pensado un numero entre 1 y 20. ¿Puedes adivinar cual es?")

# 2. Generamos un numero aleatorio entero entre 1 y 20 (inclusive).
# Este es el numero que el usuario debe adivinar.
numero_secreto = randint(1, 100)

# 3. Inicializamos la variable 'intento' en 0 (o cualquier valor
#    que no sea el numero_secreto) para asegurar que el bucle comience.
intento = 0

# 4. El bucle 'while' se repetira MIENTRAS el intento del usuario
#    sea DIFERENTE (!=) al numero secreto.
while intento != numero_secreto:
    
    # 5. Pedimos un numero al usuario y lo convertimos a entero (int).
    intento = int(input("Introduce tu numero: "))
    
    # 6. Usamos condicionales 'if/elif/else' para dar pistas al usuario.
    if intento < numero_secreto:
        print("¡Muy bajo! Intenta un numero mas grande.")
    elif intento > numero_secreto:
        print("¡Muy alto! Intenta un numero mas pequeño.")
        
# 7. Si el codigo llega a esta linea, es porque el 'while' termino.
#    Eso solo ocurre cuando la condicion (intento != numero_secreto) es Falsa.
#    (Es decir, cuando 'intento' es IGUAL a 'numero_secreto').
print(f"\n¡Felicidades! 🎉 Has adivinado el numero secreto: {numero_secreto}")