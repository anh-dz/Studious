from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from . mainUI import Ui_Studious

class ViewControl(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Studious()
        self.ui.setupUi(self)

        # Connect the button click signal to the function
        self.ui.btn_lB_menu.clicked.connect(self.Side_Menu_Def_0)
        self.Side_Menu_Def_0()

    def Side_Menu_Def_0(self):
        if self.ui.wg_leftBar.width() <= 50:
            self.animation1 = QPropertyAnimation(self.ui.wg_leftBar, b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(40)
            self.animation1.setEndValue(200)
            self.animation1.setEasingCurve(QEasingCurve.Type.InOutSine)
            self.animation1.start()

            self.animation2 = QPropertyAnimation(self.ui.wg_leftBar, b"minimumWidth")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(40)
            self.animation2.setEndValue(200)
            self.animation2.setEasingCurve(QEasingCurve.Type.InOutSine)
            self.animation2.start()

        else:
            self.animation1 = QPropertyAnimation(self.ui.wg_leftBar, b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(200)
            self.animation1.setEndValue(40)
            self.animation1.setEasingCurve(QEasingCurve.Type.InOutSine)
            self.animation1.start()

            self.animation2 = QPropertyAnimation(self.ui.wg_leftBar, b"minimumWidth")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(200)
            self.animation2.setEndValue(40)
            self.animation2.setEasingCurve(QEasingCurve.Type.InOutSine)
            self.animation2.start()
