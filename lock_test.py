import sys
from PyQt6.QtCore import Qt, QTimer, QEasingCurve
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QGraphicsOpacityEffect

class RestUI(QMainWindow):
    def __init__(self, t):
        super().__init__()

        self.t = t * 1000

        self.setWindowState(Qt.WindowState.WindowFullScreen)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet("background: black;")

        self.current_opacity = 0.0
        self.setWindowOpacity(self.current_opacity)  # Set the window opacity (0.0 = fully transparent, 1.0 = fully opaque)

        # Create a central widget with a vertical layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a label widget for displaying text
        self.label = QLabel()
        self.label.setText("Làm việc vất vả rồi. Nghỉ ngơi chút nào!!!")
        self.label.setStyleSheet("font-size: 36px; color: white;")
        layout.addWidget(self.label)

        # Create a button widget
        self.button_layout = QHBoxLayout()

        self.close_button = QPushButton("ĐÓNG")
        self.close_button.setFixedSize(56, 30)
        self.close_button.setStyleSheet("QPushButton{background-color: #e74c3c; color: white; border-radius: 5px; font-size: 18px;}")
        self.close_button.clicked.connect(self.close)
        self.button_layout.addWidget(self.close_button)
        layout.addLayout(self.button_layout)

        central_widget.setLayout(layout)

        self.close_button.hide()

        # Create a timer for the fade-in animation
        self.fade_in_timer = QTimer(self)
        self.fade_in_timer.timeout.connect(self.fade_in)
        self.fade_in_timer.start(5)  # Increase the timer interval for a slower fade-in

        # Create a timer to hide and show the button
        self.button_timer = QTimer(self)
        self.button_timer.timeout.connect(lambda: self.close_button.show())
        self.button_timer.start(self.t)  # Hide the button for 10 seconds

    def fade_in(self):
        if self.current_opacity < 1.0:
            self.current_opacity += 0.04
            self.setWindowOpacity(self.current_opacity)
        else:
            self.fade_in_timer.stop()

def main():
    app = QApplication(sys.argv)
    window = RestUI(10)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
