# STUDIOUS
# OS: WINDOWS 11
#
# DEVELOPER: THE DREAM TEAM
# FRONTEND: NGUYEN MAI NHAT ANH
# BACKEND: NGUYEN NHAT HUY
# UX DESIGNER: NGUYEN YEN LY
#
# COPYRIGHT 2023 STUDIOUS
# Do not modify this file unless you know what you are doing.

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from view import *
from control import *
import sys

class ViewControl(Ui_MainWindow):
    def __init__(self):
        super().__init__()

class MainApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

app = QApplication(sys.argv)
mainwindows = MainApp()

def main():
    widgets = ViewControl()
    widgets.setupUi(mainwindows)
    

    model_obj = StudiousFunc(widgets)
    mainwindows.show()
    app.exec()

if __name__ == '__main__':
    main()