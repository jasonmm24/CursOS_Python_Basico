# --- CODIGO 5: ---
import os # Necesario para verificar si el archivo existe

# 1. LA CLASE (El Molde)
class Videojuego:
    def __init__(self, titulo, anio, precio):
        self.titulo = titulo
        self.anio = anio
        self.precio = precio

    # Metodo para convertir el objeto a texto CSV (Comma Separated Values)
    # Ejemplo: "Mario,1985,500"
    def a_texto(self):
        return f"{self.titulo},{self.anio},{self.precio}"

    def __str__(self):
        return f"🎮 {self.titulo} ({self.anio}) - ${self.precio}"

# 2. FUNCIONES DE MANEJO DE ARCHIVOS

def guardar_catalogo(lista_juegos):
    """Sobrescribe el archivo con la lista actual de objetos."""
    with open("catalogo.txt", "w", encoding="utf-8") as f:
        for juego in lista_juegos:
            # Guardamos la version en texto del objeto
            f.write(juego.a_texto() + "\n")
    print("--> Datos guardados en disco.")

def cargar_catalogo():
    """Lee el archivo y reconstruye los objetos."""
    lista_recuperada = []
    
    # Si el archivo no existe, devolvemos lista vacia
    if not os.path.exists("catalogo.txt"):
        return []

    with open("catalogo.txt", "r", encoding="utf-8") as f:
        for linea in f:
            datos = linea.strip().split(',')
            if len(datos) == 3:
                # 3. RECONSTRUCCION DEL OBJETO
                # Leemos texto y creamos un nuevo objeto Videojuego
                titulo = datos[0]
                anio = int(datos[1])
                precio = float(datos[2])
                
                juego_temporal = Videojuego(titulo, anio, precio)
                lista_recuperada.append(juego_temporal)
                
    return lista_recuperada

# 3. PROGRAMA PRINCIPAL
def main():
    # Paso A: Cargar lo que teniamos guardado antes
    mis_juegos = cargar_catalogo()
    print(f"Inicio: Se cargaron {len(mis_juegos)} juegos del disco.")

    while True:
        print("\n1. Agregar Juego")
        print("2. Ver Catalogo")
        print("3. Guardar y Salir")
        opc = input("Opcion: ")

        if opc == "1":
            t = input("Titulo: ")
            a = int(input("Año: "))
            p = float(input("Precio: "))
            # Creamos el objeto y lo metemos a la lista en memoria
            mis_juegos.append(Videojuego(t, a, p))
        
        elif opc == "2":
            print("\n--- CATALOGO ---")
            for j in mis_juegos:
                print(j) # Llama a __str__
        
        elif opc == "3":
            # Paso B: Guardar todo antes de cerrar
            guardar_catalogo(mis_juegos)
            print("¡Adios!")
            break

if __name__ == "__main__":
    main()