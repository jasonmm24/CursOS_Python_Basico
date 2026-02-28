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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 550)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_main = QVBoxLayout(self.centralwidget)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.group_genero = QGroupBox(self.centralwidget)
        self.group_genero.setObjectName(u"group_genero")
        self.verticalLayout_radio = QVBoxLayout(self.group_genero)
        self.verticalLayout_radio.setObjectName(u"verticalLayout_radio")
        self.lbl_pregunta1 = QLabel(self.group_genero)
        self.lbl_pregunta1.setObjectName(u"lbl_pregunta1")

        self.verticalLayout_radio.addWidget(self.lbl_pregunta1)

        self.rb_principiante = QRadioButton(self.group_genero)
        self.rb_principiante.setObjectName(u"rb_principiante")
        self.rb_principiante.setChecked(True)

        self.verticalLayout_radio.addWidget(self.rb_principiante)

        self.rb_intermedio = QRadioButton(self.group_genero)
        self.rb_intermedio.setObjectName(u"rb_intermedio")

        self.verticalLayout_radio.addWidget(self.rb_intermedio)

        self.rb_avanzado = QRadioButton(self.group_genero)
        self.rb_avanzado.setObjectName(u"rb_avanzado")

        self.verticalLayout_radio.addWidget(self.rb_avanzado)


        self.verticalLayout_main.addWidget(self.group_genero)

        self.group_pais = QGroupBox(self.centralwidget)
        self.group_pais.setObjectName(u"group_pais")
        self.horizontalLayout_combo = QHBoxLayout(self.group_pais)
        self.horizontalLayout_combo.setObjectName(u"horizontalLayout_combo")
        self.lbl_pais = QLabel(self.group_pais)
        self.lbl_pais.setObjectName(u"lbl_pais")

        self.horizontalLayout_combo.addWidget(self.lbl_pais)

        self.combo_ciudades = QComboBox(self.group_pais)
        self.combo_ciudades.addItem("")
        self.combo_ciudades.addItem("")
        self.combo_ciudades.addItem("")
        self.combo_ciudades.addItem("")
        self.combo_ciudades.addItem("")
        self.combo_ciudades.setObjectName(u"combo_ciudades")
        self.combo_ciudades.setEditable(False)

        self.horizontalLayout_combo.addWidget(self.combo_ciudades)


        self.verticalLayout_main.addWidget(self.group_pais)

        self.group_lenguajes = QGroupBox(self.centralwidget)
        self.group_lenguajes.setObjectName(u"group_lenguajes")
        self.verticalLayout_list = QVBoxLayout(self.group_lenguajes)
        self.verticalLayout_list.setObjectName(u"verticalLayout_list")
        self.lbl_lista = QLabel(self.group_lenguajes)
        self.lbl_lista.setObjectName(u"lbl_lista")

        self.verticalLayout_list.addWidget(self.lbl_lista)

        self.lista_items = QListWidget(self.group_lenguajes)
        QListWidgetItem(self.lista_items)
        QListWidgetItem(self.lista_items)
        QListWidgetItem(self.lista_items)
        QListWidgetItem(self.lista_items)
        QListWidgetItem(self.lista_items)
        self.lista_items.setObjectName(u"lista_items")
        self.lista_items.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.verticalLayout_list.addWidget(self.lista_items)

        self.lbl_info_lista = QLabel(self.group_lenguajes)
        self.lbl_info_lista.setObjectName(u"lbl_info_lista")
        font = QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.lbl_info_lista.setFont(font)

        self.verticalLayout_list.addWidget(self.lbl_info_lista)


        self.verticalLayout_main.addWidget(self.group_lenguajes)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_main.addItem(self.verticalSpacer)

        self.btn_confirmar = QPushButton(self.centralwidget)
        self.btn_confirmar.setObjectName(u"btn_confirmar")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_confirmar.setFont(font1)

        self.verticalLayout_main.addWidget(self.btn_confirmar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tema 14: Widgets Complejos", None))
        self.group_genero.setTitle(QCoreApplication.translate("MainWindow", u"1. RadioButton (Selecci\u00f3n \u00danica)", None))
        self.lbl_pregunta1.setText(QCoreApplication.translate("MainWindow", u"Selecciona tu nivel de experiencia:", None))
        self.rb_principiante.setText(QCoreApplication.translate("MainWindow", u"Principiante (0-1 a\u00f1os)", None))
        self.rb_intermedio.setText(QCoreApplication.translate("MainWindow", u"Intermedio (2-4 a\u00f1os)", None))
        self.rb_avanzado.setText(QCoreApplication.translate("MainWindow", u"Avanzado (5+ a\u00f1os)", None))
        self.group_pais.setTitle(QCoreApplication.translate("MainWindow", u"2. ComboBox (Lista Desplegable)", None))
        self.lbl_pais.setText(QCoreApplication.translate("MainWindow", u"Selecciona tu Ciudad:", None))
        self.combo_ciudades.setItemText(0, QCoreApplication.translate("MainWindow", u"Ciudad de M\u00e9xico", None))
        self.combo_ciudades.setItemText(1, QCoreApplication.translate("MainWindow", u"Bogot\u00e1", None))
        self.combo_ciudades.setItemText(2, QCoreApplication.translate("MainWindow", u"Buenos Aires", None))
        self.combo_ciudades.setItemText(3, QCoreApplication.translate("MainWindow", u"Madrid", None))
        self.combo_ciudades.setItemText(4, QCoreApplication.translate("MainWindow", u"Lima", None))

        self.group_lenguajes.setTitle(QCoreApplication.translate("MainWindow", u"3. ListWidget (Lista de Elementos)", None))
        self.lbl_lista.setText(QCoreApplication.translate("MainWindow", u"Lenguajes de programaci\u00f3n que conoces:", None))

        __sortingEnabled = self.lista_items.isSortingEnabled()
        self.lista_items.setSortingEnabled(False)
        ___qlistwidgetitem = self.lista_items.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Python", None));
        ___qlistwidgetitem1 = self.lista_items.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Java", None));
        ___qlistwidgetitem2 = self.lista_items.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"C++", None));
        ___qlistwidgetitem3 = self.lista_items.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"JavaScript", None));
        ___qlistwidgetitem4 = self.lista_items.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"C#", None));
        self.lista_items.setSortingEnabled(__sortingEnabled)

        self.lbl_info_lista.setText(QCoreApplication.translate("MainWindow", u"* Nota: Este ListWidget est\u00e1 configurado para permitir selecci\u00f3n m\u00faltiple.", None))
        self.btn_confirmar.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #e1f5fe; border: 1px solid #0288d1; border-radius: 5px; padding: 5px;", None))
        self.btn_confirmar.setText(QCoreApplication.translate("MainWindow", u"Confirmar Selecci\u00f3n (Ver Di\u00e1logo)", None))
    # retranslateUi

