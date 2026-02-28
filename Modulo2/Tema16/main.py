import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog
# Importamos la clase generada en tu archivo Interfaz_ui.py
from Interfaz_ui import Ui_MainWindow

class VentanaInventario(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ------------------------------------------------------------------
        # 1. CONFIGURACIÓN INICIAL DE LA TABLA
        # ------------------------------------------------------------------
        # Ajustamos el ancho de las columnas para que se vean bien
        self.tabla_productos.setColumnWidth(0, 50)  # ID (pequeño)
        self.tabla_productos.setColumnWidth(1, 200) # Producto (grande)
        self.tabla_productos.setColumnWidth(2, 100) # Categoría
        self.tabla_productos.setColumnWidth(3, 80)  # Precio

        # ------------------------------------------------------------------
        # 2. CONEXIONES (BOTONES Y PESTAÑAS)
        # ------------------------------------------------------------------
        self.btn_agregar.clicked.connect(self.agregar_fila)
        self.btn_eliminar.clicked.connect(self.eliminar_fila)
        self.btn_guardar_notas.clicked.connect(self.guardar_notas)

        # ------------------------------------------------------------------
        # 3. CONEXIONES DEL MENÚ (BARRA SUPERIOR)
        # ------------------------------------------------------------------
        # Las acciones (QAction) se conectan igual que los botones (triggered)
        self.action_salir.triggered.connect(self.close) # Cierra la ventana
        self.action_nuevo.triggered.connect(self.limpiar_tabla)
        self.action_acerca_de.triggered.connect(self.mostrar_info)

    def agregar_fila(self):
        """
        Agrega una nueva fila a la tabla con datos de ejemplo.
        En una app real, estos datos vendrían de inputs o base de datos.
        """
        # 1. Determinar en qué posición vamos a insertar (al final)
        fila_actual = self.tabla_productos.rowCount()
        
        # 2. Insertar una fila vacía
        self.tabla_productos.insertRow(fila_actual)

        # 3. Llenar las celdas (Items)
        # IMPORTANTE: QTableWidget necesita OBJETOS 'QTableWidgetItem', no strings simples.
        
        # Simulamos datos (Podrías usar QInputDialog para pedirlos al usuario)
        id_producto = str(fila_actual + 100)
        nombre = f"Producto Ejemplo {fila_actual + 1}"
        categoria = "General"
        precio = "10.00"

        # Creamos los items (las celdas)
        celda_id = QTableWidgetItem(id_producto)
        celda_nombre = QTableWidgetItem(nombre)
        celda_cat = QTableWidgetItem(categoria)
        celda_precio = QTableWidgetItem(precio)

        # 4. Colocamos los items en la tabla (Fila, Columna, Item)
        self.tabla_productos.setItem(fila_actual, 0, celda_id)
        self.tabla_productos.setItem(fila_actual, 1, celda_nombre)
        self.tabla_productos.setItem(fila_actual, 2, celda_cat)
        self.tabla_productos.setItem(fila_actual, 3, celda_precio)

        # Feedback en la barra de estado (parte inferior de la ventana)
        self.statusbar.showMessage(f"Producto '{nombre}' agregado correctamente", 3000)

    def eliminar_fila(self):
        """Elimina la fila que esté seleccionada actualmente."""
        fila_seleccionada = self.tabla_productos.currentRow()

        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Aviso", "Selecciona una fila para eliminar.")
            return

        # Eliminar la fila
        self.tabla_productos.removeRow(fila_seleccionada)
        self.statusbar.showMessage("Fila eliminada", 3000)

    def limpiar_tabla(self):
        """Acción del Menú 'Nuevo': Borra todo el contenido."""
        respuesta = QMessageBox.question(self, "Confirmar", "¿Deseas borrar todo el inventario?")
        if respuesta == QMessageBox.StandardButton.Yes:
            self.tabla_productos.setRowCount(0) # Truco rápido para vaciar tabla
            self.statusbar.showMessage("Inventario reseteado", 3000)

    def mostrar_info(self):
        """Acción del Menú 'Acerca de...'"""
        QMessageBox.information(self, "Acerca de", 
                                "Gestor de Inventario v1.0\n"
                                "Desarrollado para el Curso de Python con Qt Designer.")

    def guardar_notas(self):
        """Lógica de la segunda pestaña."""
        contenido = self.txt_notas.toPlainText()
        if contenido:
            QMessageBox.information(self, "Guardado", "Notas guardadas en memoria (simulado).")
        else:
            QMessageBox.warning(self, "Vacío", "No has escrito ninguna nota.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaInventario()
    ventana.show()
    sys.exit(app.exec())