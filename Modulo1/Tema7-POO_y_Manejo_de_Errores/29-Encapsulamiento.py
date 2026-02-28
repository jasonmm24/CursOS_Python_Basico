# --- 1. Encapsulamiento (Privado vs Publico) ---

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        # 1. ATRIBUTO PUBLICO
        #    Se puede acceder y modificar libremente desde fuera.
        self.titular = titular
        
        # 2. ATRIBUTO PRIVADO (__)
        #    Al poner doble guion bajo al inicio, Python "esconde" esta variable.
        #    No se puede acceder directamente como 'objeto.__saldo'.
        self.__saldo = saldo_inicial

    def ver_saldo(self):
        # 3. ACCESO INTERNO
        #    Dentro de la clase, SI podemos ver el atributo privado.
        #    Este metodo actua como una "ventana" controlada para ver el saldo.
        return self.__saldo

# --- Uso ---
cuenta = CuentaBancaria("Ana", 1000)

print(f"Titular: {cuenta.titular}")  # Funciona (es publico)

# print(cuenta.__saldo) 
# ERROR: AttributeError. Python dice "No se de que me hablas", protegiendo el dato.

# Forma correcta: Usamos el metodo publico que creamos
print(f"Saldo: {cuenta.ver_saldo()}")