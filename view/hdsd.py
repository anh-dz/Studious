import sys
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QWidget, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class ImageDisplayApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("How to use Studious")

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.image_label = QLabel(self)
        self.image_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.image_label)

    def load_image(self, image_path):
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(750, 470, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)  # Scale the pixmap
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)  # Resize image to fit label
