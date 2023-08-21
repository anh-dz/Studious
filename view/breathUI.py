import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class BreathingCircleAnimation(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Breathing Circle")
        self.setWindowState(Qt.WindowState.WindowFullScreen)  # Set full-screen mode
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Hide window frame

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.view)

        self.circle = QGraphicsEllipseItem(-100, -100, 200, 200)
        self.circle.setBrush(QColor(51, 124, 207))  # RGB(51, 124, 207)
        self.scene.addItem(self.circle)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.script_label = QLabel("Close your eyes and take a deep breath in through your nose. Feel the air filling your lungs.")
        self.script_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.script_label.setWordWrap(True)
        layout.addWidget(self.script_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(False)
        layout.addWidget(self.progress_bar)

        self.count_label = QLabel("Breaths: 0")
        self.count_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.count_label)

        self.button_layout = QHBoxLayout()

        self.close_button = QPushButton("X")
        self.close_button.setFixedSize(30, 30)
        self.close_button.setStyleSheet("QPushButton { background-color: #e74c3c; color: white; border-radius: 15px; font-size: 18px; }")
        self.close_button.clicked.connect(self.close)
        self.button_layout.addWidget(self.close_button)

        layout.addLayout(self.button_layout)

        self.setLayout(layout)

        self.inhale = True
        self.radius = 100
        self.breath_duration = 4000  # Time in milliseconds for inhale/exhale
        self.elapsed_time = 0
        self.breath_count = 0  # Initialize breath count
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(20)  # Adjust the interval for a smoother or faster animation

        self.script_index = 0
        self.scripts = [
            "Nhìn vào hơi thở của bạn và cảm nhận",
            "Thở ra một hơi thật dài và sẵn sàng",
            "Từ từ nhắm mắt lại và hít thở thật sâu. Cảm nhận không khí lấp đầy phổi của bạn",
            "Giữ hơi thở một lúc, sau đó chậm rãi thở ra bằng miệng. Hãy để những căng thẳng trôi ra cùng hơi thở bạn",
            "Chậm rãi hít thở thật sâu lần nữa, bạn sẽ cảm thấy như được lên thiên đàng",
            "Khi bạn thở ra, bạn sẽ cảm thấy thật sung sướng và sảng khoái",
            "Tiếp tục hít vào năng lượng tích cực và thở ra căng thẳng. Bạn sẽ cảm thấy bản thân trở nên thư thái hơn với từng hơi thở",
            "Bạn đang có cảm nhận gì rồi?",
        ]

        self.script_label.setText(self.scripts[self.script_index])

    def animate(self):
        if self.inhale:
            self.elapsed_time += 20
            self.radius += 0.2
            self.label.setText("Chậm rãi hít vào...")
        else:
            self.elapsed_time += 20
            self.radius -= 0.2
            self.label.setText("Chậm rãi thở ra...")

        if self.elapsed_time >= self.breath_duration:
            self.inhale = not self.inhale
            self.elapsed_time = 0
            self.progress_bar.setValue(0)
            if not self.inhale:
                self.breath_count += 1
                self.count_label.setText(f"Breaths: {self.breath_count}")

                # Switch to the next guided meditation script
                self.script_index = (self.script_index + 1) % len(self.scripts)
                self.script_label.setText(self.scripts[self.script_index])

        if self.radius >= 140:
            self.inhale = False
        elif self.radius <= 100:
            self.inhale = True

        self.circle.setRect(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = BreathingCircleAnimation()
#     window.show()
#     sys.exit(app.exec())
