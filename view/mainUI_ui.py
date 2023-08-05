# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_Studious(object):
    def setupUi(self, Studious):
        if not Studious.objectName():
            Studious.setObjectName(u"Studious")
        Studious.resize(820, 560)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Studious.sizePolicy().hasHeightForWidth())
        Studious.setSizePolicy(sizePolicy)
        Studious.setMinimumSize(QSize(820, 560))
        Studious.setMaximumSize(QSize(820, 560))
        icon = QIcon()
        icon.addFile(u"assert/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Studious.setWindowIcon(icon)
        self.centralwidget = QWidget(Studious)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(820, 560))
        self.centralwidget.setMaximumSize(QSize(820, 560))
        self.wg_leftBar = QWidget(self.centralwidget)
        self.wg_leftBar.setObjectName(u"wg_leftBar")
        self.wg_leftBar.setGeometry(QRect(0, 0, 150, 561))
        self.wg_leftBar.setMinimumSize(QSize(0, 0))
        self.wg_leftBar.setMaximumSize(QSize(16777215, 16777215))
        self.wg_leftBar.setStyleSheet(u"* {\n"
"	background-color: rgba(52, 22, 85, 70%);\n"
"	color: rgb(249, 245, 246);\n"
"}\n"
"QPushButton{\n"
"	background-color: transparent;\n"
"	background: none;\n"
"	font: 18pt \"Arial\";\n"
"	border: 0px;\n"
"	text-align: left;\n"
"	padding: 2px 7px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(52, 22, 85, 100%);\n"
"}")
        self.btn_lB_menu = QPushButton(self.wg_leftBar)
        self.btn_lB_menu.setObjectName(u"btn_lB_menu")
        self.btn_lB_menu.setGeometry(QRect(0, 30, 161, 40))
        self.btn_lB_menu.setMinimumSize(QSize(0, 0))
        self.btn_lB_menu.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.btn_lB_menu.setFont(font)
        self.btn_lB_menu.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"assert/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lB_menu.setIcon(icon1)
        self.btn_lB_menu.setIconSize(QSize(32, 32))
        self.btn_lB_menu.setCheckable(False)
        self.layoutWidget = QWidget(self.wg_leftBar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 85, 151, 366))
        self.layout_leftBar = QVBoxLayout(self.layoutWidget)
        self.layout_leftBar.setObjectName(u"layout_leftBar")
        self.layout_leftBar.setContentsMargins(0, 0, 0, 0)
        self.btn_lB_1 = QPushButton(self.layoutWidget)
        self.btn_lB_1.setObjectName(u"btn_lB_1")
        self.btn_lB_1.setMinimumSize(QSize(0, 40))
        self.btn_lB_1.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"assert/pomodoro.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lB_1.setIcon(icon2)
        self.btn_lB_1.setIconSize(QSize(32, 32))

        self.layout_leftBar.addWidget(self.btn_lB_1)

        self.btn_lB_2 = QPushButton(self.layoutWidget)
        self.btn_lB_2.setObjectName(u"btn_lB_2")
        self.btn_lB_2.setMinimumSize(QSize(0, 40))
        self.btn_lB_2.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"assert/chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lB_2.setIcon(icon3)
        self.btn_lB_2.setIconSize(QSize(32, 32))

        self.layout_leftBar.addWidget(self.btn_lB_2)

        self.btn_lB_3 = QPushButton(self.layoutWidget)
        self.btn_lB_3.setObjectName(u"btn_lB_3")
        self.btn_lB_3.setMinimumSize(QSize(0, 40))
        self.btn_lB_3.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"assert/habit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lB_3.setIcon(icon4)
        self.btn_lB_3.setIconSize(QSize(32, 32))

        self.layout_leftBar.addWidget(self.btn_lB_3)

        self.btn_lB_4 = QPushButton(self.layoutWidget)
        self.btn_lB_4.setObjectName(u"btn_lB_4")
        self.btn_lB_4.setMinimumSize(QSize(0, 40))
        self.btn_lB_4.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"assert/botchat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lB_4.setIcon(icon5)
        self.btn_lB_4.setIconSize(QSize(32, 32))

        self.layout_leftBar.addWidget(self.btn_lB_4)

        self.btn_lB_5 = QPushButton(self.layoutWidget)
        self.btn_lB_5.setObjectName(u"btn_lB_5")
        self.btn_lB_5.setMinimumSize(QSize(0, 40))
        self.btn_lB_5.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"assert/card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lB_5.setIcon(icon6)
        self.btn_lB_5.setIconSize(QSize(32, 32))

        self.layout_leftBar.addWidget(self.btn_lB_5)

        self.btn_lB_6 = QPushButton(self.layoutWidget)
        self.btn_lB_6.setObjectName(u"btn_lB_6")
        self.btn_lB_6.setMinimumSize(QSize(0, 40))
        self.btn_lB_6.setMaximumSize(QSize(16777215, 16777215))
        self.btn_lB_6.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u"assert/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lB_6.setIcon(icon7)
        self.btn_lB_6.setIconSize(QSize(32, 32))

        self.layout_leftBar.addWidget(self.btn_lB_6)

        self.btn_lB_7 = QPushButton(self.layoutWidget)
        self.btn_lB_7.setObjectName(u"btn_lB_7")
        self.btn_lB_7.setMinimumSize(QSize(0, 40))
        self.btn_lB_7.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"assert/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lB_7.setIcon(icon8)
        self.btn_lB_7.setIconSize(QSize(32, 32))

        self.layout_leftBar.addWidget(self.btn_lB_7)

        self.sW_main = QStackedWidget(self.centralwidget)
        self.sW_main.setObjectName(u"sW_main")
        self.sW_main.setGeometry(QRect(40, 0, 781, 561))
        self.sW_main.setStyleSheet(u"* {\n"
"	background-color: transparent;\n"
"	color: rgb(249, 245, 246);\n"
"	font: 18pt \"Arial\";\n"
"}\n"
"QToolButton{\n"
"	border: 0px;\n"
"}\n"
"QComboBox{\n"
"	background-color: rgba(52, 22, 85, 50%);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	color: rgb(249, 245, 246);\n"
"	font: 14pt \"Arial\";\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(assert/drop-down-24);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.page_m_pom = QWidget()
        self.page_m_pom.setObjectName(u"page_m_pom")
        self.page_m_pom.setStyleSheet(u"QLabel{\n"
"	font: 72pt \"Arial\";\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	qproperty-margin: auto;\n"
"}")
        self.lb_m_time = QLabel(self.page_m_pom)
        self.lb_m_time.setObjectName(u"lb_m_time")
        self.lb_m_time.setGeometry(QRect(243, 180, 311, 141))
        self.lb_m_time.setLayoutDirection(Qt.LeftToRight)
        self.lb_m_time.setStyleSheet(u"color: rgb(249, 245, 246);")
        self.btn_m_audio = QToolButton(self.page_m_pom)
        self.btn_m_audio.setObjectName(u"btn_m_audio")
        self.btn_m_audio.setGeometry(QRect(710, 30, 51, 51))
        self.btn_m_audio.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"assert/audio-on.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_m_audio.setIcon(icon9)
        self.btn_m_audio.setIconSize(QSize(50, 50))
        self.lb_m_quote = QLabel(self.page_m_pom)
        self.lb_m_quote.setObjectName(u"lb_m_quote")
        self.lb_m_quote.setGeometry(QRect(40, 442, 662, 120))
        self.lb_m_quote.setStyleSheet(u"font: 16pt \"Arial\";\n"
"color: rgb(249, 245, 246);\n"
"padding: 2px 7px;")
        self.lb_m_quote.setWordWrap(True)
        self.btn_m_pin = QToolButton(self.page_m_pom)
        self.btn_m_pin.setObjectName(u"btn_m_pin")
        self.btn_m_pin.setGeometry(QRect(650, 30, 51, 51))
        icon10 = QIcon()
        icon10.addFile(u"assert/pin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_m_pin.setIcon(icon10)
        self.btn_m_pin.setIconSize(QSize(50, 50))
        self.btn_m_fs = QToolButton(self.page_m_pom)
        self.btn_m_fs.setObjectName(u"btn_m_fs")
        self.btn_m_fs.setGeometry(QRect(700, 490, 51, 51))
        self.btn_m_fs.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u"assert/fs.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_m_fs.setIcon(icon11)
        self.btn_m_fs.setIconSize(QSize(50, 50))
        self.horizontalLayoutWidget = QWidget(self.page_m_pom)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(320, 330, 160, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_m_startstop = QToolButton(self.horizontalLayoutWidget)
        self.btn_m_startstop.setObjectName(u"btn_m_startstop")
        self.btn_m_startstop.setMaximumSize(QSize(51, 51))
        self.btn_m_startstop.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u"assert/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_m_startstop.setIcon(icon12)
        self.btn_m_startstop.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_m_startstop)

        self.btn_m_next = QToolButton(self.horizontalLayoutWidget)
        self.btn_m_next.setObjectName(u"btn_m_next")
        self.btn_m_next.setMaximumSize(QSize(51, 51))
        self.btn_m_next.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u"assert/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_m_next.setIcon(icon13)
        self.btn_m_next.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.btn_m_next)

        self.cB_m_task = QComboBox(self.page_m_pom)
        self.cB_m_task.addItem("")
        self.cB_m_task.addItem("")
        self.cB_m_task.setObjectName(u"cB_m_task")
        self.cB_m_task.setGeometry(QRect(273, 130, 251, 31))
        self.cB_m_task.setStyleSheet(u"")
        self.sW_main.addWidget(self.page_m_pom)
        self.page_m_2 = QWidget()
        self.page_m_2.setObjectName(u"page_m_2")
        self.page_m_2.setStyleSheet(u"* {\n"
"	font: 18pt \"Arial\";\n"
"	border: 0px;\n"
"}\n"
"QPushButton{\n"
"    background-color: rgba(52, 22, 85, 70%);\n"
"    color: rgb(249, 245, 246);\n"
"    font: 14pt \"Arial\";\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"    padding: 2px 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(52, 22, 85, 100%);\n"
"}")
        self.columnChart = QWidget(self.page_m_2)
        self.columnChart.setObjectName(u"columnChart")
        self.columnChart.setGeometry(QRect(20, 90, 412, 392))
        self.columnChart.setMinimumSize(QSize(412, 392))
        self.verticalLayout_2 = QVBoxLayout(self.columnChart)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pieChart = QWidget(self.page_m_2)
        self.pieChart.setObjectName(u"pieChart")
        self.pieChart.setGeometry(QRect(439, 89, 331, 392))
        self.pieChart.setMinimumSize(QSize(331, 392))
        self.verticalLayout = QVBoxLayout(self.pieChart)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_m_delChart = QPushButton(self.page_m_2)
        self.btn_m_delChart.setObjectName(u"btn_m_delChart")
        self.btn_m_delChart.setGeometry(QRect(650, 29, 112, 32))
        self.btn_m_delChart.setMinimumSize(QSize(0, 32))
        self.btn_m_delChart.setStyleSheet(u"")
        icon14 = QIcon()
        icon14.addFile(u"assert/del.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_m_delChart.setIcon(icon14)
        self.btn_m_delChart.setIconSize(QSize(23, 23))
        self.label = QLabel(self.page_m_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 500, 461, 41))
        self.label.setStyleSheet(u"color: rgb(249, 245, 246);\n"
"font: 18pt \"Arial\";")
        self.cB_chooseDate = QComboBox(self.page_m_2)
        self.cB_chooseDate.addItem("")
        self.cB_chooseDate.addItem("")
        self.cB_chooseDate.addItem("")
        self.cB_chooseDate.addItem("")
        self.cB_chooseDate.addItem("")
        self.cB_chooseDate.setObjectName(u"cB_chooseDate")
        self.cB_chooseDate.setGeometry(QRect(160, 30, 171, 31))
        self.cB_chooseDate.setStyleSheet(u"")
        self.sW_main.addWidget(self.page_m_2)
        self.btn_m_delChart.raise_()
        self.label.raise_()
        self.cB_chooseDate.raise_()
        self.pieChart.raise_()
        self.columnChart.raise_()
        self.page_m_3 = QWidget()
        self.page_m_3.setObjectName(u"page_m_3")
        self.sW_main.addWidget(self.page_m_3)
        self.page_m_4 = QWidget()
        self.page_m_4.setObjectName(u"page_m_4")
        self.sW_main.addWidget(self.page_m_4)
        self.page_m_5 = QWidget()
        self.page_m_5.setObjectName(u"page_m_5")
        self.sW_main.addWidget(self.page_m_5)
        self.page_m_6 = QWidget()
        self.page_m_6.setObjectName(u"page_m_6")
        self.sW_main.addWidget(self.page_m_6)
        self.page_m_7 = QWidget()
        self.page_m_7.setObjectName(u"page_m_7")
        self.sW_main.addWidget(self.page_m_7)
        self.Background = QLabel(self.centralwidget)
        self.Background.setObjectName(u"Background")
        self.Background.setEnabled(True)
        self.Background.setGeometry(QRect(0, 0, 820, 560))
        sizePolicy.setHeightForWidth(self.Background.sizePolicy().hasHeightForWidth())
        self.Background.setSizePolicy(sizePolicy)
        self.Background.setMinimumSize(QSize(820, 560))
        self.Background.setMaximumSize(QSize(820, 560))
        self.Background.setFocusPolicy(Qt.NoFocus)
        self.Background.setContextMenuPolicy(Qt.NoContextMenu)
        self.Background.setAutoFillBackground(False)
        self.Background.setStyleSheet(u"border-image: url(assert/background.jpg);")
        self.Background.setFrameShape(QFrame.NoFrame)
        self.Background.setFrameShadow(QFrame.Plain)
        self.Background.setLineWidth(0)
        self.Background.setScaledContents(True)
        self.Background.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 820, 560))
        self.pushButton.setStyleSheet(u"background-color: rgb(70, 69, 140, 50%);\n"
"border: 0px;")
        Studious.setCentralWidget(self.centralwidget)
        self.Background.raise_()
        self.sW_main.raise_()
        self.pushButton.raise_()
        self.wg_leftBar.raise_()

        self.retranslateUi(Studious)

        self.sW_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Studious)
    # setupUi

    def retranslateUi(self, Studious):
        Studious.setWindowTitle(QCoreApplication.translate("Studious", u"Studious", None))
        self.btn_lB_menu.setText(QCoreApplication.translate("Studious", u"  MENU", None))
        self.btn_lB_1.setText(QCoreApplication.translate("Studious", u"  Pomodoro", None))
        self.btn_lB_2.setText(QCoreApplication.translate("Studious", u"  Th\u1ed1ng k\u00ea", None))
        self.btn_lB_3.setText(QCoreApplication.translate("Studious", u"  Th\u00f3i Quen", None))
        self.btn_lB_4.setText(QCoreApplication.translate("Studious", u"  BotChat", None))
        self.btn_lB_5.setText(QCoreApplication.translate("Studious", u"  FlashCard", None))
        self.btn_lB_6.setText(QCoreApplication.translate("Studious", u"  C\u00e0i \u0110\u1eb7t", None))
        self.btn_lB_7.setText(QCoreApplication.translate("Studious", u"  Gi\u1edbi Thi\u1ec7u", None))
        self.lb_m_time.setText(QCoreApplication.translate("Studious", u"25:00", None))
        self.btn_m_audio.setText("")
        self.lb_m_quote.setText(QCoreApplication.translate("Studious", u"CU\u1ed8C \u0110\u1edcI TH\u1eacT \u0110\u1eb8P TUY\u1ec6T V\u1edcI", None))
        self.btn_m_pin.setText("")
        self.btn_m_fs.setText("")
        self.btn_m_startstop.setText("")
        self.btn_m_next.setText("")
        self.cB_m_task.setItemText(0, QCoreApplication.translate("Studious", u"H\u1ecdc", None))
        self.cB_m_task.setItemText(1, QCoreApplication.translate("Studious", u"L\u00e0m vi\u1ec7c", None))

        self.btn_m_delChart.setText(QCoreApplication.translate("Studious", u"Xo\u00e1 d\u1eef li\u1ec7u", None))
        self.label.setText(QCoreApplication.translate("Studious", u"B\u1ea1n \u0111\u00e3 s\u1eed d\u1ee5ng Pomodoro 1 gi\u1edd ng\u00e0y h\u00f4m nay", None))
        self.cB_chooseDate.setItemText(0, QCoreApplication.translate("Studious", u"3 ng\u00e0y", None))
        self.cB_chooseDate.setItemText(1, QCoreApplication.translate("Studious", u"7 ng\u00e0y", None))
        self.cB_chooseDate.setItemText(2, QCoreApplication.translate("Studious", u"30 ng\u00e0y", None))
        self.cB_chooseDate.setItemText(3, QCoreApplication.translate("Studious", u"90 ng\u00e0y", None))
        self.cB_chooseDate.setItemText(4, QCoreApplication.translate("Studious", u"365 ng\u00e0y", None))

        self.Background.setText("")
        self.pushButton.setText("")
    # retranslateUi

