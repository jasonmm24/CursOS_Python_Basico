# --- 3. Herencia Basica ---

# CLASE PADRE (Superclase)
# Define lo que es comun para todos los vehiculos.
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        print(f"El {self.marca} {self.modelo} esta arrancando...")

# CLASE HIJA (Subclase)
# Ponemos (Vehiculo) entre parentesis.
# Esto significa: "Moto ES UN Vehiculo". Hereda todo su codigo.
class Moto(Vehiculo):
    
    # Metodo exclusivo de la Moto
    def hacer_caballito(self):
        print("¡La moto esta haciendo un caballito!")

# --- Uso ---
# Al crear la Moto, usamos el __init__ que heredo de Vehiculo
mi_moto = Moto("Yamaha", "R1")

# La moto tiene sus propios metodos...
mi_moto.hacer_caballito()

# ...Y TAMBIEN los metodos que "copio" de su padre.
mi_moto.arrancar()