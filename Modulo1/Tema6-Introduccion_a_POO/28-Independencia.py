# --- 10. Independencia de Objetos y Metodo Magico '__str__' ---
# OBJETIVO: Comprobar que los objetos son independientes
#           y aprender a imprimirlos de forma "bonita".

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        self.encendido = True
        
    def acelerar(self):
        if self.encendido:
            self.velocidad += 10
            
    # --- 1. DEFINICION DE __str__ (El "Sticker") ---
    #    Este metodo especial le dice a Python que DEVOLVER
    #    (return) cuando alguien intente hacer print(objeto)
    
    def __str__(self):
        # 2. LOGICA DE IMPRESION
        #    Leemos nuestros propios atributos (self)
        estado = "Encendido" if self.encendido else "Apagado"
        
        # 3. DEVOLVEMOS UN STRING
        return f"[Coche: {self.marca} {self.modelo} | Estado: {estado} | Vel: {self.velocidad} km/h]"

# --- Uso: Parte A (Independencia) ---
print("--- Probando Independencia ---")
mustang = Coche("Ford", "Mustang")
vocho = Coche("VW", "Sedan")

# Arrancamos y aceleramos SOLO EL MUSTANG
mustang.arrancar()
mustang.acelerar()

# 4. 'print(mustang)' ahora llamara a __str__
print(f"Mustang: {mustang}")
# 'print(vocho)' tambien llamara a __str__
print(f"Vocho:   {vocho}")
# Vemos que solo los atributos del mustang cambiaron.
# ¡El 'self' del mustang es diferente del 'self' del vocho!

# --- Uso: Parte B (__str__) ---
print("\n--- Probando __str__ ---")
# Si no tuvieramos __str__, esto imprimiria algo feo
# como: <__main__.Coche object at 0x10d2...>
coche_tesla = Coche("Tesla", "Model S")
print(coche_tesla)