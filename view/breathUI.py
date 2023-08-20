import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class BreathingCircleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Breathing Circle")
        self.setWindowState(Qt.WindowState.WindowFullScreen)  # Set full-screen mode
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Hide window frame

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.view)

        self.circle = QGraphicsEllipseItem(-60, -60, 120, 120)
        # self.circle.setPen(Qt.NoPen)
        self.circle.setBrush(QColor('blue'))
        self.scene.addItem(self.circle)

        self.inhale = True
        self.radius = 60
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(20)  # Adjust the interval for a smoother or faster animation

    def animate(self):
        if self.inhale:
            self.radius += 0.2
        else:
            self.radius -= 0.2

        if self.radius >= 120:
            self.inhale = False
        elif self.radius <= 50:
            self.inhale = True

        self.circle.setRect(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BreathingCircleApp()
    window.show()
    sys.exit(app.exec())
