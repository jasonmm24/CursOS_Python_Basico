# --- 6. Polimorfismo sin Herencia estricta ---

class PDF:
    def abrir(self):
        print("Abriendo archivo PDF con Adobe...")

class Word:
    def abrir(self):
        print("Abriendo documento Word con Office...")

# Esta funcion NO sabe de clases (PDF o Word).
# Solo le importa que el objeto recibido tenga un metodo .abrir()
def lector_de_archivos(documento):
    print("--- Iniciando lectura ---")
    documento.abrir()

doc1 = PDF()
doc2 = Word()

# Funciona con ambos porque ambos "saben" abrirse.
lector_de_archivos(doc1)
lector_de_archivos(doc2)