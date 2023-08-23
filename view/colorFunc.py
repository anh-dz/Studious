from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

def getColorTask(): # return 7 color of Task sort by priority
    return ['#C51605', '#F94C10', '#F94C10', '#1A5D1A', '#0C356A', '#35155D', '#352F44']

def create_colored_icon(color, radius=8):
    pixmap = QPixmap(16, 16)
    pixmap.fill(QColor(0, 0, 0, 0))
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    rounded_rect = pixmap.rect().adjusted(1, 1, -1, -1)
    painter.setBrush(color)
    painter.setPen(Qt.PenStyle.NoPen)
    painter.drawRoundedRect(rounded_rect, radius, radius)
    painter.end()

    return QIcon(pixmap)

class comboCompanies(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("font: 18pt;")
        self.addItems(['Chưa hoàn thành', 'Đang làm', 'Đã hoàn thành'])
        self.currentIndexChanged.connect(self.getComboValue)

    def getComboValue(self):
        print(self.currentText())