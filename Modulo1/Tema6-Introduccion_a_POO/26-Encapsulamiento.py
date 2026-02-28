# --- 8. Metodos que Modifican Atributos (Encapsulamiento) ---
# OBJETIVO: Entender como un objeto maneja su propio estado interno.

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        # 1. Este es el "Estado" interno del objeto
        self.encendido = False 

    # 2. METODO DE INTERFAZ (El "Boton")
    #    Este metodo es la forma "correcta" de cambiar el estado.
    #    Es como la "llave" del coche.
    def arrancar(self):
        print(f"Intentando arrancar el {self.modelo}...")
        
        # 3. LOGICA INTERNA
        #    El metodo comprueba su propio estado ('self.encendido')
        if self.encendido:
            print("Error: El coche YA estaba encendido.")
        else:
            # 4. MODIFICACION DEL ESTADO
            #    El metodo cambia su propio atributo 'self.encendido'.
            self.encendido = True
            print("¡Vroom! El coche ha arrancado.")
            
    def apagar(self):
        if not self.encendido:
            print("Error: El coche YA estaba apagado.")
        else:
            self.encendido = False
            print("El coche se ha apagado.")

# --- Uso ---
mi_coche = Coche("Honda", "Civic")

print(f"\n¿Coche encendido? (Estado inicial): {mi_coche.encendido}") # False
mi_coche.arrancar() # Llamamos al metodo para cambiar el estado
print(f"¿Coche encendido? (Despues de arrancar): {mi_coche.encendido}") # True
mi_coche.arrancar() # El metodo ahora detecta que ya estaba encendido
mi_coche.apagar()
print(f"¿Coche encendido? (Despues de apagar): {mi_coche.encendido}") # False
