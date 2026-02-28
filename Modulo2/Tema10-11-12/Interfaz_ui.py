# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 469)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_titulo = QLabel(self.centralwidget)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_titulo)

        self.group_entrada = QGroupBox(self.centralwidget)
        self.group_entrada.setObjectName(u"group_entrada")
        self.formLayout = QFormLayout(self.group_entrada)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_line = QLabel(self.group_entrada)
        self.lbl_line.setObjectName(u"lbl_line")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_line)

        self.input_texto = QLineEdit(self.group_entrada)
        self.input_texto.setObjectName(u"input_texto")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_texto)

        self.lbl_spin = QLabel(self.group_entrada)
        self.lbl_spin.setObjectName(u"lbl_spin")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_spin)

        self.input_numero = QSpinBox(self.group_entrada)
        self.input_numero.setObjectName(u"input_numero")
        self.input_numero.setMinimum(18)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_numero)


        self.verticalLayout.addWidget(self.group_entrada)

        self.group_selectores = QGroupBox(self.centralwidget)
        self.group_selectores.setObjectName(u"group_selectores")
        self.verticalLayout_2 = QVBoxLayout(self.group_selectores)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_combo = QLabel(self.group_selectores)
        self.lbl_combo.setObjectName(u"lbl_combo")

        self.verticalLayout_2.addWidget(self.lbl_combo)

        self.combo_opciones = QComboBox(self.group_selectores)
        self.combo_opciones.addItem("")
        self.combo_opciones.addItem("")
        self.combo_opciones.setObjectName(u"combo_opciones")

        self.verticalLayout_2.addWidget(self.combo_opciones)

        self.check_opcion = QCheckBox(self.group_selectores)
        self.check_opcion.setObjectName(u"check_opcion")
        self.check_opcion.setChecked(True)

        self.verticalLayout_2.addWidget(self.check_opcion)


        self.verticalLayout.addWidget(self.group_selectores)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_accion = QPushButton(self.centralwidget)
        self.btn_accion.setObjectName(u"btn_accion")

        self.verticalLayout.addWidget(self.btn_accion)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tema 10: Mapa de Widgets", None))
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"Hola, soy un Label (Etiqueta de Texto)", None))
        self.group_entrada.setTitle(QCoreApplication.translate("MainWindow", u"Esto es un GroupBox (Agrupa elementos)", None))
        self.lbl_line.setText(QCoreApplication.translate("MainWindow", u"Label:", None))
        self.input_texto.setText(QCoreApplication.translate("MainWindow", u"Soy un LineEdit (Texto corto)", None))
        self.lbl_spin.setText(QCoreApplication.translate("MainWindow", u"Label:", None))
        self.input_numero.setSuffix(QCoreApplication.translate("MainWindow", u" (Soy un SpinBox)", None))
        self.group_selectores.setTitle(QCoreApplication.translate("MainWindow", u"Otro GroupBox (Para organizar)", None))
        self.lbl_combo.setText(QCoreApplication.translate("MainWindow", u"Abajo ver\u00e1s un ComboBox (Lista desplegable):", None))
        self.combo_opciones.setItemText(0, QCoreApplication.translate("MainWindow", u"Soy un ComboBox (Opci\u00f3n 1)", None))
        self.combo_opciones.setItemText(1, QCoreApplication.translate("MainWindow", u"Soy un ComboBox (Opci\u00f3n 2)", None))

        self.check_opcion.setText(QCoreApplication.translate("MainWindow", u"Soy un CheckBox (Marca esta casilla)", None))
        self.btn_accion.setText(QCoreApplication.translate("MainWindow", u"Soy un PushButton (\u00a1Haz clic aqu\u00ed!)", None))
    # retranslateUi

