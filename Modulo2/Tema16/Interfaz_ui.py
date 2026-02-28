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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 500)
        self.action_salir = QAction(MainWindow)
        self.action_salir.setObjectName(u"action_salir")
        self.action_nuevo = QAction(MainWindow)
        self.action_nuevo.setObjectName(u"action_nuevo")
        self.action_acerca_de = QAction(MainWindow)
        self.action_acerca_de.setObjectName(u"action_acerca_de")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_inventario = QWidget()
        self.tab_inventario.setObjectName(u"tab_inventario")
        self.verticalLayout_tab1 = QVBoxLayout(self.tab_inventario)
        self.verticalLayout_tab1.setObjectName(u"verticalLayout_tab1")
        self.label_info = QLabel(self.tab_inventario)
        self.label_info.setObjectName(u"label_info")
        font = QFont()
        font.setBold(True)
        self.label_info.setFont(font)

        self.verticalLayout_tab1.addWidget(self.label_info)

        self.tabla_productos = QTableWidget(self.tab_inventario)
        if (self.tabla_productos.columnCount() < 4):
            self.tabla_productos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabla_productos.setObjectName(u"tabla_productos")
        self.tabla_productos.setAlternatingRowColors(True)
        self.tabla_productos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_tab1.addWidget(self.tabla_productos)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_agregar = QPushButton(self.tab_inventario)
        self.btn_agregar.setObjectName(u"btn_agregar")

        self.horizontalLayout.addWidget(self.btn_agregar)

        self.btn_eliminar = QPushButton(self.tab_inventario)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_eliminar)


        self.verticalLayout_tab1.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_inventario, "")
        self.tab_detalle = QWidget()
        self.tab_detalle.setObjectName(u"tab_detalle")
        self.formLayout = QFormLayout(self.tab_detalle)
        self.formLayout.setObjectName(u"formLayout")
        self.label_nota = QLabel(self.tab_detalle)
        self.label_nota.setObjectName(u"label_nota")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_nota)

        self.txt_notas = QTextEdit(self.tab_detalle)
        self.txt_notas.setObjectName(u"txt_notas")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_notas)

        self.btn_guardar_notas = QPushButton(self.tab_detalle)
        self.btn_guardar_notas.setObjectName(u"btn_guardar_notas")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.btn_guardar_notas)

        self.tabWidget.addTab(self.tab_detalle, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 33))
        self.menu_archivo = QMenu(self.menubar)
        self.menu_archivo.setObjectName(u"menu_archivo")
        self.menu_ayuda = QMenu(self.menubar)
        self.menu_ayuda.setObjectName(u"menu_ayuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_archivo.menuAction())
        self.menubar.addAction(self.menu_ayuda.menuAction())
        self.menu_archivo.addAction(self.action_nuevo)
        self.menu_archivo.addSeparator()
        self.menu_archivo.addAction(self.action_salir)
        self.menu_ayuda.addAction(self.action_acerca_de)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tema 16: Tablas, Men\u00fas y Pesta\u00f1as", None))
        self.action_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.action_salir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo Inventario", None))
        self.action_acerca_de.setText(QCoreApplication.translate("MainWindow", u"Acerca de...", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"Listado de productos disponibles (QTableWidget)", None))
        ___qtablewidgetitem = self.tabla_productos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tabla_productos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem2 = self.tabla_productos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda", None));
        ___qtablewidgetitem3 = self.tabla_productos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Precio ($)", None));
        self.btn_agregar.setText(QCoreApplication.translate("MainWindow", u"+ A\u00f1adir Fila", None))
        self.btn_eliminar.setText(QCoreApplication.translate("MainWindow", u"- Eliminar Fila", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inventario), QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.label_nota.setText(QCoreApplication.translate("MainWindow", u"Notas adicionales:", None))
        self.btn_guardar_notas.setText(QCoreApplication.translate("MainWindow", u"Guardar Notas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_detalle), QCoreApplication.translate("MainWindow", u"Detalles / Notas", None))
        self.menu_archivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menu_ayuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

