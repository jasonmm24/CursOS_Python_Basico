# --- 7. Clases Abstractas (Plantillas) ---
from abc import ABC, abstractmethod

# 'FormaGeometrica' hereda de ABC (Abstract Base Class).
# Esto la convierte en una plantilla que NO se puede usar directamente.
class FormaGeometrica(ABC):
    
    # @abstractmethod significa: "Mis hijos ESTAN OBLIGADOS a tener este metodo".
    @abstractmethod
    def calcular_area(self):
        pass 
    
    @abstractmethod
    def cambiar_lado(self):
        pass

class Cuadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    # CUMPLIENDO EL CONTRATO:
    # Si no definimos calcular_area aqui, Python dara error.
    def calcular_area(self):
        return self.lado * self.lado
    
    def cambiar_lado(self, nuevo_lado):
        self.lado = nuevo_lado

# forma = FormaGeometrica() # ERROR: No puedes crear una idea abstracta.
mi_cuadrado = Cuadrado(5)   # Si puedes crear algo concreto.
print(f"Area: {mi_cuadrado.calcular_area()}")

lado = int(input("dame el nuevo lado: "))

mi_cuadrado.cambiar_lado(lado)

print(f"Area: {mi_cuadrado.calcular_area()}")