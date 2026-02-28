import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from Interfaz_ui import Ui_MiPrograma

class VentanaPrincipal(QMainWindow, Ui_MiPrograma):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        
        self.boton.clicked.connect(self.Pulsado)
        
    def Pulsado(self):
        print("Me pulsaron")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())