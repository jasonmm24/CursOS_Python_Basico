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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QDoubleSpinBox, QFormLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 563)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_titulo = QLabel(self.centralwidget)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_titulo)

        self.btn_calculadora = QPushButton(self.centralwidget)
        self.btn_calculadora.setObjectName(u"btn_calculadora")

        self.verticalLayout.addWidget(self.btn_calculadora)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_registro = QWidget()
        self.tab_registro.setObjectName(u"tab_registro")
        self.verticalLayout_tab1 = QVBoxLayout(self.tab_registro)
        self.verticalLayout_tab1.setObjectName(u"verticalLayout_tab1")
        self.group_datos = QGroupBox(self.tab_registro)
        self.group_datos.setObjectName(u"group_datos")
        self.formLayout = QFormLayout(self.group_datos)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_fecha = QLabel(self.group_datos)
        self.lbl_fecha.setObjectName(u"lbl_fecha")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_fecha)

        self.date_gasto = QDateEdit(self.group_datos)
        self.date_gasto.setObjectName(u"date_gasto")
        self.date_gasto.setCalendarPopup(True)
        self.date_gasto.setDate(QDate(2025, 10, 1))

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.date_gasto)

        self.lbl_categoria = QLabel(self.group_datos)
        self.lbl_categoria.setObjectName(u"lbl_categoria")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_categoria)

        self.combo_categoria = QComboBox(self.group_datos)
        self.combo_categoria.addItem("")
        self.combo_categoria.addItem("")
        self.combo_categoria.addItem("")
        self.combo_categoria.addItem("")
        self.combo_categoria.addItem("")
        self.combo_categoria.addItem("")
        self.combo_categoria.addItem("")
        self.combo_categoria.setObjectName(u"combo_categoria")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.combo_categoria)

        self.lbl_desc = QLabel(self.group_datos)
        self.lbl_desc.setObjectName(u"lbl_desc")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_desc)

        self.input_descripcion = QLineEdit(self.group_datos)
        self.input_descripcion.setObjectName(u"input_descripcion")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_descripcion)

        self.lbl_monto = QLabel(self.group_datos)
        self.lbl_monto.setObjectName(u"lbl_monto")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_monto)

        self.spin_monto = QDoubleSpinBox(self.group_datos)
        self.spin_monto.setObjectName(u"spin_monto")
        self.spin_monto.setMaximum(99999.990000000005239)
        self.spin_monto.setSingleStep(10.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spin_monto)


        self.verticalLayout_tab1.addWidget(self.group_datos)

        self.btn_agregar = QPushButton(self.tab_registro)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_tab1.addWidget(self.btn_agregar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_tab1.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_registro, "")
        self.tab_historial = QWidget()
        self.tab_historial.setObjectName(u"tab_historial")
        self.verticalLayout_tab2 = QVBoxLayout(self.tab_historial)
        self.verticalLayout_tab2.setObjectName(u"verticalLayout_tab2")
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

        self.verticalLayout_tab2.addWidget(self.tabla_gastos)

        self.horizontalLayout_footer = QHBoxLayout()
        self.horizontalLayout_footer.setObjectName(u"horizontalLayout_footer")
        self.btn_eliminar = QPushButton(self.tab_historial)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.horizontalLayout_footer.addWidget(self.btn_eliminar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_footer.addItem(self.horizontalSpacer)

        self.lbl_limite_txt = QLabel(self.tab_historial)
        self.lbl_limite_txt.setObjectName(u"lbl_limite_txt")

        self.horizontalLayout_footer.addWidget(self.lbl_limite_txt)

        self.spin_limite = QDoubleSpinBox(self.tab_historial)
        self.spin_limite.setObjectName(u"spin_limite")
        self.spin_limite.setMaximum(999999.989999999990687)
        self.spin_limite.setValue(5000.000000000000000)

        self.horizontalLayout_footer.addWidget(self.spin_limite)

        self.lbl_total_texto = QLabel(self.tab_historial)
        self.lbl_total_texto.setObjectName(u"lbl_total_texto")
        font1 = QFont()
        font1.setBold(True)
        self.lbl_total_texto.setFont(font1)

        self.horizontalLayout_footer.addWidget(self.lbl_total_texto)

        self.lbl_total_valor = QLabel(self.tab_historial)
        self.lbl_total_valor.setObjectName(u"lbl_total_valor")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.lbl_total_valor.setFont(font2)

        self.horizontalLayout_footer.addWidget(self.lbl_total_valor)


        self.verticalLayout_tab2.addLayout(self.horizontalLayout_footer)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Proyecto Final: Gestor de Gastos", None))
        self.lbl_titulo.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #2c3e50; margin: 10px;", None))
        self.lbl_titulo.setText(QCoreApplication.translate("MainWindow", u"Control de Finanzas", None))
        self.btn_calculadora.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #8e44ad; color: white; padding: 5px; border-radius: 3px;", None))
        self.btn_calculadora.setText(QCoreApplication.translate("MainWindow", u"Abrir Calculadora", None))
        self.group_datos.setTitle(QCoreApplication.translate("MainWindow", u"Detalles de la Compra", None))
        self.lbl_fecha.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.lbl_categoria.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda:", None))
        self.combo_categoria.setItemText(0, QCoreApplication.translate("MainWindow", u"Alimentaci\u00f3n", None))
        self.combo_categoria.setItemText(1, QCoreApplication.translate("MainWindow", u"Transporte", None))
        self.combo_categoria.setItemText(2, QCoreApplication.translate("MainWindow", u"Ocio / Entretenimiento", None))
        self.combo_categoria.setItemText(3, QCoreApplication.translate("MainWindow", u"Servicios (Luz/Agua)", None))
        self.combo_categoria.setItemText(4, QCoreApplication.translate("MainWindow", u"Ropa", None))
        self.combo_categoria.setItemText(5, QCoreApplication.translate("MainWindow", u"Salud", None))
        self.combo_categoria.setItemText(6, QCoreApplication.translate("MainWindow", u"Otros", None))

        self.lbl_desc.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.input_descripcion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej: Supermercado semanal", None))
        self.lbl_monto.setText(QCoreApplication.translate("MainWindow", u"Monto ($):", None))
        self.btn_agregar.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #27ae60; color: white; font-weight: bold; padding: 10px; border-radius: 5px;", None))
        self.btn_agregar.setText(QCoreApplication.translate("MainWindow", u"Registrar Gasto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_registro), QCoreApplication.translate("MainWindow", u"+ Nuevo Gasto", None))
        ___qtablewidgetitem = self.tabla_gastos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem1 = self.tabla_gastos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda", None));
        ___qtablewidgetitem2 = self.tabla_gastos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None));
        ___qtablewidgetitem3 = self.tabla_gastos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Monto ($)", None));
        self.btn_eliminar.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #c0392b; border: 1px solid #c0392b; padding: 5px; border-radius: 3px;", None))
        self.btn_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar Seleccionado", None))
        self.lbl_limite_txt.setText(QCoreApplication.translate("MainWindow", u"L\u00edmite Alerta ($):", None))
        self.lbl_total_texto.setText(QCoreApplication.translate("MainWindow", u"TOTAL GASTADO:", None))
        self.lbl_total_valor.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: #2980b9;", None))
        self.lbl_total_valor.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_historial), QCoreApplication.translate("MainWindow", u"Historial y Resumen", None))
    # retranslateUi

