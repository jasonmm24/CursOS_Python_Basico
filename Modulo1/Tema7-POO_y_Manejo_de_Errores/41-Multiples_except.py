# --- 3. Multiples 'except' ---

try:
    # Aqui pueden pasar DOS cosas malas:
    val1 = int(input("Introduce el dividendo: ")) # Error 1: Escribir letras
    val2 = int(input("Introduce el divisor: "))   # Error 1: Escribir letras
    
    res = val1 / val2                             # Error 2: Dividir por 0
    print(f"Resultado: {res}")

# CASO A: El usuario no escribio numeros
except ValueError:
    print("ERROR DE VALOR: Solo se permiten numeros enteros.")

# CASO B: El usuario intento dividir por cero
except ZeroDivisionError:
    print("ERROR MATEMATICO: No puedes dividir entre cero.")

# CASO C: Cualquier otro error inesperado (Comodin)
except Exception:
    print("ERROR DESCONOCIDO: Algo salio mal, pero no se que fue.")