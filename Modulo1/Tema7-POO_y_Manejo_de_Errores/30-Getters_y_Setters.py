# --- 2. Getters y Setters (Control de Acceso) ---

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        # Usamos un guion bajo (_) para indicar que es "protegido" (uso interno)
        self._edad = edad

    # 1. EL GETTER (@property)
    #    Nos permite leer 'self._edad' escribiendo simplemente 'objeto.edad'.
    @property
    def edad(self):
        print("--> Leyendo la edad...")
        return self._edad

    # 2. EL SETTER (@edad.setter)
    #    Se ejecuta automaticamente cuando intentamos ASIGNAR un valor (objeto.edad = X).
    #    Aqui es donde metemos la VALIDACION.
    @edad.setter
    def edad(self, nueva_edad):
        print("--> Intentando cambiar la edad...")
        if nueva_edad > 0:
            self._edad = nueva_edad
            print("   Edad actualizada correctamente.")
        else:
            print("   ERROR: No puedes tener edad negativa.")

# --- Uso ---
usr = Usuario("Carlos", 25)

# Al leer, se activa el @property
print(f"Edad actual: {usr.edad}") 

# Al asignar, se activa el @edad.setter
usr.edad = -5  # El setter detecta el error y bloquea el cambio
usr.edad = 30  # El setter valida que es > 0 y permite el cambio