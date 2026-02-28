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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titulo = QLabel(self.centralwidget)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_titulo)

        self.group_nueva_tarea = QGroupBox(self.centralwidget)
        self.group_nueva_tarea.setObjectName(u"group_nueva_tarea")
        self.gridLayout = QGridLayout(self.group_nueva_tarea)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_descripcion = QLabel(self.group_nueva_tarea)
        self.lbl_descripcion.setObjectName(u"lbl_descripcion")

        self.gridLayout.addWidget(self.lbl_descripcion, 0, 0, 1, 1)

        self.input_tarea = QLineEdit(self.group_nueva_tarea)
        self.input_tarea.setObjectName(u"input_tarea")

        self.gridLayout.addWidget(self.input_tarea, 0, 1, 1, 2)

        self.lbl_prioridad = QLabel(self.group_nueva_tarea)
        self.lbl_prioridad.setObjectName(u"lbl_prioridad")

        self.gridLayout.addWidget(self.lbl_prioridad, 1, 0, 1, 1)

        self.combo_prioridad = QComboBox(self.group_nueva_tarea)
        icon = QIcon(QIcon.fromTheme(u"weather-storm"))
        self.combo_prioridad.addItem(icon, "")
        self.combo_prioridad.addItem("")
        self.combo_prioridad.addItem("")
        self.combo_prioridad.setObjectName(u"combo_prioridad")

        self.gridLayout.addWidget(self.combo_prioridad, 1, 1, 1, 1)

        self.date_limite = QDateEdit(self.group_nueva_tarea)
        self.date_limite.setObjectName(u"date_limite")
        self.date_limite.setCalendarPopup(True)
        self.date_limite.setDate(QDate(2025, 10, 1))

        self.gridLayout.addWidget(self.date_limite, 1, 2, 1, 1)

        self.btn_agregar = QPushButton(self.group_nueva_tarea)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_agregar.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn_agregar, 2, 0, 1, 3)


        self.verticalLayout.addWidget(self.group_nueva_tarea)

        self.lista_tareas = QListWidget(self.centralwidget)
        self.lista_tareas.setObjectName(u"lista_tareas")
        font1 = QFont()
        font1.setPointSize(10)
        self.lista_tareas.setFont(font1)
        self.lista_tareas.setAlternatingRowColors(True)
        self.lista_tareas.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.verticalLayout.addWidget(self.lista_tareas)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_eliminar = QPushButton(self.centralwidget)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_eliminar)

        self.btn_limpiar = QPushButton(self.centralwidget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")

        self.horizontalLayout.addWidget(self.btn_limpiar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_contador = QLabel(self.centralwidget)
        self.lbl_contador.setObjectName(u"lbl_contador")
        font2 = QFont()
        font2.setItalic(True)
        self.lbl_contador.setFont(font2)
        self.lbl_contador.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_contador)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tema 15: Gestor de Tareas (To-Do List)", None))
        self.label_titulo.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #2c3e50; margin-bottom: 10px;", None))
        self.label_titulo.setText(QCoreApplication.translate("MainWindow", u"Mis Tareas Pendientes", None))
        self.group_nueva_tarea.setStyleSheet(QCoreApplication.translate("MainWindow", u"QGroupBox { font-weight: bold; border: 1px solid gray; border-radius: 5px; margin-top: 10px; } QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px; }", None))
        self.group_nueva_tarea.setTitle(QCoreApplication.translate("MainWindow", u"Nueva Tarea", None))
        self.lbl_descripcion.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.input_tarea.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej: Comprar leche...", None))
        self.lbl_prioridad.setText(QCoreApplication.translate("MainWindow", u"Prioridad:", None))
        self.combo_prioridad.setItemText(0, QCoreApplication.translate("MainWindow", u"Alta", None))
        self.combo_prioridad.setItemText(1, QCoreApplication.translate("MainWindow", u"Media", None))
        self.combo_prioridad.setItemText(2, QCoreApplication.translate("MainWindow", u"Baja", None))

        self.date_limite.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.btn_agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar Tarea", None))
        self.btn_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar Seleccionada", None))
        self.btn_limpiar.setText(QCoreApplication.translate("MainWindow", u"Borrar Todo", None))
        self.lbl_contador.setText(QCoreApplication.translate("MainWindow", u"Tareas pendientes: 0", None))
    # retranslateUi

