import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
# Importamos tu diseño generado
from Interfaz_ui import Ui_MainWindow

class VentanaEncuesta(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectamos el botón para procesar la encuesta
        self.btn_confirmar.clicked.connect(self.mostrar_resumen)

    def mostrar_resumen(self):
        """
        Esta función recopila toda la información de los widgets complejos
        y la muestra en un cuadro de diálogo (QMessageBox).
        """
        
        # ---------------------------------------------------------
        # 1. LÓGICA DE RADIO BUTTONS (Selección Única)
        # ---------------------------------------------------------
        # Verificamos manualmente cuál está marcado con .isChecked()
        nivel_experiencia = "No especificado"
        
        if self.rb_principiante.isChecked():
            nivel_experiencia = "Principiante"
        elif self.rb_intermedio.isChecked():
            nivel_experiencia = "Intermedio"
        elif self.rb_avanzado.isChecked():
            nivel_experiencia = "Avanzado"

        # ---------------------------------------------------------
        # 2. LÓGICA DE COMBOBOX (Lista Desplegable)
        # ---------------------------------------------------------
        # Es muy sencillo: .currentText() nos da lo que se ve en pantalla.
        ciudad_seleccionada = self.combo_ciudades.currentText()

        # ---------------------------------------------------------
        # 3. LÓGICA DE LIST WIDGET (Selección Múltiple)
        # ---------------------------------------------------------
        # Esto es más complejo. .selectedItems() devuelve una lista de OBJETOS,
        # no de textos. Hay que recorrer esa lista con un bucle 'for'.
        
        items_seleccionados = self.lista_items.selectedItems()
        lista_lenguajes = []
        
        for item in items_seleccionados:
            # Extraemos el texto de cada objeto item
            lista_lenguajes.append(item.text())

        # Si la lista está vacía, ponemos un texto por defecto
        if not lista_lenguajes:
            texto_lenguajes = "Ninguno"
        else:
            # Unimos los elementos con comas (ej: "Python, Java, C++")
            texto_lenguajes = ", ".join(lista_lenguajes)

        # ---------------------------------------------------------
        # 4. USO DE QMESSAGEBOX (Diálogos)
        # ---------------------------------------------------------
        # Construimos el mensaje final
        mensaje_final = (
            f"Resultados de la Encuesta:\n\n"
            f"• Nivel: {nivel_experiencia}\n"
            f"• Ciudad: {ciudad_seleccionada}\n"
            f"• Lenguajes: {texto_lenguajes}"
        )

        # Lanzamos la ventana emergente
        # Parámetros: (Padre, Título, Texto del mensaje)
        QMessageBox.information(self, "Confirmación de Datos", mensaje_final)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaEncuesta()
    ventana.show()
    sys.exit(app.exec())