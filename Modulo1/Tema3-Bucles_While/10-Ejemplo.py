import numpy as np

def Suma(a, b):
    return np.add(a,b)

def Resta(a, b):
    return a - b

def Multiplicacion(a, b):
    return a * b

def Division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b

while True:
    print("  Calculadora \n")
    print("1.- Suma \n2.- Resta \n3.- Multiplicacion \n4.- Division \n5.- Salir")
    opcion = input("Selecciona la operacion que quieres hacer: ")

    if opcion == '5':
        print("Saliendo de la calculadora.")
        break

    elif opcion in ('1', '2', '3', '4'):
        #*
        try:
            a = float(input("Dame el primer numero: "))
            b = float(input("Dame el segundo numero: "))
        
        except ValueError:
            print("\nError: Entrada invalida. Debes introducir solo numeros.\n")
            continue

        if opcion == '1':
            print(f"Resultado: La suma de {a} y {b} es: {Suma(a, b)}")
        
        elif opcion == '2':
            print(f"Resultado: La resta de {a} y {b} es: {Resta(a, b)}")

        elif opcion == '3':
            print(f"Resultado: La multiplicacion de {a} y {b} es: {Multiplicacion(a, b)}")

        elif opcion == '4':
            print(f"Resultado: La división de {a} y {b} es: {Division(a, b)}")

    else:
        print("\nOpción no válida. Por favor, elige un número del 1 al 5.\n")
    
    input("\n")