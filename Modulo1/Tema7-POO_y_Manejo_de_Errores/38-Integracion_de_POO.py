# --- 10. Sistema de Pagos (Integracion) ---
from abc import ABC, abstractmethod

# 1. ABSTRACCION:
#    Definimos la regla: Todo metodo de pago debe saber 'pagar'.
class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, cantidad):
        pass

# 2. HERENCIA:
#    Creamos implementaciones concretas.
class PayPal(MetodoPago):
    def __init__(self, email):
        self.email = email 
        
    # 3. POLIMORFISMO:
    #    PayPal paga de una forma...
    def pagar(self, cantidad):
        print(f"Procesando pago de ${cantidad} via PayPal ({self.email})... Exito.")

class TarjetaCredito(MetodoPago):
    def __init__(self, numero):
        self.numero = numero
        
    #    ...y la Tarjeta paga de otra forma distinta.
    def pagar(self, cantidad):
        print(f"Cargando ${cantidad} a Tarjeta *{self.numero[-4:]}... Aprobado.")

# 4. LOGICA DEL NEGOCIO
class Tienda:
    # Recibe CUALQUIER cosa que sea un MetodoPago (Polimorfismo)
    def cobrar_producto(self, metodo_pago, precio):
        print("--- Iniciando compra ---")
        metodo_pago.pagar(precio)
        print("--- Compra finalizada ---\n")

# --- EJECUCION ---
mi_paypal = PayPal("juan@mail.com")
mi_tarjeta = TarjetaCredito("1234567812349999")

tienda = Tienda()

# La tienda usa la misma funcion, pero el resultado cambia segun el objeto
tienda.cobrar_producto(mi_paypal, 500)
tienda.cobrar_producto(mi_tarjeta, 1200)