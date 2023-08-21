# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pinDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(480, 88)
        icon = QIcon()
        icon.addFile(u"assert/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"color: rgb(249, 245, 246);\n"
"font: 18pt \"Arial\";\n"
"qproperty-alignment: 'AlignCenter';\n"
"qproperty-margin: auto;\n"
"")
        self.lb_task = QLabel(Dialog)
        self.lb_task.setObjectName(u"lb_task")
        self.lb_task.setGeometry(QRect(0, 0, 240, 90))
        self.lb_time = QLabel(Dialog)
        self.lb_time.setObjectName(u"lb_time")
        self.lb_time.setGeometry(QRect(240, 0, 240, 90))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Studious - Pin Task ", None))
        self.lb_task.setText(QCoreApplication.translate("Dialog", u"TASK", None))
        self.lb_time.setText(QCoreApplication.translate("Dialog", u"TIME", None))
    # retranslateUi

