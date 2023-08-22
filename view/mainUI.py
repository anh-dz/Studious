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
        Studious.resize(820, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Studious.sizePolicy().hasHeightForWidth())
        Studious.setSizePolicy(sizePolicy)
        Studious.setMinimumSize(QtCore.QSize(820, 560))
        Studious.setMaximumSize(QtCore.QSize(820, 560))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assert/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Studious.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=Studious)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(820, 560))
        self.centralwidget.setMaximumSize(QtCore.QSize(820, 560))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assert/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_menu.setIcon(icon1)
        self.btn_lB_menu.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_menu.setCheckable(False)
        self.btn_lB_menu.setObjectName("btn_lB_menu")
        self.layoutWidget = QtWidgets.QWidget(parent=self.wg_leftBar)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 85, 151, 366))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layout_leftBar = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layout_leftBar.setContentsMargins(0, 0, 0, 0)
        self.layout_leftBar.setObjectName("layout_leftBar")
        self.btn_lB_1 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_1.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_1.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assert/pomodoro.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_1.setIcon(icon2)
        self.btn_lB_1.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_1.setObjectName("btn_lB_1")
        self.layout_leftBar.addWidget(self.btn_lB_1)
        self.btn_lB_2 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_2.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_2.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assert/chart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_2.setIcon(icon3)
        self.btn_lB_2.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_2.setObjectName("btn_lB_2")
        self.layout_leftBar.addWidget(self.btn_lB_2)
        self.btn_lB_3 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_3.setStyleSheet("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assert/habit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_3.setIcon(icon4)
        self.btn_lB_3.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_3.setObjectName("btn_lB_3")
        self.layout_leftBar.addWidget(self.btn_lB_3)
        self.btn_lB_4 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_4.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_4.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assert/botchat.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_4.setIcon(icon5)
        self.btn_lB_4.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_4.setObjectName("btn_lB_4")
        self.layout_leftBar.addWidget(self.btn_lB_4)
        self.btn_lB_5 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_5.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_5.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assert/relax.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_5.setIcon(icon6)
        self.btn_lB_5.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_5.setObjectName("btn_lB_5")
        self.layout_leftBar.addWidget(self.btn_lB_5)
        self.btn_lB_6 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_6.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_lB_6.setStyleSheet("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("assert/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_6.setIcon(icon7)
        self.btn_lB_6.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_6.setObjectName("btn_lB_6")
        self.layout_leftBar.addWidget(self.btn_lB_6)
        self.btn_lB_7 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_lB_7.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_lB_7.setStyleSheet("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("assert/about.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_7.setIcon(icon8)
        self.btn_lB_7.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_7.setObjectName("btn_lB_7")
        self.layout_leftBar.addWidget(self.btn_lB_7)
        self.btn_lB_ques = QtWidgets.QPushButton(parent=self.wg_leftBar)
        self.btn_lB_ques.setGeometry(QtCore.QRect(0, 510, 41, 40))
        self.btn_lB_ques.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_lB_ques.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_lB_ques.setFont(font)
        self.btn_lB_ques.setStyleSheet("QPushButton:hover{\n"
"    background-color: transparent;\n"
"}")
        self.btn_lB_ques.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("assert/ques.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_lB_ques.setIcon(icon9)
        self.btn_lB_ques.setIconSize(QtCore.QSize(32, 32))
        self.btn_lB_ques.setCheckable(False)
        self.btn_lB_ques.setObjectName("btn_lB_ques")
        self.sW_main = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.sW_main.setGeometry(QtCore.QRect(40, 0, 781, 561))
        self.sW_main.setStyleSheet("* {\n"
"    background-color: transparent;\n"
"    color: rgb(249, 245, 246);\n"
"    font: 18pt \"Arial\";\n"
"}\n"
"QTextBrowser{\n"
"    background-color: rgba(52, 22, 85, 70%);\n"
"    border: 0px solid;\n"
"    border-radius: 5px;\n"
"}\n"
"QListView{\n"
"    background-color: rgba(52, 22, 85, 70%);\n"
"    border: 0px solid;\n"
"    border-radius: 5px;\n"
"}\n"
"QPlainTextEdit{\n"
"    background-color: rgba(52, 22, 85, 70%);\n"
"    border: 0px solid;\n"
"    border-radius: 5px;\n"
"}\n"
"QToolButton{\n"
"    border: 0px;\n"
"}\n"
"QComboBox{\n"
"    background-color: rgba(52, 22, 85, 50%);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    color: rgb(249, 245, 246);\n"
"    font: 14pt \"Arial\";\n"
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
"}\n"
"QTableWidget {\n"
"    background-color: rgba(52, 22, 85, 50%);\n"
"    border: 0px;\n"
"}\n"
"QTableWidget::item {\n"
"    padding: 7px;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgba(52, 22, 85, 50%);\n"
"    padding: 4px;\n"
"    border: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: 0px;\n"
"    background:white;\n"
"    width:5px;\n"
"    border-radius: 5px;\n"
"    margin: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 0px;\n"
"    border: 0px;\n"
"    border-radius: 5px;\n"
"    background-color: black;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.sW_main.setObjectName("sW_main")
        self.page_m_pom = QtWidgets.QWidget()
        self.page_m_pom.setStyleSheet("QLabel{\n"
"    font: 72pt \"Arial\";\n"
"    qproperty-alignment: \'AlignCenter\';\n"
"    qproperty-margin: auto;\n"
"}")
        self.page_m_pom.setObjectName("page_m_pom")
        self.lb_m_time = QtWidgets.QLabel(parent=self.page_m_pom)
        self.lb_m_time.setGeometry(QtCore.QRect(243, 180, 311, 141))
        self.lb_m_time.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.lb_m_time.setStyleSheet("color: rgb(249, 245, 246);")
        self.lb_m_time.setObjectName("lb_m_time")
        self.btn_m_audio = QtWidgets.QToolButton(parent=self.page_m_pom)
        self.btn_m_audio.setGeometry(QtCore.QRect(710, 30, 51, 51))
        self.btn_m_audio.setStyleSheet("")
        self.btn_m_audio.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("assert/audio-on.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_m_audio.setIcon(icon10)
        self.btn_m_audio.setIconSize(QtCore.QSize(50, 50))
        self.btn_m_audio.setObjectName("btn_m_audio")
        self.lb_m_quote = QtWidgets.QLabel(parent=self.page_m_pom)
        self.lb_m_quote.setGeometry(QtCore.QRect(40, 442, 662, 120))
        self.lb_m_quote.setStyleSheet("font: 16pt \"Arial\";\n"
"color: rgb(249, 245, 246);\n"
"padding: 2px 7px;")
        self.lb_m_quote.setWordWrap(True)
        self.lb_m_quote.setObjectName("lb_m_quote")
        self.btn_m_pin = QtWidgets.QToolButton(parent=self.page_m_pom)
        self.btn_m_pin.setGeometry(QtCore.QRect(650, 30, 51, 51))
        self.btn_m_pin.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("assert/pin.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_m_pin.setIcon(icon11)
        self.btn_m_pin.setIconSize(QtCore.QSize(50, 50))
        self.btn_m_pin.setObjectName("btn_m_pin")
        self.btn_m_fs = QtWidgets.QToolButton(parent=self.page_m_pom)
        self.btn_m_fs.setGeometry(QtCore.QRect(700, 490, 51, 51))
        self.btn_m_fs.setStyleSheet("")
        self.btn_m_fs.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("assert/fs.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_m_fs.setIcon(icon12)
        self.btn_m_fs.setIconSize(QtCore.QSize(50, 50))
        self.btn_m_fs.setObjectName("btn_m_fs")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.page_m_pom)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 330, 160, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_m_startstop = QtWidgets.QToolButton(parent=self.horizontalLayoutWidget)
        self.btn_m_startstop.setMaximumSize(QtCore.QSize(51, 51))
        self.btn_m_startstop.setStyleSheet("")
        self.btn_m_startstop.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("assert/start.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_m_startstop.setIcon(icon13)
        self.btn_m_startstop.setIconSize(QtCore.QSize(50, 50))
        self.btn_m_startstop.setObjectName("btn_m_startstop")
        self.horizontalLayout.addWidget(self.btn_m_startstop)
        self.btn_m_next = QtWidgets.QToolButton(parent=self.horizontalLayoutWidget)
        self.btn_m_next.setMaximumSize(QtCore.QSize(51, 51))
        self.btn_m_next.setStyleSheet("")
        self.btn_m_next.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("assert/next.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_m_next.setIcon(icon14)
        self.btn_m_next.setIconSize(QtCore.QSize(50, 50))
        self.btn_m_next.setObjectName("btn_m_next")
        self.horizontalLayout.addWidget(self.btn_m_next)
        self.cB_m_task = QtWidgets.QComboBox(parent=self.page_m_pom)
        self.cB_m_task.setGeometry(QtCore.QRect(273, 130, 251, 31))
        self.cB_m_task.setStyleSheet("")
        self.cB_m_task.setObjectName("cB_m_task")
        self.cB_m_task.addItem("")
        self.cB_m_task.addItem("")
        self.sW_main.addWidget(self.page_m_pom)
        self.page_m_2 = QtWidgets.QWidget()
        self.page_m_2.setStyleSheet("* {\n"
"    font: 18pt \"Arial\";\n"
"    border: 0px;\n"
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
        self.page_m_2.setObjectName("page_m_2")
        self.columnChart = QtWidgets.QWidget(parent=self.page_m_2)
        self.columnChart.setGeometry(QtCore.QRect(20, 90, 412, 392))
        self.columnChart.setMinimumSize(QtCore.QSize(412, 392))
        self.columnChart.setObjectName("columnChart")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.columnChart)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pieChart = QtWidgets.QWidget(parent=self.page_m_2)
        self.pieChart.setGeometry(QtCore.QRect(439, 89, 331, 392))
        self.pieChart.setMinimumSize(QtCore.QSize(331, 392))
        self.pieChart.setObjectName("pieChart")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.pieChart)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_m_delChart = QtWidgets.QPushButton(parent=self.page_m_2)
        self.btn_m_delChart.setGeometry(QtCore.QRect(650, 29, 112, 32))
        self.btn_m_delChart.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_m_delChart.setStyleSheet("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("assert/del.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_m_delChart.setIcon(icon15)
        self.btn_m_delChart.setIconSize(QtCore.QSize(23, 23))
        self.btn_m_delChart.setObjectName("btn_m_delChart")
        self.label = QtWidgets.QLabel(parent=self.page_m_2)
        self.label.setGeometry(QtCore.QRect(180, 500, 461, 41))
        self.label.setStyleSheet("color: rgb(249, 245, 246);\n"
"font: 18pt \"Arial\";")
        self.label.setObjectName("label")
        self.cB_chooseDate = QtWidgets.QComboBox(parent=self.page_m_2)
        self.cB_chooseDate.setGeometry(QtCore.QRect(160, 30, 171, 31))
        self.cB_chooseDate.setStyleSheet("")
        self.cB_chooseDate.setObjectName("cB_chooseDate")
        self.cB_chooseDate.addItem("")
        self.cB_chooseDate.addItem("")
        self.cB_chooseDate.addItem("")
        self.cB_chooseDate.addItem("")
        self.cB_chooseDate.addItem("")
        self.cB_chooseDate.addItem("")
        self.btn_m_delChart.raise_()
        self.label.raise_()
        self.cB_chooseDate.raise_()
        self.pieChart.raise_()
        self.columnChart.raise_()
        self.sW_main.addWidget(self.page_m_2)
        self.page_m_3 = QtWidgets.QWidget()
        self.page_m_3.setObjectName("page_m_3")
        self.lb_3_date = QtWidgets.QLabel(parent=self.page_m_3)
        self.lb_3_date.setGeometry(QtCore.QRect(160, 30, 330, 40))
        self.lb_3_date.setStyleSheet("font: 24pt;")
        self.lb_3_date.setObjectName("lb_3_date")
        self.LB = QtWidgets.QLabel(parent=self.page_m_3)
        self.LB.setGeometry(QtCore.QRect(120, 375, 120, 30))
        self.LB.setStyleSheet("font: 24pt;")
        self.LB.setObjectName("LB")
        self.textBrowser_3_des = QtWidgets.QTextBrowser(parent=self.page_m_3)
        self.textBrowser_3_des.setGeometry(QtCore.QRect(60, 410, 661, 131))
        self.textBrowser_3_des.setObjectName("textBrowser_3_des")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.page_m_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 80, 671, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Table = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Table.setContentsMargins(0, 0, 0, 0)
        self.Table.setObjectName("Table")
        self.tW_3_todoToday = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget)
        self.tW_3_todoToday.setStyleSheet("")
        self.tW_3_todoToday.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tW_3_todoToday.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tW_3_todoToday.setProperty("showDropIndicator", False)
        self.tW_3_todoToday.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tW_3_todoToday.setObjectName("tW_3_todoToday")
        self.tW_3_todoToday.setColumnCount(2)
        self.tW_3_todoToday.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tW_3_todoToday.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tW_3_todoToday.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tW_3_todoToday.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tW_3_todoToday.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tW_3_todoToday.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tW_3_todoToday.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tW_3_todoToday.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tW_3_todoToday.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tW_3_todoToday.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tW_3_todoToday.setItem(0, 0, item)
        self.tW_3_todoToday.horizontalHeader().setCascadingSectionResizes(True)
        self.tW_3_todoToday.horizontalHeader().setDefaultSectionSize(320)
        self.tW_3_todoToday.horizontalHeader().setMinimumSectionSize(80)
        self.tW_3_todoToday.horizontalHeader().setSortIndicatorShown(False)
        self.tW_3_todoToday.horizontalHeader().setStretchLastSection(True)
        self.tW_3_todoToday.verticalHeader().setDefaultSectionSize(39)
        self.tW_3_todoToday.verticalHeader().setMinimumSectionSize(39)
        self.Table.addWidget(self.tW_3_todoToday)
        self.lb_4_complete = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.lb_4_complete.setStyleSheet("font: italic 18pt;\n"
"color: rgb(255, 196, 54);")
        self.lb_4_complete.setObjectName("lb_4_complete")
        self.Table.addWidget(self.lb_4_complete)
        self.btn_3_edit = QtWidgets.QToolButton(parent=self.page_m_3)
        self.btn_3_edit.setGeometry(QtCore.QRect(710, 30, 40, 40))
        self.btn_3_edit.setStyleSheet("")
        self.btn_3_edit.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("assert/edit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_3_edit.setIcon(icon16)
        self.btn_3_edit.setIconSize(QtCore.QSize(32, 32))
        self.btn_3_edit.setObjectName("btn_3_edit")
        self.sW_main.addWidget(self.page_m_3)
        self.page_m_4 = QtWidgets.QWidget()
        self.page_m_4.setObjectName("page_m_4")
        self.LV_chatView = QtWidgets.QListView(parent=self.page_m_4)
        self.LV_chatView.setGeometry(QtCore.QRect(20, 30, 741, 451))
        self.LV_chatView.setStyleSheet("")
        self.LV_chatView.setObjectName("LV_chatView")
        self.PtE_chatBot = QtWidgets.QPlainTextEdit(parent=self.page_m_4)
        self.PtE_chatBot.setGeometry(QtCore.QRect(112, 500, 601, 51))
        self.PtE_chatBot.setStyleSheet("")
        self.PtE_chatBot.setObjectName("PtE_chatBot")
        self.btn_4_send = QtWidgets.QToolButton(parent=self.page_m_4)
        self.btn_4_send.setGeometry(QtCore.QRect(720, 500, 48, 48))
        self.btn_4_send.setStyleSheet("")
        self.btn_4_send.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("assert/send.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_4_send.setIcon(icon17)
        self.btn_4_send.setIconSize(QtCore.QSize(48, 48))
        self.btn_4_send.setObjectName("btn_4_send")
        self.BTN_ICONUSER = QtWidgets.QToolButton(parent=self.page_m_4)
        self.BTN_ICONUSER.setGeometry(QtCore.QRect(60, 500, 48, 48))
        self.BTN_ICONUSER.setStyleSheet("")
        self.BTN_ICONUSER.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("assert/user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.BTN_ICONUSER.setIcon(icon18)
        self.BTN_ICONUSER.setIconSize(QtCore.QSize(48, 48))
        self.BTN_ICONUSER.setObjectName("BTN_ICONUSER")
        self.sW_main.addWidget(self.page_m_4)
        self.page_m_5 = QtWidgets.QWidget()
        self.page_m_5.setObjectName("page_m_5")
        self.tB_5_breath = QtWidgets.QTextBrowser(parent=self.page_m_5)
        self.tB_5_breath.setGeometry(QtCore.QRect(40, 30, 701, 431))
        self.tB_5_breath.setStyleSheet("color: white;")
        self.tB_5_breath.setObjectName("tB_5_breath")
        self.btn_5_start = QtWidgets.QPushButton(parent=self.page_m_5)
        self.btn_5_start.setGeometry(QtCore.QRect(290, 480, 221, 51))
        self.btn_5_start.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_5_start.setStyleSheet("QPushButton{\n"
"    background-color: rgba(52, 22, 85, 70%);\n"
"    color: rgb(249, 245, 246);\n"
"    font: 24pt \"Arial\";\n"
"    border-radius: 5px;\n"
"    text-align: left;\n"
"    padding: 2px 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(52, 22, 85, 100%);\n"
"}")
        self.btn_5_start.setIcon(icon6)
        self.btn_5_start.setIconSize(QtCore.QSize(23, 23))
        self.btn_5_start.setObjectName("btn_5_start")
        self.sW_main.addWidget(self.page_m_5)
        self.page_m_6 = QtWidgets.QWidget()
        self.page_m_6.setObjectName("page_m_6")
        self.LB_2 = QtWidgets.QLabel(parent=self.page_m_6)
        self.LB_2.setGeometry(QtCore.QRect(130, 50, 191, 61))
        self.LB_2.setStyleSheet("font: 48pt;")
        self.LB_2.setObjectName("LB_2")
        self.sW_setting = QtWidgets.QStackedWidget(parent=self.page_m_6)
        self.sW_setting.setGeometry(QtCore.QRect(130, 110, 641, 441))
        self.sW_setting.setObjectName("sW_setting")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.checkBox_space = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox_space.setGeometry(QtCore.QRect(50, 310, 421, 50))
        self.checkBox_space.setStyleSheet("font: 24pt;")
        self.checkBox_space.setObjectName("checkBox_space")
        self.checkBox_autosession = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox_autosession.setGeometry(QtCore.QRect(50, 240, 391, 51))
        self.checkBox_autosession.setStyleSheet("font: 24pt;")
        self.checkBox_autosession.setObjectName("checkBox_autosession")
        self.checkBox_autostart = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox_autostart.setGeometry(QtCore.QRect(50, 90, 341, 51))
        self.checkBox_autostart.setStyleSheet("font: 24pt;")
        self.checkBox_autostart.setObjectName("checkBox_autostart")
        self.cB_6_select = QtWidgets.QComboBox(parent=self.page)
        self.cB_6_select.setGeometry(QtCore.QRect(240, 30, 191, 41))
        self.cB_6_select.setStyleSheet("font: 24pt;")
        self.cB_6_select.setObjectName("cB_6_select")
        self.cB_6_select.addItem("")
        self.cB_6_select.addItem("")
        self.cB_6_select.addItem("")
        self.checkBox_noti = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox_noti.setGeometry(QtCore.QRect(50, 160, 411, 51))
        self.checkBox_noti.setStyleSheet("font: 24pt;")
        self.checkBox_noti.setObjectName("checkBox_noti")
        self.LB_3 = QtWidgets.QLabel(parent=self.page)
        self.LB_3.setGeometry(QtCore.QRect(50, 20, 151, 61))
        self.LB_3.setStyleSheet("font: 24pt;")
        self.LB_3.setObjectName("LB_3")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 380, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.sW_setting.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.sW_setting.addWidget(self.page_2)
        self.sW_main.addWidget(self.page_m_6)
        self.page_m_7 = QtWidgets.QWidget()
        self.page_m_7.setObjectName("page_m_7")
        self.tB_7_about = QtWidgets.QTextBrowser(parent=self.page_m_7)
        self.tB_7_about.setGeometry(QtCore.QRect(50, 30, 691, 501))
        self.tB_7_about.setStyleSheet("color: white;")
        self.tB_7_about.setObjectName("tB_7_about")
        self.sW_main.addWidget(self.page_m_7)
        self.Background = QtWidgets.QLabel(parent=self.centralwidget)
        self.Background.setEnabled(True)
        self.Background.setGeometry(QtCore.QRect(0, 0, 820, 560))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Background.sizePolicy().hasHeightForWidth())
        self.Background.setSizePolicy(sizePolicy)
        self.Background.setMinimumSize(QtCore.QSize(820, 560))
        self.Background.setMaximumSize(QtCore.QSize(820, 560))
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
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 820, 560))
        self.pushButton.setStyleSheet("background-color: rgba(70, 69, 140, 40%);\n"
"border: 0px;")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.raise_()
        self.Background.raise_()
        self.sW_main.raise_()
        self.wg_leftBar.raise_()
        Studious.setCentralWidget(self.centralwidget)

        self.retranslateUi(Studious)
        self.sW_main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Studious)

    def retranslateUi(self, Studious):
        _translate = QtCore.QCoreApplication.translate
        Studious.setWindowTitle(_translate("Studious", "Studious"))
        self.btn_lB_menu.setText(_translate("Studious", "  MENU"))
        self.btn_lB_1.setText(_translate("Studious", "  Pomodoro"))
        self.btn_lB_2.setText(_translate("Studious", "  Thống kê"))
        self.btn_lB_3.setText(_translate("Studious", "  Công việc"))
        self.btn_lB_4.setText(_translate("Studious", "  BotChat"))
        self.btn_lB_5.setText(_translate("Studious", "  Thư giãn"))
        self.btn_lB_6.setText(_translate("Studious", "  Cài Đặt"))
        self.btn_lB_7.setText(_translate("Studious", "  Giới Thiệu"))
        self.lb_m_time.setText(_translate("Studious", "25:00"))
        self.lb_m_quote.setText(_translate("Studious", "CUỘC ĐỜI THẬT ĐẸP TUYỆT VỜI"))
        self.cB_m_task.setItemText(0, _translate("Studious", "Học"))
        self.cB_m_task.setItemText(1, _translate("Studious", "Làm việc"))
        self.btn_m_delChart.setText(_translate("Studious", "Xoá dữ liệu"))
        self.label.setText(_translate("Studious", "Bạn đã sử dụng Pomodoro 1 giờ ngày hôm nay"))
        self.cB_chooseDate.setItemText(0, _translate("Studious", "1 ngày"))
        self.cB_chooseDate.setItemText(1, _translate("Studious", "3 ngày"))
        self.cB_chooseDate.setItemText(2, _translate("Studious", "7 ngày"))
        self.cB_chooseDate.setItemText(3, _translate("Studious", "30 ngày"))
        self.cB_chooseDate.setItemText(4, _translate("Studious", "90 ngày"))
        self.cB_chooseDate.setItemText(5, _translate("Studious", "365 ngày"))
        self.lb_3_date.setText(_translate("Studious", "Thứ 2, ngày 20/08/2023"))
        self.LB.setText(_translate("Studious", "Mô Tả"))
        item = self.tW_3_todoToday.verticalHeaderItem(0)
        item.setText(_translate("Studious", "1"))
        item = self.tW_3_todoToday.verticalHeaderItem(1)
        item.setText(_translate("Studious", "2"))
        item = self.tW_3_todoToday.verticalHeaderItem(2)
        item.setText(_translate("Studious", "3"))
        item = self.tW_3_todoToday.verticalHeaderItem(3)
        item.setText(_translate("Studious", "4"))
        item = self.tW_3_todoToday.verticalHeaderItem(4)
        item.setText(_translate("Studious", "5"))
        item = self.tW_3_todoToday.verticalHeaderItem(5)
        item.setText(_translate("Studious", "6"))
        item = self.tW_3_todoToday.verticalHeaderItem(6)
        item.setText(_translate("Studious", "7"))
        item = self.tW_3_todoToday.horizontalHeaderItem(0)
        item.setText(_translate("Studious", "Việc phải làm"))
        item = self.tW_3_todoToday.horizontalHeaderItem(1)
        item.setText(_translate("Studious", "Trạng thái"))
        __sortingEnabled = self.tW_3_todoToday.isSortingEnabled()
        self.tW_3_todoToday.setSortingEnabled(False)
        item = self.tW_3_todoToday.item(0, 0)
        item.setText(_translate("Studious", "Học Toán"))
        self.tW_3_todoToday.setSortingEnabled(__sortingEnabled)
        self.lb_4_complete.setText(_translate("Studious", "     Tổng cộng: 7 Đã hoàn thành: 0 Chưa hoàn thành: 1 Đang làm: 0"))
        self.tB_5_breath.setHtml(_translate("Studious", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:transparent;\"><br /></p></body></html>"))
        self.btn_5_start.setText(_translate("Studious", "  Bắt đầu hít thở"))
        self.LB_2.setText(_translate("Studious", "Cài đặt"))
        self.checkBox_space.setText(_translate("Studious", "  Nhấn Space để bắt đầu phiên tiếp"))
        self.checkBox_autosession.setText(_translate("Studious", "  Tự bắt đầu phiên tiếp"))
        self.checkBox_autostart.setText(_translate("Studious", "  Tự khởi động cùng hệ thống"))
        self.cB_6_select.setItemText(0, _translate("Studious", "Baroque"))
        self.cB_6_select.setItemText(1, _translate("Studious", "Classical"))
        self.cB_6_select.setItemText(2, _translate("Studious", "Melody"))
        self.checkBox_noti.setText(_translate("Studious", "  Thông báo nghỉ ngơi trước 5 phút"))
        self.LB_3.setText(_translate("Studious", "Thể loại nhạc"))
        self.pushButton_2.setText(_translate("Studious", "--->"))
        self.tB_7_about.setHtml(_translate("Studious", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:transparent;\"><br /></p></body></html>"))
