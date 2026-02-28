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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(338, 436)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pantalla = QLineEdit(self.centralwidget)
        self.pantalla.setObjectName(u"pantalla")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.pantalla.setFont(font)
        self.pantalla.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pantalla.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.pantalla.setReadOnly(True)

        self.verticalLayout.addWidget(self.pantalla)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_borrar = QPushButton(self.centralwidget)
        self.btn_borrar.setObjectName(u"btn_borrar")
        self.btn_borrar.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn_borrar, 0, 0, 1, 3)

        self.btn_dividir = QPushButton(self.centralwidget)
        self.btn_dividir.setObjectName(u"btn_dividir")

        self.gridLayout.addWidget(self.btn_dividir, 0, 3, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_multiplicar = QPushButton(self.centralwidget)
        self.btn_multiplicar.setObjectName(u"btn_multiplicar")

        self.gridLayout.addWidget(self.btn_multiplicar, 1, 3, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_restar = QPushButton(self.centralwidget)
        self.btn_restar.setObjectName(u"btn_restar")

        self.gridLayout.addWidget(self.btn_restar, 2, 3, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_sumar = QPushButton(self.centralwidget)
        self.btn_sumar.setObjectName(u"btn_sumar")

        self.gridLayout.addWidget(self.btn_sumar, 3, 3, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")

        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 2)

        self.btn_igual = QPushButton(self.centralwidget)
        self.btn_igual.setObjectName(u"btn_igual")
        self.btn_igual.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn_igual, 4, 2, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora - Tema 13", None))
        self.pantalla.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_borrar.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_dividir.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_multiplicar.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_restar.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_sumar.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

