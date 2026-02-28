import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, 
                               QMessageBox, QWidget, QVBoxLayout, QLineEdit, 
                               QGridLayout, QPushButton)
from PySide6.QtGui import QColor, QBrush, QFont, QKeyEvent
from PySide6.QtCore import Qt

# Importamos las dos interfaces visuales
from gastos_ui import Ui_MainWindow   # Ventana Principal
from calculadora_ui import Ui_Form    # Ventana Secundaria

# ============================================================================
# CLASE: CALCULADORA (Secundaria)
# ============================================================================
class Calculadora(QWidget, Ui_Form):
    """
    Ventana de calculadora que funciona tanto con clics como con teclado físico.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.expresion = "" # Variable interna para guardar la operación matemática

        # --- CONEXIONES DE BOTONES (Ratón) ---
        # Conectamos cada botón numérico a la función agregar_texto
        self.btn_0.clicked.connect(lambda: self.agregar_texto("0"))
        self.btn_1.clicked.connect(lambda: self.agregar_texto("1"))
        self.btn_2.clicked.connect(lambda: self.agregar_texto("2"))
        self.btn_3.clicked.connect(lambda: self.agregar_texto("3"))
        self.btn_4.clicked.connect(lambda: self.agregar_texto("4"))
        self.btn_5.clicked.connect(lambda: self.agregar_texto("5"))
        self.btn_6.clicked.connect(lambda: self.agregar_texto("6"))
        self.btn_7.clicked.connect(lambda: self.agregar_texto("7"))
        self.btn_8.clicked.connect(lambda: self.agregar_texto("8"))
        self.btn_9.clicked.connect(lambda: self.agregar_texto("9"))

        # Conectamos los operadores
        self.btn_suma.clicked.connect(lambda: self.agregar_texto("+"))
        self.btn_resta.clicked.connect(lambda: self.agregar_texto("-"))
        self.btn_mul.clicked.connect(lambda: self.agregar_texto("*"))
        self.btn_div.clicked.connect(lambda: self.agregar_texto("/"))

        # Botones de acción
        self.btn_igual.clicked.connect(self.calcular_resultado)
        self.btn_c.clicked.connect(self.borrar_todo)

    def keyPressEvent(self, event: QKeyEvent):
        """
        MÉTODO MÁGICO DE QT:
        Detecta cuando el usuario presiona una tecla física mientras usa esta ventana.
        """
        # Obtenemos el texto de la tecla (ej: "1", "+", "a")
        texto_tecla = event.text()
        # Obtenemos el código de tecla (útil para teclas especiales como Enter o Esc)
        codigo_tecla = event.key()

        # 1. Si es un número o un operador matemático válido
        if texto_tecla in "0123456789+-*/.":
            self.agregar_texto(texto_tecla)
        
        # 2. Si es la tecla ENTER (Qt tiene dos códigos para Enter: el normal y el del teclado numérico)
        elif codigo_tecla == Qt.Key_Return or codigo_tecla == Qt.Key_Enter:
            self.btn_igual.animateClick() # Efecto visual de clic en el botón
            self.calcular_resultado()
            
        # 3. Si es la tecla ESCAPE o SUPRIMIR -> Borrar todo
        elif codigo_tecla == Qt.Key_Escape or codigo_tecla == Qt.Key_Delete:
            self.btn_c.animateClick()
            self.borrar_todo()
            
        # 4. Si es BACKSPACE (Borrar hacia atrás) -> Borrar último caracter
        elif codigo_tecla == Qt.Key_Backspace:
            # Eliminamos el último caracter del string
            self.expresion = self.expresion[:-1]
            self.pantalla.setText(self.expresion)

    def agregar_texto(self, texto):
        """Añade números o símbolos a la pantalla y actualiza la variable interna."""
        self.expresion += texto
        self.pantalla.setText(self.expresion)

    def calcular_resultado(self):
        """Evalúa la operación matemática escrita en la expresión."""
        try:
            # 'eval' ejecuta el cálculo matemático (ej: eval("2+2") -> 4)
            # Convertimos a str para poder ponerlo en el LineEdit
            resultado = str(eval(self.expresion))
            self.pantalla.setText(resultado)
            # Guardamos el resultado como nueva base para seguir operando
            self.expresion = resultado 
        except:
            # Si hay error (ej: división por cero), mostramos aviso
            self.pantalla.setText("Error")
            self.expresion = ""

    def borrar_todo(self):
        """Resetea la calculadora."""
        self.expresion = ""
        self.pantalla.clear()


# ============================================================================
# CLASE: GESTOR DE GASTOS (Principal)
# ============================================================================
class GestorGastos(QMainWindow, Ui_MainWindow):
    """
    Controlador principal de la aplicación de Finanzas.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Ajustes estéticos de columnas de la tabla
        self.tabla_gastos.setColumnWidth(0, 100) # Fecha
        self.tabla_gastos.setColumnWidth(1, 150) # Categoría
        self.tabla_gastos.setColumnWidth(2, 200) # Descripción

        # Variable para controlar la ventana de calculadora
        self.ventana_calculadora = None

        # Conexiones de la interfaz principal
        self.btn_agregar.clicked.connect(self.registrar_gasto)
        self.btn_eliminar.clicked.connect(self.eliminar_gasto)
        self.btn_calculadora.clicked.connect(self.abrir_calculadora)
        
        # Conexión reactiva: si cambia el límite, actualizamos colores al instante
        self.spin_limite.valueChanged.connect(self.actualizar_total)

    def abrir_calculadora(self):
        """Abre la ventana de calculadora (si no está ya abierta)."""
        if self.ventana_calculadora is None:
            self.ventana_calculadora = Calculadora()
        self.ventana_calculadora.show()

    def registrar_gasto(self):
        """Toma los datos del formulario y los guarda en la tabla."""
        fecha = self.date_gasto.date().toString("dd/MM/yyyy")
        categoria = self.combo_categoria.currentText()
        descripcion = self.input_descripcion.text()
        monto = self.spin_monto.value()

        # Validaciones
        if monto == 0:
            QMessageBox.warning(self, "Atención", "El monto debe ser mayor a 0.")
            return

        if not descripcion:
            QMessageBox.warning(self, "Atención", "Debes escribir una descripción.")
            return

        # Insertar fila
        fila = self.tabla_gastos.rowCount()
        self.tabla_gastos.insertRow(fila)

        # Crear celdas
        item_fecha = QTableWidgetItem(fecha)
        item_cat = QTableWidgetItem(categoria)
        item_desc = QTableWidgetItem(descripcion)
        item_monto = QTableWidgetItem(f"{monto:.2f}")
        item_monto.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        # Resaltar gastos individuales altos (> 1000)
        if monto > 1000:
            color_rojo = QColor(231, 76, 60)
            pincel = QBrush(color_rojo)
            
            item_monto.setForeground(pincel)
            item_fecha.setForeground(pincel)
            
            fuente = item_monto.font()
            fuente.setBold(True)
            item_monto.setFont(fuente)

        # Llenar tabla
        self.tabla_gastos.setItem(fila, 0, item_fecha)
        self.tabla_gastos.setItem(fila, 1, item_cat)
        self.tabla_gastos.setItem(fila, 2, item_desc)
        self.tabla_gastos.setItem(fila, 3, item_monto)

        # Limpiar campos y actualizar
        self.input_descripcion.clear()
        self.spin_monto.setValue(0.00)
        
        self.actualizar_total()
        self.statusbar.showMessage("Gasto registrado con éxito", 3000)

    def eliminar_gasto(self):
        """Elimina la fila seleccionada."""
        fila_seleccionada = self.tabla_gastos.currentRow()

        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Error", "Selecciona una fila para eliminar.")
            return

        respuesta = QMessageBox.question(
            self, "Confirmar", "¿Estás seguro de eliminar este gasto?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta == QMessageBox.StandardButton.Yes:
            self.tabla_gastos.removeRow(fila_seleccionada)
            self.actualizar_total()
            self.statusbar.showMessage("Gasto eliminado", 3000)

    def actualizar_total(self):
        """Suma la columna de montos y verifica alertas de presupuesto."""
        total = 0.0
        total_filas = self.tabla_gastos.rowCount()

        for i in range(total_filas):
            item_texto = self.tabla_gastos.item(i, 3).text()
            try:
                valor = float(item_texto)
                total += valor
            except ValueError:
                pass

        self.lbl_total_valor.setText(f"${total:,.2f}")

        # Lógica de Alerta Personalizada
        limite_usuario = self.spin_limite.value()

        if total > limite_usuario:
            self.lbl_total_valor.setStyleSheet("color: red; font-size: 14pt; font-weight: bold;")
            self.statusbar.showMessage(f"¡ALERTA! Has superado tu límite de ${limite_usuario:,.2f}", 5000)
        else:
            self.lbl_total_valor.setStyleSheet("color: #2980b9; font-size: 14pt; font-weight: bold;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = GestorGastos()
    ventana.show()
    sys.exit(app.exec())