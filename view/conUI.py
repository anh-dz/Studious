from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from .mainUI import Ui_Studious
from .colorFunc import *
from .chatmessage import *
from .hdsd import *

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

        self.ui.btn_7_community.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://www.facebook.com/groups/803129063825326")))

        self.ui.btn_6_nextPage.clicked.connect(self.nextPage)
        self.pageInt = 0

        self.ui.btn_lB_menu.clicked.connect(self.toggleSideMenu)

        self.ui.btn_lB_1.setStyleSheet("background-color: rgb(60, 30, 100);")

        self.setupHTMLText()
    
        self.buttons = [
            self.ui.btn_lB_1,
            self.ui.btn_lB_2,
            self.ui.btn_lB_3,
            self.ui.btn_lB_4,
            self.ui.btn_lB_5,
            self.ui.btn_lB_6,
            self.ui.btn_lB_7
        ]
        
        self.colorTask = getColorTask()

        for row in range(7):
            self.setColorRowTable(self.ui.tW_6, row, self.colorTask[row])

        # Connect each button's clicked signal to the slot function
        for button in self.buttons:
            button.clicked.connect(self.buttonClicked)
        
        self.ui.btn_lB_ques.clicked.connect(self.checkQues)

        self.testComboBoxColor()

    def buttonClicked(self):
        # Get the sender of the clicked signal (the button that was clicked)
        clicked_button = self.sender()

        if clicked_button == self.ui.btn_lB_1:
            self.blur_effect.setBlurRadius(0)
        else:
            self.blur_effect.setBlurRadius(12)

        # Change the background color of the clicked button
        clicked_button.setStyleSheet("background-color: rgb(60, 30, 100);")

        # Change the background color of other buttons back to the original color
        for button in self.buttons:
            if button != clicked_button:
                button.setStyleSheet("")

        if clicked_button == self.ui.btn_lB_1:
            self.ui.sW_main.setCurrentIndex(0)
        elif clicked_button == self.ui.btn_lB_2:
            self.ui.sW_main.setCurrentIndex(1)
        elif clicked_button == self.ui.btn_lB_3:
            self.ui.sW_main.setCurrentIndex(2)
        elif clicked_button == self.ui.btn_lB_4:
            self.ui.sW_main.setCurrentIndex(3)
        elif clicked_button == self.ui.btn_lB_5:
            self.ui.sW_main.setCurrentIndex(4)
        elif clicked_button == self.ui.btn_lB_6:
            self.ui.sW_main.setCurrentIndex(5)
        elif clicked_button == self.ui.btn_lB_7:
            self.ui.sW_main.setCurrentIndex(6)
    
    def checkQues(self):
        w = self.ui.sW_main.currentIndex()
        self.image_app = ImageDisplayApp()
        self.image_app.load_image(f"assert/hdsd/{w}.png")
        self.image_app.show()
    
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
        # self.ui.tW_6.setItem(0, 0, QTableWidgetItem(create_colored_icon(QColor("blue")), "Hello World"))
    
    def setColorRowTable(self, table, row, color):
        for j in range(3): #table.columnCount()
            table.item(row, j).setBackground(QColor(color))

    
    def setupHTMLText(self):
        with open("data/breath.html", "r", encoding="utf-8") as f:
            breathHTML = f.read()
            self.ui.tB_5_breath.setHtml(breathHTML)
        with open("data/about.html", "r", encoding="utf-8") as f:
            about = f.read()
            self.ui.tB_7_about.setHtml(about)
