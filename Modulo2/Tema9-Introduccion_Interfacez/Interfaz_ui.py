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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MiPrograma(object):
    def setupUi(self, MiPrograma):
        if not MiPrograma.objectName():
            MiPrograma.setObjectName(u"MiPrograma")
        MiPrograma.resize(678, 537)
        self.centralwidget = QWidget(MiPrograma)
        self.centralwidget.setObjectName(u"centralwidget")
        self.boton = QPushButton(self.centralwidget)
        self.boton.setObjectName(u"boton")
        self.boton.setGeometry(QRect(180, 120, 331, 251))
        palette = QPalette()
        brush = QBrush(QColor(44, 206, 255, 179))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        self.boton.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.boton.setFont(font)
        MiPrograma.setCentralWidget(self.centralwidget)

        self.retranslateUi(MiPrograma)

        QMetaObject.connectSlotsByName(MiPrograma)
    # setupUi

    def retranslateUi(self, MiPrograma):
        MiPrograma.setWindowTitle(QCoreApplication.translate("MiPrograma", u"Mi Primer Interfaz", None))
        self.boton.setText(QCoreApplication.translate("MiPrograma", u"Pulsame", None))
    # retranslateUi

