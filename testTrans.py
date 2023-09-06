import sys
from PyQt6.QtCore import Qt, QTimer, QEasingCurve
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QGraphicsOpacityEffect

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Transparent Window")
        self.setGeometry(100, 100, 800, 600)  # Set the window size and position
        self.setStyleSheet("background: black;")
        self.current_opacity = 0.0
        self.setWindowOpacity(self.current_opacity)  # Set the window opacity (0.0 = fully transparent, 1.0 = fully opaque)

        # Create a central widget with a vertical layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Create a label widget for displaying text
        self.label = QLabel()
        self.label.setText("Transparent Window Content")
        self.label.setStyleSheet("font-size: 24px; color: white;")
        layout.addWidget(self.label)

        central_widget.setLayout(layout)
        
        # Create a timer for the fade-in animation
        self.fade_in_timer = QTimer(self)
        self.fade_in_timer.timeout.connect(self.fade_in)
        self.fade_in_timer.start(5)  # Increase the timer interval for a slower fade-in

    def fade_in(self):
        if self.current_opacity < 1.0:
            # Increase opacity gradually using a linear easing curve
            self.current_opacity += 0.02
            self.setWindowOpacity(self.current_opacity)
        else:
            # Stop the timer when opacity reaches 1 (fully visible)
            self.fade_in_timer.stop()

def main():
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
