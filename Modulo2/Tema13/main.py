import sys
from PySide6.QtWidgets import QApplication, QMainWindow
# Importamos la "piel" de la calculadora que creamos en Qt Designer
from Interfaz_ui import Ui_MainWindow

class Calculadora(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Construye la interfaz visual (botones, pantalla...)

        # ------------------------------------------------------------------
        # ZONA DE MEMORIA (ESTADO)
        # ------------------------------------------------------------------
        # Aquí definimos las variables que "recordarán" cosas entre clic y clic.
        
        # Guardará la operación seleccionada ('+', '-', '*', '/')
        self.operacion_pendiente = None  
        
        # Guardará el primer número que escriba el usuario (ej: el 10 en "10 + 5")
        self.numero_anterior = 0         
        
        # Es un "semáforo" (True/False). 
        # Si está en True, significa que al pulsar un número, debemos borrar 
        # la pantalla antes de escribir (porque estamos empezando el segundo número).
        self.reiniciar_pantalla = False  

        # ------------------------------------------------------------------
        # ZONA DE CONEXIONES (CABLES)
        # ------------------------------------------------------------------
        
        # TRUCO PRO: Uso de 'lambda'
        # Problema: Tenemos 10 botones. ¿Creamos 10 funciones distintas? ¡No!
        # Solución: Usamos 'lambda'. Es una forma de decir:
        # "Cuando hagas clic, llama a la función 'ingresar_numero' PERO envíale este valor específico".
        
        self.btn_0.clicked.connect(lambda: self.ingresar_numero("0"))
        self.btn_1.clicked.connect(lambda: self.ingresar_numero("1"))
        self.btn_2.clicked.connect(lambda: self.ingresar_numero("2"))
        # ... (así con todos los números) ...
        self.btn_3.clicked.connect(lambda: self.ingresar_numero("3"))
        self.btn_4.clicked.connect(lambda: self.ingresar_numero("4"))
        self.btn_5.clicked.connect(lambda: self.ingresar_numero("5"))
        self.btn_6.clicked.connect(lambda: self.ingresar_numero("6"))
        self.btn_7.clicked.connect(lambda: self.ingresar_numero("7"))
        self.btn_8.clicked.connect(lambda: self.ingresar_numero("8"))
        self.btn_9.clicked.connect(lambda: self.ingresar_numero("9"))
        
        

        # Conectamos los botones de operación (+, -, *, /)
        self.btn_sumar.clicked.connect(lambda: self.definir_operacion("+"))
        self.btn_restar.clicked.connect(lambda: self.definir_operacion("-"))
        self.btn_multiplicar.clicked.connect(lambda: self.definir_operacion("*"))
        self.btn_dividir.clicked.connect(lambda: self.definir_operacion("/"))

        # Conectamos el Igual (=) y el Borrar (C)
        self.btn_igual.clicked.connect(self.calcular_resultado)
        self.btn_borrar.clicked.connect(self.borrar_todo)
    # ----------------------------------------------------------------------
    # ZONA DE LÓGICA (CEREBRO)
    # ----------------------------------------------------------------------

    def ingresar_numero(self, digito):
        """Función que recibe el número del botón pulsado y lo pone en pantalla."""
        texto_actual = self.pantalla.text()

        # CASO A: El usuario acaba de pulsar una operación (+, -...)
        # Debemos limpiar la pantalla para que escriba el segundo número.
        if self.reiniciar_pantalla == True:
            self.pantalla.setText(digito)
            self.reiniciar_pantalla = False # Ya limpiamos, bajamos la bandera.
        
        # CASO B: La pantalla tiene un "0" inicial. Lo quitamos y ponemos el número.
        elif texto_actual == "0":
            self.pantalla.setText(digito)
        
        # CASO C: Comportamiento normal. Concatenamos (pegamos) el número al final.
        # Si hay un "1" y pulso "2", se convierte en "12".
        else:
            self.pantalla.setText(texto_actual + digito)

    def definir_operacion(self, operador):
        """Se ejecuta al pulsar +, -, * o /"""
        # 1. Guardamos el número que hay en pantalla en nuestra MEMORIA (numero_anterior)
        # Convertimos a float para poder hacer matemáticas con él.
        self.numero_anterior = float(self.pantalla.text())
        
        # 2. Guardamos qué operación quiere hacer el usuario (ej: "+")
        self.operacion_pendiente = operador
        
        # 3. Levantamos la bandera: "¡Oye! El próximo número que se escriba 
        # debe borrar lo que hay en pantalla primero".
        self.reiniciar_pantalla = True

    def calcular_resultado(self):
        """Se ejecuta al pulsar '='. Aquí ocurre la magia matemática."""
        # Si no hay operación pendiente, no hacemos nada.
        if self.operacion_pendiente is None:
            return

        # Obtenemos el SEGUNDO número (el que está ahora mismo en pantalla)
        numero_actual = float(self.pantalla.text())
        resultado = 0

        # Lógica condicional básica (Tema 2 del curso)
        if self.operacion_pendiente == "+":
            resultado = self.numero_anterior + numero_actual
        elif self.operacion_pendiente == "-":
            resultado = self.numero_anterior - numero_actual
        elif self.operacion_pendiente == "*":
            resultado = self.numero_anterior * numero_actual
        elif self.operacion_pendiente == "/":
            # Manejo de errores: No se puede dividir por cero
            if numero_actual == 0:
                self.pantalla.setText("Syntax Error")
                self.reiniciar_pantalla = True
                return
            resultado = self.numero_anterior / numero_actual

        # Mostramos el resultado en pantalla.
        # Truco estético: Si es 5.0, mostramos 5. Si es 5.5, mostramos 5.5
        if resultado.is_integer():
            self.pantalla.setText(str(int(resultado)))
        else:
            self.pantalla.setText(str(resultado))

        # Importante: No borramos 'numero_anterior' inmediatamente para permitir
        # operaciones encadenadas, pero reseteamos la operación pendiente.
        self.operacion_pendiente = None
        self.reiniciar_pantalla = True

    def borrar_todo(self):
        """Botón C: Resetea todo como si cerraras y abrieras la app."""
        self.pantalla.setText("0")
        self.numero_anterior = 0
        self.operacion_pendiente = None
        self.reiniciar_pantalla = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())