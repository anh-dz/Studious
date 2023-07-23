# DEVELOPER: The Dream Team
# Do not modify this file unless you know what you are doing.

import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from view import *
from control import *

class ViewControl(Ui_MainWindow):
    def __init__(self):
        super().__init__()

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

def main():
    app = QApplication(sys.argv)
    main_window = MainApp()
    widgets = ViewControl()
    widgets.setupUi(main_window)

    model_obj = StudiousFunc(widgets)

    main_window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
