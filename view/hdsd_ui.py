# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hdsd.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 470)
        self.labelImg = QLabel(Form)
        self.labelImg.setObjectName(u"labelImg")
        self.labelImg.setGeometry(QRect(0, 0, 750, 470))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(650, 380, 81, 81))
        self.pushButton.setStyleSheet(u"font: 72pt \"Arial\";\n"
"border: 0px;")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 380, 81, 81))
        self.pushButton_2.setStyleSheet(u"font: 72pt \"Arial\";\n"
"border: 0px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelImg.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u">", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"<", None))
    # retranslateUi

