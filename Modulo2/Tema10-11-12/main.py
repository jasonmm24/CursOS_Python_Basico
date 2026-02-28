import sys  # Importamos el módulo sys para acceder a parámetros del sistema y controlar el cierre del programa.
from PySide6.QtWidgets import QApplication, QMainWindow  # Importamos los componentes básicos de Qt.

# ----------------------------------------------------------------------------------
# IMPORTANTE: 
# Aquí importamos la clase del archivo 'Interfaz_ui.py' que generaste con Qt Designer.
# 'Ui_MainWindow' es el nombre por defecto que da Qt a la clase de la interfaz.
# ----------------------------------------------------------------------------------
from Interfaz_ui import Ui_MainWindow


class VentanaPrincipal(QMainWindow, Ui_MainWindow):
    """
    Clase principal de la aplicación.
    
    Hereda de:
    1. QMainWindow: Para tener las características de una ventana normal (cerrar, minimizar, mover).
    2. Ui_MainWindow: Para tener acceso a todos los widgets dibujados en Qt Designer.
    """
    
    def __init__(self):
        """
        Constructor: Se ejecuta UNA SOLA VEZ al iniciar la ventana.
        Aquí configuramos todo lo inicial.
        """
        # Inicializamos la clase padre (QMainWindow) para construir la ventana base.
        super().__init__()
        
        # ----------------------------------------------------------------------
        # CONFIGURACIÓN DE LA INTERFAZ (UI)
        # Llama al método que construye visualmente los botones, textos, etc.
        # Sin esta línea, la ventana aparecería vacía.
        # ----------------------------------------------------------------------
        self.setupUi(self)

        # ----------------------------------------------------------------------
        # ZONA DE CONEXIONES (SEÑALES Y SLOTS)
        # Aquí definimos la interactividad: "¿Qué pasa cuando toco esto?"
        # Formato: self.objeto.evento.connect(self.funcion_a_ejecutar)
        # ----------------------------------------------------------------------
        
        # Cuando el botón 'btn_accion' sea clickeado, ejecuta la función 'procesar_formulario'
        self.btn_accion.clicked.connect(self.procesar_formulario)
        
        # Cuando el checkbox 'check_opcion' cambie (se marque o desmarque), ejecuta 'estado_cambiado'
        self.check_opcion.toggled.connect(self.estado_cambiado)


    def procesar_formulario(self):
        """
        Esta función actúa como el 'Cerebro' del formulario.
        Se ejecuta automáticamente al hacer clic en el botón.
        """
        # 1. RECUPERAR DATOS (GET)
        # Accedemos a los widgets usando 'self.' + el nombre que les dimos en Qt Designer.
        
        nombre = self.input_texto.text()                # .text() obtiene el string de un QLineEdit
        edad = self.input_numero.value()                # .value() obtiene el entero de un QSpinBox
        opcion_seleccionada = self.combo_opciones.currentText() # .currentText() obtiene el texto visible del combo
        
        # 2. PROCESAR O MOSTRAR DATOS
        # En este ejemplo, simplemente los mostramos en la consola del IDE (abajo).
        print("-" * 30)
        print("PROCESANDO FORMULARIO...")
        print(f"-> Nombre recibido: {nombre}")
        print(f"-> Edad recibida: {edad}")
        print(f"-> Opción elegida: {opcion_seleccionada}")
        
        # 3. MODIFICAR LA INTERFAZ (SET)
        # Podemos cambiar cosas visuales como respuesta.
        # Aquí cambiamos el texto del propio botón para dar feedback al usuario.
        self.btn_accion.setText("¡Datos enviados con éxito!")


    def estado_cambiado(self, estado):
        """
        Esta función reacciona al CheckBox.
        
        Parámetros:
        estado (bool): Qt envía automáticamente True si se marcó, False si se desmarcó.
        """
        if estado == True:
            print("INFO: El usuario ha ACTIVADO la casilla.")
        else:
            print("INFO: El usuario ha DESACTIVADO la casilla.")


# ----------------------------------------------------------------------------------
# BLOQUE PRINCIPAL DE EJECUCIÓN
# Este código solo se ejecuta si lanzamos este archivo directamente.
# ----------------------------------------------------------------------------------
if __name__ == "__main__":
    # 1. Creamos la instancia de la aplicación.
    # sys.argv permite pasar comandos por consola al arrancar (necesario para Qt).
    app = QApplication(sys.argv)
    
    # 2. Creamos una instancia de nuestra ventana personalizada.
    # En este momento se ejecuta el __init__ de arriba.
    ventana = VentanaPrincipal()
    
    # 3. Hacemos visible la ventana.
    # Por defecto, las ventanas se crean ocultas en memoria.
    ventana.show()
    
    # 4. Iniciamos el 'Bucle de Eventos' (Event Loop).
    # app.exec() deja el programa rodando "en espera" de clics del ratón.
    # sys.exit(...) asegura que cuando cerremos la ventana, el proceso termine limpiamente.
    sys.exit(app.exec())