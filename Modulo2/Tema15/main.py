import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from PySide6.QtCore import Qt
# Importamos la clase generada en tu archivo Interfaz_ui.py
from Interfaz_ui import Ui_MainWindow

class GestorTareas(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # --- CONEXIONES (SEÑALES Y SLOTS) ---
        self.btn_agregar.clicked.connect(self.agregar_tarea)
        self.btn_eliminar.clicked.connect(self.eliminar_tarea)
        self.btn_limpiar.clicked.connect(self.borrar_todo)

        # Opcional: Permitir agregar tarea pulsando "Enter" en la caja de texto
        self.input_tarea.returnPressed.connect(self.agregar_tarea)

    def agregar_tarea(self):
        """Recopila datos, los formatea y añade a la lista."""
        
        # 1. OBTENER DATOS
        tarea_texto = self.input_tarea.text().strip() # .strip() quita espacios vacíos al inicio/final
        prioridad = self.combo_prioridad.currentText()
        
        # Obtener fecha: .date() devuelve un objeto fecha, .toString() lo convierte a texto
        fecha = self.date_limite.date().toString("dd/MM/yyyy")

        # 2. VALIDACIÓN (Evitar tareas vacías)
        if not tarea_texto:
            QMessageBox.warning(self, "Aviso", "La descripción de la tarea no puede estar vacía.")
            return

        # 3. FORMATEO DEL TEXTO
        # Creamos una cadena bonita para mostrar en la lista
        item_texto = f"[{fecha}] - ({prioridad}) {tarea_texto}"

        # 4. AGREGAR A LA LISTA
        # Opción A (Simple): self.lista_tareas.addItem(item_texto)
        
        # Opción B (Avanzada - Recomendada): Usar QListWidgetItem para personalizar colores
        item = QListWidgetItem(item_texto)
        
        # Colorear según prioridad (Lógica condicional visual)
        if prioridad == "Alta":
            item.setForeground(Qt.GlobalColor.red) # Texto rojo
        elif prioridad == "Media":
            item.setForeground(Qt.GlobalColor.orange) # Texto azul oscuro
        else:
            item.setForeground(Qt.GlobalColor.black) # Texto negro

        self.lista_tareas.addItem(item)

        # 5. LIMPIEZA Y ACTUALIZACIÓN
        self.input_tarea.clear()  # Borrar el campo de texto
        self.input_tarea.setFocus() # Poner el cursor de nuevo para escribir rápido
        self.actualizar_contador()

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada actualmente."""
        # Obtenemos la fila seleccionada (row)
        fila_seleccionada = self.lista_tareas.currentRow()

        # Si no hay selección, currentRow() devuelve -1
        if fila_seleccionada == -1:
            QMessageBox.information(self, "Info", "Selecciona una tarea para eliminar.")
            return

        # Preguntar confirmación (Buenas prácticas de UX)
        respuesta = QMessageBox.question(
            self, "Confirmar", "¿Seguro que deseas eliminar esta tarea?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta == QMessageBox.StandardButton.Yes:
            # takeItem extrae el ítem de la lista y lo elimina
            self.lista_tareas.takeItem(fila_seleccionada)
            self.actualizar_contador()

    def borrar_todo(self):
        """Limpia toda la lista."""
        cantidad = self.lista_tareas.count()
        
        if cantidad > 0:
            respuesta = QMessageBox.warning(
                self, "Cuidado", f"¿Vas a borrar {cantidad} tareas?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if respuesta == QMessageBox.StandardButton.Yes:
                self.lista_tareas.clear()
                self.actualizar_contador()

    def actualizar_contador(self):
        """Actualiza la etiqueta inferior con el número total de tareas."""
        cantidad = self.lista_tareas.count()
        self.lbl_contador.setText(f"Tareas pendientes: {cantidad}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GestorTareas()
    ventana.show()
    sys.exit(app.exec())