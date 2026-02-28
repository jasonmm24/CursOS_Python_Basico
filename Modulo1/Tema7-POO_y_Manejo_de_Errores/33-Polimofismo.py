# --- 5. Polimorfismo (Sobrescritura) ---

class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido generico.")

class Perro(Animal):
    # SOBRESCRITURA:
    # Definimos el mismo metodo que el padre, pero cambiamos su comportamiento.
    def hacer_sonido(self):
        print("El Perro hace: ¡Guau guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau miau!")

# --- Uso ---
# Lista polimorfica: contiene objetos de diferentes tipos
zoo = [Perro(), Gato(), Animal()]

for animal in zoo:
    # LA MAGIA:
    # Llamamos a .hacer_sonido() en todos.
    # Python sabe automaticamente cual version ejecutar segun el objeto.
    animal.hacer_sonido()