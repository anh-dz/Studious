from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from main import *

class StudiousFunc:
    def __init__(self, widgets: ViewControl):
        global wgs
        wgs = widgets
        self.testBackend()
    
    def testBackend(self):
        wgs.label.setText("UR GAY")
        print("Hello World")
