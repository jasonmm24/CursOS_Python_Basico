# --- REPASO 9: Programa Robusto ---

print("--- Division Segura ---")

while True:
    try:
        # Codigo "Peligroso" (puede fallar)
        numerador = int(input("Ingresa el numerador: "))
        denominador = int(input("Ingresa el denominador: "))
        
        resultado = numerador / denominador
        print(f"El resultado es: {resultado}")
        
        # Si llegamos aqui, todo salio bien, rompemos el bucle
        break 

    except ValueError:
        # Atrapa errores si el usuario escribe letras
        print("⚠️ Error: Debes ingresar numeros enteros, no letras.")
        
    except ZeroDivisionError:
        # Atrapa el error matematico de dividir entre 0
        print("⚠️ Error: No puedes dividir entre cero.")

print("Programa finalizado correctamente.")