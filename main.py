import sys
from PyQt6.QtWidgets import QApplication
from view import *
from control import *

class MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        main_window = ViewControl()
        model_obj = StudiousFunc(main_window.ui)
        main_window.show()
        sys.exit(self.exec())

if __name__ == '__main__':
    app = MainApp(sys.argv)
