# --- 7. Metodos (Las Acciones) ---
# OBJETIVO: Definir el *comportamiento* (lo que el objeto puede HACER).

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    # --- 1. DEFINICION DE UN METODO ---
    #    Un "metodo" es simplemente una funcion 'def' que
    #    esta *dentro* de una clase.
    #
    #    Siempre recibe 'self' como primer parametro, para que
    #    el metodo sepa *cual* de los objetos (mustang o vocho)
    #    es el que esta realizando la accion.
    def tocar_claxon(self):
        # 2. USA 'self' PARA ACCEDER A SUS PROPIOS DATOS
        #    Usa 'self.marca' para saber su propia marca.
        print(f"El {self.marca} {self.modelo} hace: ¡Beep Beep!")
        
    def describir(self):
        print(f"Soy un {self.marca} {self.modelo}.")

# --- Creacion y Uso ---
mi_mustang = Coche("Ford", "Mustang")
mi_vocho = Coche("VW", "Sedan")

# --- 3. LLAMADA AL METODO ---
#    Usamos la notacion de punto (objeto.metodo()) para
#    "ordenarle" al objeto que ejecute su accion.
#
#    mi_mustang.describir() --> Python lo traduce a: Coche.describir(self=mi_mustang)
mi_mustang.describir()

#    mi_vocho.tocar_claxon() --> Python lo traduce a: Coche.tocar_claxon(self=mi_vocho)
mi_vocho.tocar_claxon()