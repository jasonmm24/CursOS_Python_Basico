import sys
import json  # Importamos librería JSON para guardar datos en archivo
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem, 
                               QMessageBox, QWidget, QVBoxLayout, QLineEdit, 
                               QGridLayout, QPushButton)
from PySide6.QtGui import QColor, QBrush, QFont, QKeyEvent
from PySide6.QtCore import Qt

# Importamos nuestras interfaces visuales
from gastos_ui import Ui_MainWindow
from calculadora_ui import Ui_Form

# ============================================================================
# CLASE: CALCULADORA (Código del Tema anterior, sin cambios)
# ============================================================================
class Calculadora(QWidget, Ui_Form):
    """Ventana independiente para cálculos rápidos."""
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.expresion = ""

        # Conexiones numéricas y operacionales
        for n in range(10):
            getattr(self, f"btn_{n}").clicked.connect(lambda ch, num=n: self.agregar_texto(str(num)))
        
        self.btn_suma.clicked.connect(lambda: self.agregar_texto("+"))
        self.btn_resta.clicked.connect(lambda: self.agregar_texto("-"))
        self.btn_mul.clicked.connect(lambda: self.agregar_texto("*"))
        self.btn_div.clicked.connect(lambda: self.agregar_texto("/"))
        self.btn_igual.clicked.connect(self.calcular_resultado)
        self.btn_c.clicked.connect(self.borrar_todo)

    def keyPressEvent(self, event: QKeyEvent):
        """Manejo de teclado físico."""
        texto = event.text()
        clave = event.key()
        if texto in "0123456789+-*/.":
            self.agregar_texto(texto)
        elif clave in (Qt.Key_Return, Qt.Key_Enter):
            self.calcular_resultado()
        elif clave in (Qt.Key_Escape, Qt.Key_Delete):
            self.borrar_todo()

    def agregar_texto(self, texto):
        self.expresion += texto
        self.pantalla.setText(self.expresion)

    def calcular_resultado(self):
        try:
            res = str(eval(self.expresion))
            self.pantalla.setText(res)
            self.expresion = res
        except:
            self.pantalla.setText("Error")
            self.expresion = ""

    def borrar_todo(self):
        self.expresion = ""
        self.pantalla.clear()


