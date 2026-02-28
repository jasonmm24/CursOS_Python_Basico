# --- 9. Metodos que Interactuan (Abstraccion) ---
# OBJETIVO: Ver como los metodos trabajan juntos y
#           esconden la complejidad.

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0 # Nuevo atributo de estado

    def arrancar(self):
        self.encendido = True
        print(f"El {self.modelo} arranca.")
        
    def acelerar(self):
        # 1. LECTURA DE ESTADO (Abstraccion)
        #    Este metodo "lee" el atributo 'self.encendido'.
        #    El usuario no necesita saber esto, solo pisa el "pedal".
        if self.encendido:
            # 2. MODIFICACION DE OTRO ESTADO
            self.velocidad += 10
            print(f"El {self.modelo} acelera a {self.velocidad} km/h")
        else:
            # 3. ACCION ALTERNATIVA
            print(f"No puedes acelerar. El {self.modelo} esta apagado.")
            
    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 5
            print(f"Frenando... {self.velocidad} km/h")
        else:
            print(f"El {self.modelo} esta parado")

# --- Uso ---
mi_coche = Coche("Chevy", "Pop")

mi_coche.acelerar() # Falla, porque self.encendido es False
mi_coche.arrancar() # Cambia self.encendido a True
mi_coche.acelerar() # Funciona, porque self.encendido es True
mi_coche.acelerar() # Aumenta mas
mi_coche.frenar()