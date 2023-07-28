from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys

class StudiousFS(QWidget):
    def __init__(self):
        super().__init__()
        self.x = QApplication.primaryScreen().size().width()
        self.y = QApplication.primaryScreen().size().height()

        self.setWindowTitle("Studious Full Screen")
        self.setGeometry(0, 0, self.x, self.y)

        background_image = QPixmap("assert/background.jpg")
        background_label = QLabel(self)
        background_label.setPixmap(background_image.scaled(self.size(), Qt.AspectRatioMode.IgnoreAspectRatio))
        background_label.setGeometry(0, 0, self.x, self.y)

        # Create a QLabel widget to display the text
        lb_task = QLabel("TASK", self)
        lb_task.setStyleSheet("font: 50pt \"Arial\";\n"
"color: rgb(249, 245, 246);\n"
"border: 0px;\n"
"qproperty-alignment: \'AlignCenter\';\n"
"qproperty-margin: auto;")
        lb_time = QLabel("25:00", self)
        lb_time.setStyleSheet("font: 50pt \"Arial\";\n"
"color: rgb(249, 245, 246);\n"
"border: 0px;\n"
"qproperty-alignment: \'AlignCenter\';\n"
"qproperty-margin: auto;")

        # Create a QVBoxLayout to center the label
        layout = QVBoxLayout()
        layout.addWidget(lb_task)
        layout.addWidget(lb_time)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set the layout for the main widget
        self.setLayout(layout)

        self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StudiousFS()
    sys.exit(app.exec()) 
