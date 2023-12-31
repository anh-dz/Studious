#!/usr/bin/env python3

import sys, os
from PyQt6.QtWidgets import QApplication
from view import *
from control.mainControl import *
os.environ["QT_FONT_DPI"] = "72" # DPI MACOS
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

def main():
    app = QApplication(sys.argv)
    main_window = ViewControl()
    model_obj = StudiousFunc(main_window.ui)
    main_window.show()
    app.exec()
    if model_obj.countdown.work_or_rest:
        model_obj.file.dataTimeJson[model_obj.file.ntime][main_window.ui.cB_m_task.currentText()] += round((model_obj.countdown.wtime-model_obj.countdown.time_left/60)/60, 1)
    model_obj.file.writeDataTime()

if __name__ == '__main__':
    main()