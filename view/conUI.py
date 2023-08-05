from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from . mainUI import Ui_Studious
from .colorFunc import create_colored_icon

class ViewControl(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Studious()
        self.ui.setupUi(self)

        self.ui.pushButton.hide()
        self.ui.pushButton.clicked.connect(self.Side_Menu_Def_0)

        self.ui.btn_lB_1.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(0))
        self.ui.btn_lB_2.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(1))
        self.ui.btn_lB_3.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(2))
        self.ui.btn_lB_4.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(3))
        self.ui.btn_lB_5.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(4))
        self.ui.btn_lB_6.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(5))
        self.ui.btn_lB_7.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(6))

        self.ui.btn_lB_menu.clicked.connect(self.Side_Menu_Def_0)
        self.Side_Menu_Def_0()

        self.testComboBoxColor()

    def Side_Menu_Def_0(self):
        if self.ui.wg_leftBar.width() <= 70:
            self.animation1 = QPropertyAnimation(self.ui.wg_leftBar, b"maximumWidth")
            self.animation1.setDuration(250)
            self.animation1.setStartValue(44)
            self.animation1.setEndValue(150)
            self.animation1.setEasingCurve(QEasingCurve.Type.InOutSine)
            self.animation1.start()

            self.animation2 = QPropertyAnimation(self.ui.wg_leftBar, b"minimumWidth")
            self.animation2.setDuration(250)
            self.animation2.setStartValue(44)
            self.animation2.setEndValue(150)
            self.animation2.setEasingCurve(QEasingCurve.Type.InOutSine)
            self.animation2.start()
            self.ui.pushButton.show()
        else:
            self.animation1 = QPropertyAnimation(self.ui.wg_leftBar, b"maximumWidth")
            self.animation1.setDuration(250)
            self.animation1.setStartValue(150)
            self.animation1.setEndValue(44)
            self.animation1.setEasingCurve(QEasingCurve.Type.InOutSine)
            self.animation1.start()

            self.animation2 = QPropertyAnimation(self.ui.wg_leftBar, b"minimumWidth")
            self.animation2.setDuration(250)
            self.animation2.setStartValue(150)
            self.animation2.setEndValue(44)
            self.animation2.setEasingCurve(QEasingCurve.Type.InOutSine)
            self.animation2.start()
            self.ui.pushButton.hide()
    
    def testComboBoxColor(self):
        self.ui.cB_m_task.clear()
        self.ui.cB_m_task.addItem(create_colored_icon(QColor('blue')), "Học Toán")
        self.ui.cB_m_task.addItem(create_colored_icon(QColor('green')), "Học IELTS")
        self.ui.cB_m_task.addItem(create_colored_icon(QColor('red')), "Làm việc")