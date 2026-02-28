# --- 4. Extendiendo con super() ---

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def trabajar(self):
        print(f"{self.nombre} esta trabajando.")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        # 1. LLAMADA AL PADRE
        #    Usamos super().__init__(...) para que la clase Empleado
        #    se encargue de guardar el nombre y el salario.
        #    ¡No repetimos ese codigo!
        super().__init__(nombre, salario)
        
        # 2. EXTENSION
        #    Ahora agregamos lo que es unico del Gerente.
        self.departamento = departamento

    def trabajar(self):
        # Podemos sobrescribir el metodo para hacerlo mas especifico
        print(f"{self.nombre} esta supervisando el departamento de {self.departamento}.")

# --- Uso ---
g = Gerente("Laura", 50000, "Ventas")
g.trabajar() # Usa la version del Gerente
print(f"Salario: {g.salario}") # Atributo heredado del Empleado