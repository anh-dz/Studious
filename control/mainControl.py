from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from main import *

class StudiousFunc:
    def __init__(self, widgets):
        super().__init__()
        global wgs
        wgs = widgets
        wgs.btn_lB_pom.clicked.connect(self.testBackend)
    
    def testBackend(self):
        print("Hello World")
