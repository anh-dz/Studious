from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from main import *
import time

class StudiousFunc:
    def __init__(self, widgets: ViewControl):
        global wgs
        wgs = widgets
        self.countdown = countdown()
        self.countdown.start_timer()
    
    def testBackend(self):
        self.countdown = countdown()
        print("Hello World")

class countdown:
    def __init__(self):
        self.mtime = 1
        self.start_time = self.mtime*60
        self.time_left = self.start_time
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_countdown)

    def start_timer(self):
        self.timer.start(1000)  # Update every second

    def update_countdown(self):
        self.time_left -= 1

        if self.time_left >= 0:
            # Format the remaining time as MM:SS
            minutes, seconds = divmod(self.time_left, 60)
            wgs.label.setText(f"{minutes:02}:{seconds:02}")
        else:
            self.timer.stop()
            wgs.label.setText("Time's up!")
