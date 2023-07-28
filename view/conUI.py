from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from . mainUI import Ui_Studious

def create_colored_icon(color):
    '''
        Example: create_colored_icon(QColor('white')
    '''
    pixmap = QPixmap(16, 16)
    pixmap.fill(color)
    return QIcon(pixmap)

class ViewControl(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Studious()
        self.ui.setupUi(self)

        self.ui.btn_lB_menu.clicked.connect(self.Side_Menu_Def_0)
        self.Side_Menu_Def_0()
        self.testComboBoxColor()

    def Side_Menu_Def_0(self):
        if self.ui.wg_leftBar.width() <= 70:
            self.animation1 = QPropertyAnimation(self.ui.wg_leftBar, b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(44)
            self.animation1.setEndValue(150)
            self.animation1.setEasingCurve(QEasingCurve.Type.InOutSine)
            self.animation1.start()

            self.animation2 = QPropertyAnimation(self.ui.wg_leftBar, b"minimumWidth")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(44)
            self.animation2.setEndValue(150)
            self.animation2.setEasingCurve(QEasingCurve.Type.InOutSine)
            self.animation2.start()

        else:
            self.animation1 = QPropertyAnimation(self.ui.wg_leftBar, b"maximumWidth")
            self.animation1.setDuration(500)
            self.animation1.setStartValue(150)
            self.animation1.setEndValue(44)
            self.animation1.setEasingCurve(QEasingCurve.Type.InOutSine)
            self.animation1.start()

            self.animation2 = QPropertyAnimation(self.ui.wg_leftBar, b"minimumWidth")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(150)
            self.animation2.setEndValue(44)
            self.animation2.setEasingCurve(QEasingCurve.Type.InOutSine)
            self.animation2.start()
    
    def testComboBoxColor(self):
        self.ui.cB_m_task.clear()
        self.ui.cB_m_task.addItem(create_colored_icon(QColor('blue')), "Học")
        self.ui.cB_m_task.addItem(create_colored_icon(QColor('red')), "Làm việc")