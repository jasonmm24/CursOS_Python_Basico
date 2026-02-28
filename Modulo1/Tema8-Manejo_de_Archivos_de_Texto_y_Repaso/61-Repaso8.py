# --- REPASO 8: Clases y Objetos ---

# 1. EL MOLDE (Clase)
class Gato:
    # El Constructor: Se ejecuta al crear el objeto.
    # 'self' es la referencia al objeto que se esta creando.
    def __init__(self, nombre, color):
        self.nombre = nombre  # Atributo
        self.color = color    # Atributo

    # Metodo (Accion)
    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")

# 2. LOS OBJETOS (Instancias)
mi_gato = Gato("Felix", "Negro")
tu_gato = Gato("Pelusa", "Blanco")

# 3. USAR LOS OBJETOS
print(f"Mi gato es {mi_gato.nombre} y es color {mi_gato.color}")
mi_gato.maullar() # Felix maulla

print(f"Tu gato es {tu_gato.nombre}")
tu_gato.maullar() # Pelusa maulla