# ============================================================================
# CLASE PRINCIPAL: GESTOR DE GASTOS PRO
# ============================================================================
class GestorGastos(QMainWindow, Ui_MainWindow):
    """
    Versión Avanzada (Tema 19) con:
    1. Persistencia de Datos (JSON)
    2. Filtrado de Tabla
    3. Estilos QSS (Modo Oscuro)
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Ajustes iniciales de tabla
        self.tabla_gastos.setColumnWidth(0, 100)
        self.tabla_gastos.setColumnWidth(1, 150)
        self.tabla_gastos.setColumnWidth(2, 200)

        self.ventana_calculadora = None

        # --- CONEXIONES ---
        self.btn_agregar.clicked.connect(self.registrar_gasto)
        self.btn_eliminar.clicked.connect(self.eliminar_gasto)
        self.btn_calculadora.clicked.connect(self.abrir_calculadora)
        self.spin_limite.valueChanged.connect(self.actualizar_total)
        
        # NUEVAS CONEXIONES (TEMA 19)
        # 1. Al cambiar la opción del combo de filtro, ejecutamos el filtrado
        self.combo_filtro.currentTextChanged.connect(self.filtrar_tabla)
        # 2. Al marcar el checkbox, activamos/desactivamos el tema oscuro
        self.check_oscuro.toggled.connect(self.cambiar_tema)

        # --- CARGA DE DATOS AL INICIO ---
        # Intentamos cargar datos guardados anteriormente
        self.cargar_datos_json()

    def abrir_calculadora(self):
        if self.ventana_calculadora is None:
            self.ventana_calculadora = Calculadora()
        self.ventana_calculadora.show()

    # ========================================================================
    # FUNCIÓN: REGISTRAR GASTO (Modificada para guardar automáticamente)
    # ========================================================================
    def registrar_gasto(self):
        fecha = self.date_gasto.date().toString("dd/MM/yyyy")
        categoria = self.combo_categoria.currentText()
        descripcion = self.input_descripcion.text()
        monto = self.spin_monto.value()

        if monto == 0 or not descripcion:
            QMessageBox.warning(self, "Atención", "Revisa los datos (Monto > 0 y Descripción obligatoria).")
            return

        # Insertamos en la tabla
        self.insertar_fila_tabla(fecha, categoria, descripcion, monto)

        # Limpiamos y actualizamos
        self.input_descripcion.clear()
        self.spin_monto.setValue(0.00)
        self.actualizar_total()
        
        # NUEVO: Guardamos los cambios en el archivo JSON
        self.guardar_datos_json()
        
        self.statusbar.showMessage("Gasto guardado", 3000)

    def insertar_fila_tabla(self, fecha, cat, desc, monto):
        """Función auxiliar para no repetir código al cargar desde JSON."""
        fila = self.tabla_gastos.rowCount()
        self.tabla_gastos.insertRow(fila)

        item_fecha = QTableWidgetItem(fecha)
        item_cat = QTableWidgetItem(cat)
        item_desc = QTableWidgetItem(desc)
        item_monto = QTableWidgetItem(f"{monto:.2f}")
        item_monto.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        # Lógica de colores (rojo si > 1000)
        if float(monto) > 1000:
            color_rojo = QColor(231, 76, 60)
            item_monto.setForeground(QBrush(color_rojo))
            item_monto.setFont(QFont("Arial", weight=QFont.Bold))

        self.tabla_gastos.setItem(fila, 0, item_fecha)
        self.tabla_gastos.setItem(fila, 1, item_cat)
        self.tabla_gastos.setItem(fila, 2, item_desc)
        self.tabla_gastos.setItem(fila, 3, item_monto)

    # ========================================================================
    # FUNCIÓN: ELIMINAR (Modificada para guardar automáticamente)
    # ========================================================================
    def eliminar_gasto(self):
        fila = self.tabla_gastos.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Error", "Selecciona una fila.")
            return

        if QMessageBox.question(self, "Borrar", "¿Eliminar?") == QMessageBox.StandardButton.Yes:
            self.tabla_gastos.removeRow(fila)
            self.actualizar_total()
            
            # NUEVO: Actualizamos el archivo JSON tras borrar
            self.guardar_datos_json()
            
            self.statusbar.showMessage("Eliminado", 3000)

    def actualizar_total(self):
        total = 0.0
        filas = self.tabla_gastos.rowCount()
        
        # Sumamos solo las filas VISIBLES (respetando el filtro)
        for i in range(filas):
            if not self.tabla_gastos.isRowHidden(i):
                try:
                    texto = self.tabla_gastos.item(i, 3).text()
                    total += float(texto)
                except: pass

        self.lbl_total_valor.setText(f"${total:,.2f}")

        limit = self.spin_limite.value()
        if total > limit:
            self.lbl_total_valor.setStyleSheet("color: red; font-size: 14pt; font-weight: bold;")
        else:
            # Respetamos el color según el modo (oscuro o claro)
            color = "white" if self.check_oscuro.isChecked() else "#2881bd"
            self.lbl_total_valor.setStyleSheet(f"color: {color}; font-size: 14pt; font-weight: bold;")

    # ========================================================================
    # TEMA 19: CARACTERÍSTICA 1 - FILTRADO DE DATOS
    # ========================================================================
    def filtrar_tabla(self, categoria_seleccionada):
        """
        Oculta o muestra filas según la categoría seleccionada en el ComboBox.
        """
        filas = self.tabla_gastos.rowCount()
        
        for i in range(filas):
            # Obtenemos el texto de la columna 1 (Categoría)
            cat_fila = self.tabla_gastos.item(i, 1).text()
            
            # Lógica: Si seleccionamos "Todas", mostramos todo.
            # Si no, mostramos solo las que coinciden con la selección.
            if categoria_seleccionada == "Todas":
                self.tabla_gastos.setRowHidden(i, False) # Mostrar
            elif categoria_seleccionada == cat_fila:
                self.tabla_gastos.setRowHidden(i, False) # Mostrar
            else:
                self.tabla_gastos.setRowHidden(i, True)  # Ocultar
        
        # Recalculamos el total para sumar solo lo visible
        self.actualizar_total()

    # ========================================================================
    # TEMA 19: CARACTERÍSTICA 2 - PERSISTENCIA (JSON)
    # ========================================================================
    def guardar_datos_json(self):
        """
        Recorre la tabla y guarda los datos en un archivo 'datos_gastos.json'.
        """
        lista_datos = []
        filas = self.tabla_gastos.rowCount()
        
        for i in range(filas):
            datos_fila = {
                "fecha": self.tabla_gastos.item(i, 0).text(),
                "categoria": self.tabla_gastos.item(i, 1).text(),
                "descripcion": self.tabla_gastos.item(i, 2).text(),
                "monto": float(self.tabla_gastos.item(i, 3).text())
            }
            lista_datos.append(datos_fila)
            
        try:
            with open("datos_gastos.json", "w") as archivo:
                json.dump(lista_datos, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar: {e}")

    def cargar_datos_json(self):
        """
        Lee 'datos_gastos.json' y rellena la tabla al iniciar la app.
        """
        try:
            with open("datos_gastos.json", "r") as archivo:
                lista_datos = json.load(archivo)
                
            for dato in lista_datos:
                self.insertar_fila_tabla(
                    dato["fecha"], dato["categoria"], dato["descripcion"], dato["monto"]
                )
            self.actualizar_total()
        except FileNotFoundError:
            pass # Si el archivo no existe (primera vez), no hacemos nada.

    # ========================================================================
    # TEMA 19: CARACTERÍSTICA 3 - ESTILOS QSS (Modo Oscuro)
    # ========================================================================
    def cambiar_tema(self, activado):
        """
        Aplica hojas de estilo (CSS) para cambiar entre modo Claro y Oscuro.
        """
        if activado:
            # --- MODO OSCURO (Dark Theme) ---
            estilo_oscuro = """
            QMainWindow, QWidget { background-color: #2b2b2b; color: #ffffff; }
            QTableWidget { gridline-color: #555; background-color: #333; color: white; }
            QHeaderView::section { background-color: #444; color: white; }
            QLineEdit, QSpinBox, QDateEdit, QComboBox { 
                background-color: #444; color: white; border: 1px solid #555; padding: 4px;
            }
            QPushButton { background-color: #555; color: white; border-radius: 4px; padding: 6px; }
            QPushButton:hover { background-color: #666; }
            QGroupBox { border: 1px solid #555; margin-top: 10px; }
            QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px; }
            QLabel { color: #ddd; }
            """
            
            self.setStyleSheet(estilo_oscuro)
        else:
            # --- MODO CLARO (Default) ---
            self.setStyleSheet("") # Vaciar estilo vuelve al diseño de sistema

        # Actualizamos el total para arreglar el color del texto si es necesario
        self.actualizar_total()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GestorGastos()
    window.show()
    sys.exit(app.exec())