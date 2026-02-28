# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gastos.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDoubleSpinBox, QFormLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_titulo = QLabel(self.centralwidget)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_titulo)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_registro = QWidget()
        self.tab_registro.setObjectName(u"tab_registro")
        self.verticalLayout_2 = QVBoxLayout(self.tab_registro)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.group_datos = QGroupBox(self.tab_registro)
        self.group_datos.setObjectName(u"group_datos")
        self.formLayout = QFormLayout(self.group_datos)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.group_datos)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.date_gasto = QDateEdit(self.group_datos)
        self.date_gasto.setObjectName(u"date_gasto")
        self.date_gasto.setCalendarPopup(True)
        self.date_gasto.setDate(QDate(2025, 1, 1))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.date_gasto)

        self.label_2 = QLabel(self.group_datos)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.combo_categoria = QComboBox(self.group_datos)
        self.combo_categoria.addItem("")
        self.combo_categoria.addItem("")
        self.combo_categoria.addItem("")
        self.combo_categoria.addItem("")
        self.combo_categoria.addItem("")
        self.combo_categoria.addItem("")
        self.combo_categoria.setObjectName(u"combo_categoria")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.combo_categoria)

        self.label_3 = QLabel(self.group_datos)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.input_descripcion = QLineEdit(self.group_datos)
        self.input_descripcion.setObjectName(u"input_descripcion")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_descripcion)

        self.label_4 = QLabel(self.group_datos)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.spin_monto = QDoubleSpinBox(self.group_datos)
        self.spin_monto.setObjectName(u"spin_monto")
        self.spin_monto.setMaximum(99999.990000000005239)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spin_monto)


        self.verticalLayout_2.addWidget(self.group_datos)

        self.btn_agregar = QPushButton(self.tab_registro)
        self.btn_agregar.setObjectName(u"btn_agregar")

        self.verticalLayout_2.addWidget(self.btn_agregar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_registro, "")
        self.tab_historial = QWidget()
        self.tab_historial.setObjectName(u"tab_historial")
        self.verticalLayout_3 = QVBoxLayout(self.tab_historial)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_filtro = QHBoxLayout()
        self.horizontalLayout_filtro.setObjectName(u"horizontalLayout_filtro")
        self.label_filtro = QLabel(self.tab_historial)
        self.label_filtro.setObjectName(u"label_filtro")
        font1 = QFont()
        font1.setBold(True)
        self.label_filtro.setFont(font1)

        self.horizontalLayout_filtro.addWidget(self.label_filtro)

        self.combo_filtro = QComboBox(self.tab_historial)
        self.combo_filtro.addItem("")
        self.combo_filtro.addItem("")
        self.combo_filtro.addItem("")
        self.combo_filtro.addItem("")
        self.combo_filtro.addItem("")
        self.combo_filtro.addItem("")
        self.combo_filtro.addItem("")
        self.combo_filtro.setObjectName(u"combo_filtro")

        self.horizontalLayout_filtro.addWidget(self.combo_filtro)


        self.verticalLayout_3.addLayout(self.horizontalLayout_filtro)

        self.tabla_gastos = QTableWidget(self.tab_historial)
        if (self.tabla_gastos.columnCount() < 4):
            self.tabla_gastos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_gastos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_gastos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_gastos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_gastos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabla_gastos.setObjectName(u"tabla_gastos")
        self.tabla_gastos.setAlternatingRowColors(True)
        self.tabla_gastos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_3.addWidget(self.tabla_gastos)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_eliminar = QPushButton(self.tab_historial)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.horizontalLayout.addWidget(self.btn_eliminar)

        self.btn_calculadora = QPushButton(self.tab_historial)
        self.btn_calculadora.setObjectName(u"btn_calculadora")

        self.horizontalLayout.addWidget(self.btn_calculadora)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.tab_historial)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.spin_limite = QDoubleSpinBox(self.tab_historial)
        self.spin_limite.setObjectName(u"spin_limite")
        self.spin_limite.setMaximum(999999.989999999990687)
        self.spin_limite.setValue(5000.000000000000000)

        self.horizontalLayout.addWidget(self.spin_limite)

        self.lbl_total_valor = QLabel(self.tab_historial)
        self.lbl_total_valor.setObjectName(u"lbl_total_valor")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.lbl_total_valor.setFont(font2)

        self.horizontalLayout.addWidget(self.lbl_total_valor)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.check_oscuro = QCheckBox(self.tab_historial)
        self.check_oscuro.setObjectName(u"check_oscuro")
        font3 = QFont()
        font3.setItalic(True)
        self.check_oscuro.setFont(font3)

        self.verticalLayout_3.addWidget(self.check_oscuro)

        self.tabWidget.addTab(self.tab_historial, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gestor de Gastos Pro", None))
        self.lbl_titulo.setStyleSheet(QCoreApplication.translate("MainWindow", u"margin: 10px; color: #2c3e50;", None))
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"Control de Finanzas Personal", None))
        self.group_datos.setTitle(QCoreApplication.translate("MainWindow", u"Detalles", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda:", None))
        self.combo_categoria.setItemText(0, QCoreApplication.translate("MainWindow", u"Alimentaci\u00f3n", None))
        self.combo_categoria.setItemText(1, QCoreApplication.translate("MainWindow", u"Transporte", None))
        self.combo_categoria.setItemText(2, QCoreApplication.translate("MainWindow", u"Ocio", None))
        self.combo_categoria.setItemText(3, QCoreApplication.translate("MainWindow", u"Servicios", None))
        self.combo_categoria.setItemText(4, QCoreApplication.translate("MainWindow", u"Salud", None))
        self.combo_categoria.setItemText(5, QCoreApplication.translate("MainWindow", u"Otros", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Monto ($):", None))
        self.btn_agregar.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #27ae60; color: white; padding: 10px; font-weight: bold;", None))
        self.btn_agregar.setText(QCoreApplication.translate("MainWindow", u"Registrar Gasto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_registro), QCoreApplication.translate("MainWindow", u"+ Nuevo Gasto", None))
        self.label_filtro.setText(QCoreApplication.translate("MainWindow", u"Filtrar por Categor\u00eda:", None))
        self.combo_filtro.setItemText(0, QCoreApplication.translate("MainWindow", u"Todas", None))
        self.combo_filtro.setItemText(1, QCoreApplication.translate("MainWindow", u"Alimentaci\u00f3n", None))
        self.combo_filtro.setItemText(2, QCoreApplication.translate("MainWindow", u"Transporte", None))
        self.combo_filtro.setItemText(3, QCoreApplication.translate("MainWindow", u"Ocio", None))
        self.combo_filtro.setItemText(4, QCoreApplication.translate("MainWindow", u"Servicios", None))
        self.combo_filtro.setItemText(5, QCoreApplication.translate("MainWindow", u"Salud", None))
        self.combo_filtro.setItemText(6, QCoreApplication.translate("MainWindow", u"Otros", None))

        ___qtablewidgetitem = self.tabla_gastos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem1 = self.tabla_gastos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda", None));
        ___qtablewidgetitem2 = self.tabla_gastos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None));
        ___qtablewidgetitem3 = self.tabla_gastos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Monto ($)", None));
        self.btn_eliminar.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: red; border: 1px solid red; padding: 5px;", None))
        self.btn_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btn_calculadora.setText(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"L\u00edmite:", None))
        self.lbl_total_valor.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.check_oscuro.setText(QCoreApplication.translate("MainWindow", u"Activar Modo Oscuro (Dark Theme)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_historial), QCoreApplication.translate("MainWindow", u"Historial", None))
    # retranslateUi

