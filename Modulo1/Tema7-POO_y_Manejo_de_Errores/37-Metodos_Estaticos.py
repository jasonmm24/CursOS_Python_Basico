# --- 9. Metodos Estaticos ---

class Calculadora:
    
    # @staticmethod NO recibe ni 'self' ni 'cls'.
    # Es una funcion normal que vive aqui por organizacion.
    @staticmethod
    def sumar(a, b):
        return a + b
    
    @staticmethod
    def info():
        print("Esta es una calculadora estatica simple.")

# No necesito instanciar (crear objeto) para usarlos.
# Los llamo directamente desde la Clase.
print(f"Suma: {Calculadora.sumar(10, 5)}")
Calculadora.info()