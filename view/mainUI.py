# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Studious(object):
    def setupUi(self, Studious):
        Studious.setObjectName("Studious")
        Studious.resize(810, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Studious.sizePolicy().hasHeightForWidth())
        Studious.setSizePolicy(sizePolicy)
        Studious.setMinimumSize(QtCore.QSize(810, 560))
        Studious.setMaximumSize(QtCore.QSize(810, 560))
        self.centralwidget = QtWidgets.QWidget(parent=Studious)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(810, 560))
        self.centralwidget.setMaximumSize(QtCore.QSize(810, 560))
        self.centralwidget.setObjectName("centralwidget")
        self.wg_leftBar = QtWidgets.QWidget(parent=self.centralwidget)
        self.wg_leftBar.setGeometry(QtCore.QRect(0, 0, 150, 561))
        self.wg_leftBar.setMinimumSize(QtCore.QSize(0, 0))
        self.wg_leftBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.wg_leftBar.setStyleSheet("* {\n"
"    background-color: rgba(52, 22, 85, 70%);\n"
"    color: rgb(249, 245, 246);\n"
"}\n"
"QPushButton{\n"
"    background-color: transparent;\n"
"    background: none;\n"
"    font: 18pt \"Arial\";\n"
"    border: 0px;\n"
"    text-align: left;\n"
"    padding: 2px 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(52, 22, 85, 100%);\n"
"}")
        self.wg_leftBar.setObjectName("wg_leftBar")
        self.btn_lB_menu = QtWidgets.QPushButton(parent=self.wg_leftBar)
        self.btn_lB_menu.setGeometry(QtCore.QRect(0, 30, 161, 40))
        self.btn_lB_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_lB_menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_lB_menu.setFont(font)
        self.btn_lB_menu.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assert/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_menu.setIcon(icon)
        self.btn_lB_menu.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_menu.setCheckable(False)
        self.btn_lB_menu.setObjectName("btn_lB_menu")
        self.layoutWidget = QtWidgets.QWidget(parent=self.wg_leftBar)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 85, 151, 366))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layout_leftBar = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layout_leftBar.setContentsMargins(0, 0, 0, 0)
        self.layout_leftBar.setObjectName("layout_leftBar")
        self.btn_lB_pom = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_pom.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_pom.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assert/pomodoro.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_pom.setIcon(icon1)
        self.btn_lB_pom.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_pom.setObjectName("btn_lB_pom")
        self.layout_leftBar.addWidget(self.btn_lB_pom)
        self.btn_lB_chart = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_chart.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_chart.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assert/chart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_chart.setIcon(icon2)
        self.btn_lB_chart.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_chart.setObjectName("btn_lB_chart")
        self.layout_leftBar.addWidget(self.btn_lB_chart)
        self.btn_lB_habit = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_habit.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_habit.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assert/habit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_habit.setIcon(icon3)
        self.btn_lB_habit.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_habit.setObjectName("btn_lB_habit")
        self.layout_leftBar.addWidget(self.btn_lB_habit)
        self.btn_lB_botChat = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_botChat.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_botChat.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assert/botchat.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_botChat.setIcon(icon4)
        self.btn_lB_botChat.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_botChat.setObjectName("btn_lB_botChat")
        self.layout_leftBar.addWidget(self.btn_lB_botChat)
        self.btn_lB_flashCard = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_flashCard.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_flashCard.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assert/card.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_flashCard.setIcon(icon5)
        self.btn_lB_flashCard.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_flashCard.setObjectName("btn_lB_flashCard")
        self.layout_leftBar.addWidget(self.btn_lB_flashCard)
        self.btn_lB_setting = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_setting.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_setting.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_lB_setting.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assert/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_setting.setIcon(icon6)
        self.btn_lB_setting.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_setting.setObjectName("btn_lB_setting")
        self.layout_leftBar.addWidget(self.btn_lB_setting)
        self.btn_lB_about = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_about.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_about.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("assert/about.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_about.setIcon(icon7)
        self.btn_lB_about.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_about.setObjectName("btn_lB_about")
        self.layout_leftBar.addWidget(self.btn_lB_about)
        self.sW_main = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.sW_main.setGeometry(QtCore.QRect(40, 0, 771, 561))
        self.sW_main.setStyleSheet("*{\n"
"    background-color: transparent;\n"
"    background: none;\n"
"}\n"
"QToolButton{\n"
"    border: 0px;\n"
"}")
        self.sW_main.setObjectName("sW_main")
        self.page_m_pom = QtWidgets.QWidget()
        self.page_m_pom.setObjectName("page_m_pom")
        self.lb_m_time = QtWidgets.QLabel(parent=self.page_m_pom)
        self.lb_m_time.setGeometry(QtCore.QRect(280, 200, 211, 111))
        self.lb_m_time.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.lb_m_time.setStyleSheet("font: 50pt \"Arial\";\n"
"color: rgb(249, 245, 246);\n"
"border: 0px;\n"
"qproperty-alignment: \'AlignCenter\';\n"
"qproperty-margin: auto;")
        self.lb_m_time.setObjectName("lb_m_time")
        self.btn_m_audio = QtWidgets.QToolButton(parent=self.page_m_pom)
        self.btn_m_audio.setGeometry(QtCore.QRect(690, 40, 51, 51))
        self.btn_m_audio.setStyleSheet("")
        self.btn_m_audio.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("assert/audio-on.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_m_audio.setIcon(icon8)
        self.btn_m_audio.setIconSize(QtCore.QSize(50, 50))
        self.btn_m_audio.setObjectName("btn_m_audio")
        self.lb_m_quote = QtWidgets.QLabel(parent=self.page_m_pom)
        self.lb_m_quote.setGeometry(QtCore.QRect(40, 450, 661, 91))
        self.lb_m_quote.setStyleSheet("font: 18pt \"Arial\";\n"
"color: rgb(249, 245, 246);\n"
"padding: 2px 7px;")
        self.lb_m_quote.setWordWrap(True)
        self.lb_m_quote.setObjectName("lb_m_quote")
        self.btn_m_pin = QtWidgets.QToolButton(parent=self.page_m_pom)
        self.btn_m_pin.setGeometry(QtCore.QRect(630, 40, 51, 51))
        self.btn_m_pin.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("assert/pin.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_m_pin.setIcon(icon9)
        self.btn_m_pin.setIconSize(QtCore.QSize(50, 50))
        self.btn_m_pin.setObjectName("btn_m_pin")
        self.btn_m_fs = QtWidgets.QToolButton(parent=self.page_m_pom)
        self.btn_m_fs.setGeometry(QtCore.QRect(700, 490, 51, 51))
        self.btn_m_fs.setStyleSheet("")
        self.btn_m_fs.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("assert/fs.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_m_fs.setIcon(icon10)
        self.btn_m_fs.setIconSize(QtCore.QSize(50, 50))
        self.btn_m_fs.setObjectName("btn_m_fs")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.page_m_pom)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(310, 320, 160, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_m_startstop = QtWidgets.QToolButton(parent=self.horizontalLayoutWidget)
        self.btn_m_startstop.setMaximumSize(QtCore.QSize(51, 51))
        self.btn_m_startstop.setStyleSheet("")
        self.btn_m_startstop.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("assert/start.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_m_startstop.setIcon(icon11)
        self.btn_m_startstop.setIconSize(QtCore.QSize(50, 50))
        self.btn_m_startstop.setObjectName("btn_m_startstop")
        self.horizontalLayout.addWidget(self.btn_m_startstop)
        self.btn_m_next = QtWidgets.QToolButton(parent=self.horizontalLayoutWidget)
        self.btn_m_next.setMaximumSize(QtCore.QSize(51, 51))
        self.btn_m_next.setStyleSheet("")
        self.btn_m_next.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("assert/next.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_m_next.setIcon(icon12)
        self.btn_m_next.setIconSize(QtCore.QSize(50, 50))
        self.btn_m_next.setObjectName("btn_m_next")
        self.horizontalLayout.addWidget(self.btn_m_next)
        self.cB_m_task = QtWidgets.QComboBox(parent=self.page_m_pom)
        self.cB_m_task.setGeometry(QtCore.QRect(270, 150, 251, 31))
        self.cB_m_task.setStyleSheet("QComboBox{\n"
"    background-color: rgba(52, 22, 85, 50%);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    color: rgb(249, 245, 246);\n"
"    font: 14pt \"Arial\";\n"
"}\n"
"QComboBox:hover{\n"
"\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-style: solid;\n"
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
        self.cB_m_task.setObjectName("cB_m_task")
        self.cB_m_task.addItem("")
        self.cB_m_task.addItem("")
        self.sW_main.addWidget(self.page_m_pom)
        self.page_m_task = QtWidgets.QWidget()
        self.page_m_task.setObjectName("page_m_task")
        self.sW_main.addWidget(self.page_m_task)
        self.Background = QtWidgets.QLabel(parent=self.centralwidget)
        self.Background.setEnabled(True)
        self.Background.setGeometry(QtCore.QRect(0, 0, 810, 560))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Background.sizePolicy().hasHeightForWidth())
        self.Background.setSizePolicy(sizePolicy)
        self.Background.setMinimumSize(QtCore.QSize(810, 560))
        self.Background.setMaximumSize(QtCore.QSize(810, 560))
        self.Background.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Background.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.Background.setAutoFillBackground(False)
        self.Background.setStyleSheet("border-image: url(assert/background.jpg);")
        self.Background.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Background.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.Background.setLineWidth(0)
        self.Background.setText("")
        self.Background.setScaledContents(True)
        self.Background.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Background.setObjectName("Background")
        self.Background.raise_()
        self.wg_leftBar.raise_()
        self.sW_main.raise_()
        Studious.setCentralWidget(self.centralwidget)

        self.retranslateUi(Studious)
        QtCore.QMetaObject.connectSlotsByName(Studious)

    def retranslateUi(self, Studious):
        _translate = QtCore.QCoreApplication.translate
        Studious.setWindowTitle(_translate("Studious", "Studious"))
        self.btn_lB_menu.setText(_translate("Studious", "  MENU"))
        self.btn_lB_pom.setText(_translate("Studious", "  Pomodoro"))
        self.btn_lB_chart.setText(_translate("Studious", "  Thống kê"))
        self.btn_lB_habit.setText(_translate("Studious", "  Thói Quen"))
        self.btn_lB_botChat.setText(_translate("Studious", "  BotChat"))
        self.btn_lB_flashCard.setText(_translate("Studious", "  FlashCard"))
        self.btn_lB_setting.setText(_translate("Studious", "  Cài Đặt"))
        self.btn_lB_about.setText(_translate("Studious", "  Giới Thiệu"))
        self.lb_m_time.setText(_translate("Studious", "25:00"))
        self.lb_m_quote.setText(_translate("Studious", "CUỘC ĐỜI THẬT ĐẸP TUYỆT VỜI"))
        self.cB_m_task.setItemText(0, _translate("Studious", "Học"))
        self.cB_m_task.setItemText(1, _translate("Studious", "Làm việc"))
