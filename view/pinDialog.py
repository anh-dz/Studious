# Form implementation generated from reading ui file 'pinDialog.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(653, 219)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assert/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(33, 37, 43);\n"
"color: rgb(249, 245, 246);\n"
"font: 18pt \"Arial\";\n"
"qproperty-alignment: \'AlignCenter\';\n"
"qproperty-margin: auto;\n"
"")
        self.lb_task = QtWidgets.QLabel(parent=Dialog)
        self.lb_task.setGeometry(QtCore.QRect(30, 10, 591, 91))
        self.lb_task.setObjectName("lb_task")
        self.lb_time = QtWidgets.QLabel(parent=Dialog)
        self.lb_time.setGeometry(QtCore.QRect(30, 120, 591, 91))
        self.lb_time.setObjectName("lb_time")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Studious - Pin Task "))
        self.lb_task.setText(_translate("Dialog", "TASK"))
        self.lb_time.setText(_translate("Dialog", "TIME"))
