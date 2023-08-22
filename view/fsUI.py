from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from . colorFunc import create_colored_icon

class StudiousFS(QWidget):
    def __init__(self):
        super().__init__()
        self.x = QApplication.primaryScreen().size().width()
        self.y = QApplication.primaryScreen().size().height()

        self.setWindowTitle("Studious Full Screen")
        # self.setGeometry(0, 0, self.x, self.y)
        self.setStyleSheet("QToolButton{border: 0px}")

        background_image = QPixmap("assert/background.jpg")
        background_label = QLabel(self)
        background_label.setPixmap(background_image.scaled(self.size(), Qt.AspectRatioMode.IgnoreAspectRatio))
        background_label.setGeometry(0, 0, self.x, self.y)

        self.cB_task = QComboBox(self)
        self.cB_task.setGeometry(QRect(300, 150, 221, 31))
        self.cB_task.setStyleSheet("QComboBox{\n"
"    background-color: rgba(52, 22, 85, 50%);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    color: rgb(249, 245, 246);\n"
"    font: 18pt \"Arial\";\n"
"}\n"
"QComboBox:hover{\n"
"\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(assert/drop-down-24);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(255, 121, 198);    \n"
"    background-color: rgb(33, 37, 43);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.cB_task.setObjectName("self.cB_task")

        self.lb_time = QLabel(self)
        self.lb_time.setStyleSheet("font: 128pt \"Arial\";\n"
"color: rgb(249, 245, 246);\n"
"border: 0px;\n"
"qproperty-alignment: \'AlignCenter\';\n"
"qproperty-margin: auto;")
        
        self.btn_startstop = QToolButton(self)
        self.btn_startstop.setMaximumSize(QSize(75, 75))
        icon11 = QIcon()
        icon11.addPixmap(QPixmap("assert/start.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_startstop.setIcon(icon11)
        self.btn_startstop.setIconSize(QSize(72, 72))

        self.btn_next = QToolButton(self)
        self.btn_next.setMaximumSize(QSize(75, 75))
        icon11 = QIcon()
        icon11.addPixmap(QPixmap("assert/next.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_next.setIcon(icon11)
        self.btn_next.setIconSize(QSize(72, 72))

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.btn_startstop)
        buttons_layout.addWidget(self.btn_next)
        buttons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a QVBoxLayout to center the label
        layout = QVBoxLayout()
        layout.addWidget(self.cB_task)
        layout.addWidget(self.lb_time)
        layout.addLayout(buttons_layout)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set the layout for the main widget
        self.setLayout(layout)

        self.bottomQuote = QLabel("bottomQuote", self)
        self.bottomQuote.setStyleSheet("font: 26pt \"Arial\";\n"
"color: rgb(249, 245, 246);\n"
"border: 0px;\n"
"qproperty-alignment: \'AlignCenter\';\n"
"qproperty-margin: auto;")
        self.bottomQuote.setWordWrap(True)

        self.bottomQuote.setGeometry(QRect(10, self.y-200, self.x-20, 180))

        self.btn_exit = QToolButton(self)
        self.btn_exit.setGeometry(self.x - 80, self.y-80, 75, 75)
        fsExit = QIcon()
        fsExit.addPixmap(QPixmap("assert/exit-full-screen.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_exit.setIcon(fsExit)
        self.btn_exit.setIconSize(QSize(72, 72))

        self.btn_audio = QToolButton(self)
        self.btn_audio.setGeometry(self.x - 80, 5, 75, 75)
        audioIcon = QIcon()
        audioIcon.addPixmap(QPixmap("assert/audio-on.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_audio.setIcon(audioIcon)
        self.btn_audio.setIconSize(QSize(72, 72))

        self.cB_task.addItem(create_colored_icon(QColor('blue')), "Học Toán")
        self.cB_task.addItem(create_colored_icon(QColor('green')), "Học IELTS")
        self.cB_task.addItem(create_colored_icon(QColor('red')), "Làm việc")

        self.showFullScreen()