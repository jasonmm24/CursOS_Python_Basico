# --- 8. Metodos de Clase (Constructores Alternativos) ---
from datetime import date

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad}.")

    # @classmethod recibe 'cls' (la Clase Persona) en vez de 'self'.
    # Lo usamos aqui para crear una Persona sabiendo su año de nacimiento.
    @classmethod
    def desde_nacimiento(cls, nombre, anio_nacimiento):
        # Calculamos la edad
        edad_calculada = date.today().year - anio_nacimiento
        # Llamamos al constructor estandar cls(...) -> Persona(...)
        return cls(nombre, edad_calculada)

# Crear objeto normal
p1 = Persona("Juan", 30)

p1.presentarse()

# Crear objeto usando el metodo de clase (Factory)
p2 = Persona.desde_nacimiento("Lucia", 2000)

p2.presentarse()