import sys, os
from PyQt6.QtWidgets import QApplication
from view import *
from control import *
import os

os.environ["QT_FONT_DPI"] = "72" # FIX Problem for High DPI and Scale above 100%
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

os.environ["QT_FONT_DPI"] = "72" # MACOS DPI
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

class MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        main_window = ViewControl()
        model_obj = StudiousFunc(main_window.ui)
        main_window.show()
        sys.exit(self.exec())

if __name__ == '__main__':
    app = MainApp(sys.argv)
