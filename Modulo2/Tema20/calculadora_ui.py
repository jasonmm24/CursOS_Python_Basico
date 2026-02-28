# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
#
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(250, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pantalla = QLineEdit(Form)
        self.pantalla.setObjectName(u"pantalla")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.pantalla.setFont(font)
        self.pantalla.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pantalla.setReadOnly(True)

        self.verticalLayout.addWidget(self.pantalla)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_7 = QPushButton(Form)
        self.btn_7.setObjectName(u"btn_7")

        self.gridLayout.addWidget(self.btn_7, 0, 0, 1, 1)

        self.btn_8 = QPushButton(Form)
        self.btn_8.setObjectName(u"btn_8")

        self.gridLayout.addWidget(self.btn_8, 0, 1, 1, 1)

        self.btn_9 = QPushButton(Form)
        self.btn_9.setObjectName(u"btn_9")

        self.gridLayout.addWidget(self.btn_9, 0, 2, 1, 1)

        self.btn_div = QPushButton(Form)
        self.btn_div.setObjectName(u"btn_div")

        self.gridLayout.addWidget(self.btn_div, 0, 3, 1, 1)

        self.btn_4 = QPushButton(Form)
        self.btn_4.setObjectName(u"btn_4")

        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_5 = QPushButton(Form)
        self.btn_5.setObjectName(u"btn_5")

        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_6 = QPushButton(Form)
        self.btn_6.setObjectName(u"btn_6")

        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_mul = QPushButton(Form)
        self.btn_mul.setObjectName(u"btn_mul")

        self.gridLayout.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_1 = QPushButton(Form)
        self.btn_1.setObjectName(u"btn_1")

        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)

        self.btn_2 = QPushButton(Form)
        self.btn_2.setObjectName(u"btn_2")

        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)

        self.btn_3 = QPushButton(Form)
        self.btn_3.setObjectName(u"btn_3")

        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)

        self.btn_resta = QPushButton(Form)
        self.btn_resta.setObjectName(u"btn_resta")

        self.gridLayout.addWidget(self.btn_resta, 2, 3, 1, 1)

        self.btn_c = QPushButton(Form)
        self.btn_c.setObjectName(u"btn_c")

        self.gridLayout.addWidget(self.btn_c, 3, 0, 1, 1)

        self.btn_0 = QPushButton(Form)
        self.btn_0.setObjectName(u"btn_0")

        self.gridLayout.addWidget(self.btn_0, 3, 1, 1, 1)

        self.btn_igual = QPushButton(Form)
        self.btn_igual.setObjectName(u"btn_igual")

        self.gridLayout.addWidget(self.btn_igual, 3, 2, 1, 1)

        self.btn_suma = QPushButton(Form)
        self.btn_suma.setObjectName(u"btn_suma")

        self.gridLayout.addWidget(self.btn_suma, 3, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Calculadora", None))
        self.btn_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btn_div.setText(QCoreApplication.translate("Form", u"/", None))
        self.btn_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btn_mul.setText(QCoreApplication.translate("Form", u"*", None))
        self.btn_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btn_resta.setText(QCoreApplication.translate("Form", u"-", None))
        self.btn_c.setText(QCoreApplication.translate("Form", u"C", None))
        self.btn_c.setStyleSheet(QCoreApplication.translate("Form", u"color: red; font-weight: bold;", None))
        self.btn_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.btn_igual.setText(QCoreApplication.translate("Form", u"=", None))
        self.btn_igual.setStyleSheet(QCoreApplication.translate("Form", u"color: green; font-weight: bold;", None))
        self.btn_suma.setText(QCoreApplication.translate("Form", u"+", None))
    # retranslateUi

