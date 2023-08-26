from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy, QPushButton
from PyQt6.QtCore import Qt, QRect
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

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.load_image(self.image_paths[self.current_image_index])

    def previous_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
        self.load_image(self.image_paths[self.current_image_index])