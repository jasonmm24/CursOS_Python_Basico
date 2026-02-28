# --- 5. Atributos (Datos) y 'self' ---
# OBJETIVO: Entender como guardar datos (estado) DENTRO del objeto.

class Coche:
    def __init__(self):
        print("Ensamblando coche...")
        
        # 1. ATRIBUTOS (Variables del objeto)
        #    'self' es el objeto que se esta creando.
        #    Al hacer 'self.marca', le estamos "pegando" una variable
        #    llamada 'marca' a ESE objeto en especifico.
        #    Estos son los "atributos" o el "estado" del objeto.
        self.marca = "Marca Generica"
        self.color = "Blanco"
        self.encendido = False # Estado inicial
    
    def arrancar(self):
        self.encendido = True

# --- Creacion y Uso ---
mi_coche = Coche() # Se ejecuta __init__ y se crean los atributos

# 2. LECTURA DE ATRIBUTOS
#    Usamos la "notacion de punto" (objeto.atributo) para
#    leer los datos que estan guardados dentro del objeto.
print(f"\nLa marca de mi coche es: {mi_coche.marca}")
print(f"¿Esta encendido? {mi_coche.encendido}")

# 3. ESCRITURA DE ATRIBUTOS
#    Tambien podemos cambiar el valor de esos atributos.
mi_coche.color = "Rojo"
print(f"El coche fue pintado de: {mi_coche.color}")

print(f"Arrancando coche")
mi_coche.arrancar()
print(f"¿Esta encendido? {mi_coche.encendido}")