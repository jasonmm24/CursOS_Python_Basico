# --- 9. Excepciones Personalizadas (POO) ---

# 1. DEFINIR EL ERROR
#    Creamos una clase que hereda de 'Exception'.
#    Esto la convierte en un error oficial de Python.
class SaldoInsuficienteError(Exception):
    pass

class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
        
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            # 2. LANZAR EL ERROR PERSONALIZADO
            raise SaldoInsuficienteError(f"Faltan ${cantidad - self.saldo}")
        
        self.saldo -= cantidad
        print(f"Retiro exitoso. Nuevo saldo: {self.saldo}")

# --- Uso ---
try:
    mi_cuenta = CuentaBancaria(1000)
    mi_cuenta.retirar(500) # Esto fallara

# 3. ATRAPAR EL ERROR PERSONALIZADO
except SaldoInsuficienteError as e:
    print(f"¡ALERTA DE FRAUDE O FONDOS! {e}")
    print("Enviando notificacion al usuario...")