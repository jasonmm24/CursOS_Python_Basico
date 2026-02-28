# --- 6. '__init__' con Parametros ---
# OBJETIVO: Hacer que cada objeto sea unico desde su creacion.

class Coche:
    
    # 1. PARAMETROS DE ENTRADA
    #    Ademas de 'self' (que es automatico), ahora pedimos
    #    'marca_input' y 'modelo_input' como argumentos.
    def __init__(self, marca_input, modelo_input):
        print(f"¡Ensamblando un {marca_input} {modelo_input}!")
        
        # 2. ASIGNACION
        #    Usamos los valores recibidos para ASIGNARLOS
        #    a los atributos (self.marca) del objeto.
        self.marca = marca_input
        self.modelo = modelo_input
        self.encendido = False # Estado inicial por defecto

# --- Creacion ---
# 3. ARGUMENTOS
#    Ahora, debemos pasar los "argumentos" al crear el objeto.
#    Python los hace coincidir:
#    Coche("Ford", "Mustang") --> __init__(self=mi_mustang, marca_input="Ford", modelo_input="Mustang")
mi_mustang = Coche("Ford", "Mustang")

#    Coche("VW", "Sedan") --> __init__(self=mi_vocho, marca_input="VW", modelo_input="Sedan")
mi_vocho = Coche("VW", "Sedan")

# --- Verificacion ---
print(f"\nCoche 1: {mi_mustang.marca} {mi_mustang.modelo}")
print(f"Coche 2: {mi_vocho.marca} {mi_vocho.modelo}")

marca_usuario = input("Dame la Marca de tu carro: ")
modelo_usuario = input("Dame el Modelo: ")

carro = Coche(marca_usuario, modelo_usuario)

print(f"Tu carro es: {carro.marca} {carro.modelo}")

#Como ver todos mis objetos