from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from .mainUI import Ui_Studious
from .colorFunc import *
from .chatmessage import *

class ViewControl(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Studious()
        self.ui.setupUi(self)

        self.ui.pushButton.hide()
        self.ui.pushButton.clicked.connect(self.toggleSideMenu)
        self.ui.wg_leftBar.setGeometry(QRect(0, 0, 44, 561))

        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(0)
        self.ui.Background.setGraphicsEffect(self.blur_effect)

        self.ui.btn_lB_1.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(0) or self.blur_effect.setBlurRadius(0))
        self.ui.btn_lB_2.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(1) or self.blur_effect.setBlurRadius(12))
        self.ui.btn_lB_3.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(2) or self.blur_effect.setBlurRadius(12))
        self.ui.btn_lB_4.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(3) or self.blur_effect.setBlurRadius(12))
        self.ui.btn_lB_5.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(4) or self.blur_effect.setBlurRadius(12))
        self.ui.btn_lB_6.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(5) or self.blur_effect.setBlurRadius(12))
        self.ui.btn_lB_7.clicked.connect(lambda: self.ui.sW_main.setCurrentIndex(6) or self.blur_effect.setBlurRadius(12))

        self.ui.btn_6_nextPage.clicked.connect(self.nextPage)
        self.pageInt = 0

        self.ui.btn_lB_menu.clicked.connect(self.toggleSideMenu)

        self.setupHTMLText()

        self.testComboBoxColor()
    
    def nextPage(self):
        if self.pageInt:
            self.ui.btn_6_nextPage.setText("👉")
            self.ui.sW_setting.setCurrentIndex(0)
            self.pageInt = 0
        else:
            self.ui.btn_6_nextPage.setText("👈")
            self.ui.sW_setting.setCurrentIndex(1)
            self.pageInt = 1

    def toggleSideMenu(self):
        target_width = 150 if self.ui.wg_leftBar.width() <= 70 else 44

        self.animation1 = QPropertyAnimation(self.ui.wg_leftBar, b"maximumWidth")
        self.animation1.setDuration(250)
        self.animation1.setStartValue(self.ui.wg_leftBar.width())
        self.animation1.setEndValue(target_width)
        self.animation1.setEasingCurve(QEasingCurve.Type.InOutSine)
        self.animation1.start()

        self.animation2 = QPropertyAnimation(self.ui.wg_leftBar, b"minimumWidth")
        self.animation2.setDuration(250)
        self.animation2.setStartValue(self.ui.wg_leftBar.width())
        self.animation2.setEndValue(target_width)
        self.animation2.setEasingCurve(QEasingCurve.Type.InOutSine)
        self.animation2.start()

        self.ui.pushButton.setVisible(target_width > 44)
    
    def testComboBoxColor(self):
        self.ui.cB_m_task.clear()
        self.ui.cB_m_task.addItem(create_colored_icon(QColor('blue')), "Học Toán")
        self.ui.cB_m_task.addItem(create_colored_icon(QColor('green')), "Học IELTS")
        self.ui.cB_m_task.addItem(create_colored_icon(QColor('red')), "Làm việc")       
    
    def setupHTMLText(self):
        with open("data/breath.html", "r", encoding="utf-8") as f:
            breathHTML = f.read()
            self.ui.tB_5_breath.setHtml(breathHTML)
