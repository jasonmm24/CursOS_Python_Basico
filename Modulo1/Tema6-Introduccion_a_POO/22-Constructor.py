# --- 4. El Constructor '__init__' ---
# OBJETIVO: Entender que funcion se ejecuta AUTOMATICAMENTE
#           cuando creas un nuevo objeto.

class Coche:
    
    # 1. '__init__' es un metodo "magico" (Doble Guion Bajo).
    #    Es el "constructor" o la "linea de ensamblaje".
    #    Se ejecuta 1 sola vez por cada objeto, justo al crearlo.
    #
    # 2. 'self' es un parametro OBLIGATORIO y siempre es el primero.
    #    'self' es una variable especial que representa al objeto
    #    que se esta creando en ese momento (ej. 'mi_coche_1').
    def __init__(self):
        print("--- ¡BIP BOP! Nuevo coche en la linea de ensamblaje. ---")
        print("El metodo __init__ se ha ejecutado.")

# --- Creacion ---
print("Voy a crear el primer coche...")
# 3. Esta linea...
mi_coche_1 = Coche() 
#  ...hace que Python llame a __init__(self=mi_coche_1) automaticamente.

print("\nVoy a crear el segundo coche...")
# 4. Esta linea...
mi_coche_2 = Coche()
#  ...hace que Python llame a __init__(self=mi_coche_2) otra vez.