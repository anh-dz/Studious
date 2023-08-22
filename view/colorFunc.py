from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

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