# --- 10. Integracion: Menu Robusto ---

def division_segura(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None # Devolvemos un valor especial si falla

def main():
    while True:
        print("\n--- Calculadora Robusta ---")
        print("1. Dividir dos numeros")
        print("2. Salir")
        
        opcion = input("Opcion: ")
        
        if opcion == "1":
            # TRY GRANDE para atrapar errores de input
            try:
                n1 = float(input("Numerador: "))
                n2 = float(input("Denominador: "))
                
                resultado = division_segura(n1, n2)
                
                if resultado is None:
                    print("Error: No se puede dividir por cero.")
                else:
                    print(f"Resultado: {resultado:.2f}")
                
            except ValueError:
                print("Error: Debes escribir numeros, no letras.")
                
        elif opcion == "2":
            print("Adios.")
            break
        else:
            print("Opcion no reconocida.")
            
        input()

if __name__ == "__main__":
    main()