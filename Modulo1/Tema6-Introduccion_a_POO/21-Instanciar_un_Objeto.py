# --- 3. Crear el Objeto (La "Instancia") ---
# OBJETIVO: Entender como "construir" un objeto real a partir del molde.

class Coche:
    pass

# --- Creacion de Objetos (Instanciacion) ---

# 1. 'mi_mustang = Coche()'
#    Esto le dice a Python: "Usa el molde 'Coche' para construir
#    un objeto nuevo y guarda ese objeto en la variable 'mi_mustang'".
#    A esto se le llama "instanciar" la clase.
mi_mustang = Coche()

# 2. 'mi_vocho = Coche()'
#    Hacemos lo mismo otra vez. Python crea un SEGUNDO objeto,
#    totalmente nuevo e independiente, y lo guarda en 'mi_vocho'.
mi_vocho = Coche()

# --- Comprobacion ---
print(f"La variable 'mi_mustang' contiene un: {type(mi_mustang)}")
print(f"La variable 'mi_vocho' contiene un: {type(mi_vocho)}")

# 'is' comprueba si dos variables apuntan al MISMO objeto en memoria.
print(f"¿Son el mismo objeto? {mi_mustang is mi_vocho}")