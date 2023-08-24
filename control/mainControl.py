import datetime
import requests
from PyQt6.QtCore import *
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtMultimedia import *
from PyQt6.QtCharts import *
from random import choice
from view import *
from .fileDataControl import *

class StudiousFunc:
    def __init__(self, widgets):
        global wgs
        wgs = widgets
        self.initialize_variables()
        self.initialize_ui()
        self.initialize_events()

    def initialize_variables(self):
        global isFwgsOn, isPwgsOn
        isFwgsOn = False
        isPwgsOn = False
        self.file = fileDataControl()
        self.qoutes = choice(list_quotes)
        self.clock_onoff = False
        self.music_onoff = True
        self.wtime, self.rtime = 25, 5
        self.dotoCurrent = "Chưa hoàn thành"
        self.countdown = countdown(self.wtime, self.rtime)
        self.box = CustomMessageBox()
        self.create_media_player()
        self.create_chart()
        self.chat = chatBot()
        self.file.readTableData()
        self.setDataWork()

    def initialize_ui(self):
        wgs.lb_m_quote.setText(self.qoutes)
        wgs.label.setText(self.file.totalTimeDay())
        wgs.lb_m_time.setText(f"{self.wtime}:00")

    def initialize_events(self):
        wgs.btn_m_startstop.clicked.connect(self.start_clock)
        wgs.btn_m_next.clicked.connect(self.next_clock)
        wgs.btn_m_audio.clicked.connect(self.onoff_audio)
        wgs.btn_m_pin.clicked.connect(self.start_dialog)
        wgs.btn_m_fs.clicked.connect(self.start_fs)
        wgs.cB_m_task.currentIndexChanged.connect(self.on_combobox_changed)
        wgs.btn_m_delChart.clicked.connect(self.delChartcheck)
        wgs.btn_3_edit.clicked.connect(self.start_weekDialog)
        wgs.btn_5_start.clicked.connect(self.start_breath)
        wgs.btn_4_send.clicked.connect(lambda: self.chat.start())
        wgs.tW_3_todoToday.itemClicked.connect(self.showDescribeWork)

    def create_media_player(self):
        self.bg_music = QUrl.fromLocalFile('assert/music/music.mp3')
        self.media_player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.audio.setVolume(1)
        self.media_player.setAudioOutput(self.audio)
        self.media_player.setSource(self.bg_music)
        self.media_player.setLoops(24)
        self.onoff_audio()
        
    def create_chart(self):
        self.chart = chart(self.file)
        wgs.cB_chooseDate.currentIndexChanged.connect(self.chart.dataChange)

    def delChartcheck(self):
        self.box.exec()

        if self.box.clickedButton() == self.box.buttonY:
            self.file.default_data()
            self.chart.dataChange()
        
        return False

    #Func control app
    def start_clock(self):
        if self.clock_onoff == False:
            self.clock_onoff = True
            self.qthread = audioFunc(QThread,'assert/music/pause.mp3')
            self.qthread.start()
            self.countdown.start_timer()
            wgs.btn_m_startstop.setIcon(QIcon("assert/pause.png"))
            if isFwgsOn:
                Fwgs.btn_startstop.setIcon(QIcon("assert/pause.png"))
            if self.countdown.work_or_rest == True:
                wgs.cB_m_task.setEnabled(not self.countdown.work_or_rest)
                if isFwgsOn:
                    Fwgs.cB_task.setEnabled(not self.countdown.work_or_rest)
            else:
                wgs.cB_m_task.setEnabled(not self.countdown.work_or_rest)
                if isFwgsOn:
                    Fwgs.cB_task.setEnabled(not self.countdown.work_or_rest)
        else:
            self.clock_onoff = False
            self.qthread = audioFunc(QThread,'assert/music/unpause.mp3')
            self.qthread.start()
            wgs.btn_m_startstop.setIcon(QIcon("assert/start.png"))
            if isFwgsOn:
                Fwgs.btn_startstop.setIcon(QIcon("assert/start.png"))
            self.countdown.stop_timer()    

    def next_clock(self):
        wgs.btn_m_startstop.setIcon(QIcon("assert/start.png"))
        if isFwgsOn:
            Fwgs.btn_startstop.setIcon(QIcon("assert/start.png"))
        self.qthread = audioFunc(QThread,'assert/music/end.mp3')
        self.qthread.start()
        if self.countdown.work_or_rest: 
            wgs.lb_m_time.setStyleSheet('color: rgb(251, 238, 172)')
            self.file.dataTimeJson[self.file.ntime][wgs.cB_m_task.currentText()] += round((self.countdown.wtime-self.countdown.time_left/60)/60, 1)
            self.file.writeDataTime()
            wgs.label.setText(self.file.totalTimeDay())
            wgs.cB_m_task.setEnabled(self.countdown.work_or_rest)
            if isFwgsOn:    
                Fwgs.lb_time.setStyleSheet("font: 128pt \"Arial\";\n"
                                            "color: rgb(251, 238, 172);\n"
                                            "border: 0px;\n"
                                            "qproperty-alignment: \'AlignCenter\';\n"
                                            "qproperty-margin: auto;")
                Fwgs.cB_task.setEnabled(self.countdown.work_or_rest)
            if isPwgsOn:
                Pwgs.lb_time.setStyleSheet('color: rgb(251, 238, 172)')
        else:
            wgs.lb_m_time.setStyleSheet('color: rgb(249, 245, 246)')
            if isFwgsOn:
                Fwgs.lb_time.setStyleSheet("font: 128pt \"Arial\";\n"
"color: rgb(249, 245, 246);\n"
"border: 0px;\n"
"qproperty-alignment: \'AlignCenter\';\n"
"qproperty-margin: auto;")
            if isPwgsOn:
                Pwgs.lb_time.setStyleSheet('rgb(249, 245, 246)')
        self.countdown.next_timer()
        self.clock_onoff = False
        wgs.lb_m_time.setText(f"{self.countdown.mtime}:00")
        if isPwgsOn:
            Pwgs.lb_time.setText(f"{self.countdown.mtime}:00")
        if isFwgsOn:
            Fwgs.lb_time.setText(f"{self.countdown.mtime}:00")
        self.chart.dataChange()

    def onoff_audio(self):
        if self.music_onoff:
            self.media_player.play()
            wgs.btn_m_audio.setIcon(QIcon("assert/audio-on.png"))
            if isFwgsOn:
                Fwgs.btn_audio.setIcon(QIcon("assert/audio-on.png"))
            self.music_onoff = False
        elif self.music_onoff == False:
            self.media_player.pause()
            wgs.btn_m_audio.setIcon(QIcon("assert/audio-off.png"))
            if isFwgsOn:
                Fwgs.btn_audio.setIcon(QIcon("assert/audio-off.png"))
            self.music_onoff = True
    
    def on_combobox_changed(self):
        if isFwgsOn:
            selected_option = Fwgs.cB_task.currentText()
        else:
            selected_option = wgs.cB_m_task.currentText()
        wgs.cB_m_task.setCurrentText(selected_option)
        if isPwgsOn:
            Pwgs.lb_task.setText(selected_option)
    
    def start_dialog(self):
        if isPwgsOn:
            self.diaLog.close()
        else:
            self.diaLog = DialogFunc()
            wgs.btn_m_pin.setIcon(QIcon("assert/unpin.png"))
        if not self.countdown.work_or_rest:
            Pwgs.lb_time.setStyleSheet('color: rgb(251, 238, 172)')
        Pwgs.lb_time.setText(f"{self.countdown.mtime}:00")

    def start_fs(self):
        self.fs = fullScreenFunc()
        Fwgs.cB_task.currentIndexChanged.connect(self.on_combobox_changed)
        if not self.countdown.work_or_rest:
            Fwgs.lb_time.setStyleSheet("font: 128pt \"Arial\";\n"
                                    "color: rgb(251, 238, 172);\n"
                                    "border: 0px;\n"
                                    "qproperty-alignment: \'AlignCenter\';\n"
                                    "qproperty-margin: auto;")
        if self.clock_onoff:
            Fwgs.btn_startstop.setIcon(QIcon("assert/pause.png"))
        if self.music_onoff:
            Fwgs.btn_audio.setIcon(QIcon("assert/audio-off.png"))
        Fwgs.lb_time.setText(f"{self.countdown.mtime}:00")
        Fwgs.btn_startstop.clicked.connect(self.start_clock)
        Fwgs.btn_next.clicked.connect(self.next_clock)
        Fwgs.btn_audio.clicked.connect(self.onoff_audio)
        Fwgs.cB_task.setCurrentText(wgs.cB_m_task.currentText())
        Fwgs.btn_exit.clicked.connect(lambda: Fwgs.close())
        Fwgs.bottomQuote.setText(self.qoutes)
        Fwgs.cB_task.setEnabled(not self.clock_onoff)

    def start_weekDialog(self):
        self.wDialog = weekDialogFunc(self.file, self.setDataWork)


    def start_breath(self):
        self.breath = BreathingCircleAnimation()
        self.breath.show()

    def setDataWork(self):
        date_format = "%d/%m/%Y"
        start_date_obj = datetime.datetime.strptime(self.file._table_data[0][0], date_format)
        end_date_obj = datetime.datetime.strptime(self.file.ntime, date_format)
        delta = end_date_obj - start_date_obj
        self.day_left = delta.days + 1
        self.todoDay = 0
        self.combo = []
        for i in range(1, 8):
            if self.file._table_data[i][self.day_left] == '':    pass
            else:
                self.combo.append(comboCompanies(wgs.tW_3_todoToday))
                wgs.tW_3_todoToday.setCellWidget(self.todoDay, 1, self.combo[-1])
                wgs.tW_3_todoToday.setItem(self.todoDay, 0, QTableWidgetItem(f"{self.file._table_data[i][self.day_left]}"))
                self.combo[-1].currentIndexChanged.connect(self.todoDoneTask)
                self.todoDay += 1
        wgs.lb_4_complete.setText(f"     Tổng cộng: {self.todoDay} Đã hoàn thành: 0 Chưa hoàn thành: {self.todoDay} Đang làm: 0")
    
    def showDescribeWork(self, item):
        self.row = item.row()
        self.col = self.day_left - 1
        data = self.file.readDescribeData()
        wgs.textBrowser_3_des.setPlainText(data[self.row][self.col])

    def todoDoneTask(self):
        check = []
        for i in self.combo:
            if i == []: pass
            else:
                check.append(i.currentText())
        done = check.count("Đã hoàn thành")
        doing = check.count("Đang làm")
        wgs.lb_4_complete.setText(f"     Tổng cộng: {self.todoDay} Đã hoàn thành: {done} Chưa hoàn thành: {self.todoDay - done - doing} Đang làm: {doing}")

class audioFunc(QThread):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, parent: QObject, path) -> None:
        super().__init__()
        self.path = path

    def run(self):
        self._media_content = QUrl.fromLocalFile(self.path)
        self._media_player = QMediaPlayer()
        self._audio = QAudioOutput()
        self._audio.setVolume(1)
        self._media_player.setAudioOutput(self._audio)
        self._media_player.setSource(self._media_content)
        self._media_player.play()

class DialogFunc(Ui_Dialog):
    def __init__(self):
        global Pwgs, isPwgsOn
        super().__init__()
        Pwgs = self
        Pwgs.setupUi(self)
        Pwgs.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        Pwgs.lb_task.setText(wgs.cB_m_task.currentText())
        Pwgs.show()
        isPwgsOn = True

    def closeEvent(self, event):
        global isPwgsOn
        isPwgsOn = False
        wgs.btn_m_pin.setIcon(QIcon("assert/pin.png"))
        Pwgs.close()

class fullScreenFunc(StudiousFS):
    def __init__(self):
        global isFwgsOn
        super().__init__()
        global Fwgs
        Fwgs = self
        Fwgs.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        Fwgs.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        Fwgs.show()
        isFwgsOn = True

    def closeEvent(self, event):
        global isFwgsOn
        isFwgsOn = False
        Fwgs.close()

    def focusOutEvent(self, event):
        # Prevent the window from losing focus
        self.activateWindow()

        return super().event(event)
    
class weekDialogFunc(Week_Dialog):
    def __init__(self, file, fn):
        super().__init__()
        self.wgt = self
        self.wgt.setupUi(self)
        
        self.file = file

        self.describeData = self.file.readDescribeData()
        self.wgt.buttonBox.accepted.connect(self.updateData)
        self.wgt.tableWidget.itemClicked.connect(self.getDescribeItem)
        self.file.readTableData()
        self.file.setTableData(self.wgt)
        self.wgt.plainTextEdit.setReadOnly(True)
        self.fn = fn
        self.row, self.col = 0, 0
        self.edit = False

        self.wgt.show()
    
    def updateData(self):
        self.describeData[self.row][self.col] = self.wgt.plainTextEdit.toPlainText()
        self.file.writeDescribeData(self.describeData)
        self.file.writeTableData(self.wgt)
        self.fn()

    def getDescribeItem(self, item):
        self.wgt.plainTextEdit.setReadOnly(False)
        if not self.edit:
            self.row = item.row()
            self.col = item.column()
            self.wgt.plainTextEdit.setPlainText(self.describeData[self.row][self.col])
            self.edit = True
        else:
            self.describeData[self.row][self.col] = self.wgt.plainTextEdit.toPlainText()
            self.wgt.plainTextEdit.clear()
            self.row = item.row()
            self.col = item.column()
            self.wgt.plainTextEdit.setPlainText(self.describeData[self.row][self.col])
                     
class countdown:
    def __init__(self, work_time:int, rest_time:int):
        self.wtime = work_time
        self.rtime = rest_time
        self.work_or_rest = True
        self.mtime = self.wtime
        self.time_left = self.mtime*60
        self.timer = QTimer()

    def start_timer(self):
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start(1000)  # Update every second

    def stop_timer(self):
        self.timer.disconnect()

    def update_countdown(self):
        self.time_left -= 1

        if self.time_left >= 0:
            # Format the remaining time as MM:SS
            self.minutes, self.seconds = divmod(self.time_left, 60)
            wgs.lb_m_time.setText(f"{self.minutes:02}:{self.seconds:02}")
            if isPwgsOn:
                Pwgs.lb_time.setText(f"{self.minutes:02}:{self.seconds:02}")
            if isFwgsOn:
                Fwgs.lb_time.setText(f"{self.minutes:02}:{self.seconds:02}")
        else:
            self.next_timer()

    def next_timer(self):
        if self.time_left == -1:
            self.time_left = self.mtime*60
            wgs.btn_m_next.click()
        else:
            try: self.timer.disconnect()
            except: pass
            if self.work_or_rest:
                self.work_or_rest = False
                self.mtime = self.rtime
            else:
                self.work_or_rest = True
                self.mtime = self.wtime
                if isFwgsOn:
                    Fwgs.lb_time.setStyleSheet("font: 128pt \"Arial\";\n"
    "color: rgb(249, 245, 246);\n"
    "border: 0px;\n"
    "qproperty-alignment: \'AlignCenter\';\n"
    "qproperty-margin: auto;")
            self.time_left = self.mtime*60

class KeyboardWidget(QWidget):
    keyPressed = pyqtSignal(str)

    def keyPressEvent(self, keyEvent):
        self.keyPressed.emit(keyEvent.text())

class chatBot(QThread):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self) -> None:
        super(chatBot, self).__init__()
        self.api = 'dc5f122151msh883ed682cbadc9cp113b09jsn67cb02e5ab7d'
        self.api_url = 'https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions'
        
        self.model = ChatLogModel()
        wgs.LV_chatView.setModel(self.model)

        message_delegate = DrawSpeechBubbleDelegate()
        wgs.LV_chatView.setItemDelegate(message_delegate)

        self.model.appendMessage("Chào bạn, tôi là Studious. Liệu tôi có thể giúp gì cho bạn?", "chatbot")

    def run(self):
        user_input = wgs.PtE_chatBot.toPlainText()
        if user_input.translate(str.maketrans('', '', '''
     
 
''')) in ["", None]: return
        self.model.appendMessage(user_input, "user")
        wgs.PtE_chatBot.clear()

        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": self.api,
            "X-RapidAPI-Host": "chatgpt-best-price.p.rapidapi.com"
        }

        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
		{
			"role": "user",
			"content": user_input
		}
	    ]
        }

        try:
            res = requests.post(self.api_url, json=data, headers=headers)
            response = res.json()["choices"][0]["message"]["content"]
        except:
            response = "Không có kết nối Internet, vui lòng thử lại!"
        self.model.appendMessage(response, "chatbot")

class chart:
    def __init__(self, file) -> None:
        self.file = file
        self.addChart = False
        self.dataChange()

    def dataChange(self):
        if self.addChart:
            wgs.columnChart.layout().removeWidget(self.colChart._chart_view)
            wgs.pieChart.layout().removeWidget(self._chart_view)
        self.curentChoose = wgs.cB_chooseDate.currentText()
        self.time, self.totalTime, self.detailTime = self.file.dataChart(self.curentChoose)
        self.columnChart()
        self.circleChart()

    def columnChart(self):
        self.colData = QBarSet("Tổng thời gian tập trung")
        self.colData.setLabelFont(QFont("Arial", 12))
        self.colData.append(self.totalTime)

        self.colSerise = QBarSeries()
        self.colSerise.append(self.colData)

        self.colChart = QChart()
        self.colChart.addSeries(self.colSerise)
        self.colChart.setTitle(f"Biểu đồ so sánh tổng thời gian tập trung trong {self.curentChoose}")
        self.colChart.setTitleFont(QFont("Arial", 12))
        self.colChart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        self.colChart.categories = self.time
        self.colChart.axis_x = QBarCategoryAxis()
        self.colChart.axis_x.append(self.colChart.categories)
        self.colChart.addAxis(self.colChart.axis_x, Qt.AlignmentFlag.AlignBottom)
        self.colSerise.attachAxis(self.colChart.axis_x)

        self.colChart.axis_y = QValueAxis()
        self.colChart.axis_y.setRange(0, max(self.totalTime)+3)
        self.colChart.addAxis(self.colChart.axis_y, Qt.AlignmentFlag.AlignLeft)
        self.colSerise.attachAxis(self.colChart.axis_y)

        self.colChart.legend().setVisible(True)
        self.colChart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        self.colChart._chart_view = QChartView(self.colChart)
        self.colChart._chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        self.addChart = True
        wgs.columnChart.layout().addWidget(self.colChart._chart_view)
    
    def circleChart(self):
        self.pieSerise = QPieSeries()
        for i in self.detailTime:
            self.pieSerise.append(i[0], i[1])
        colors = [QColor("#66b266"), QColor("#3366cc"), QColor("#ff5050"), QColor("#ffff66")]
        font = QFont("Arial", 10)
        self.pieSerise.setLabelsPosition(QPieSlice.LabelPosition.LabelInsideNormal)
        for i, slice in enumerate(self.pieSerise.slices()):
            slice.setLabel("{:.2f}%".format(100 * slice.percentage()))
            slice.setColor(colors[i])
            slice.setLabelFont(font)
            slice.setLabelColor(QColor("#000000"))

        self.pieChart = QChart()
        self.pieChart.legend()
        self.pieChart.setTitle("Biểu đồ so sánh phân bố nhiệm vụ")
        self.pieChart.setTitleFont(QFont("Arial", 12))
        self.pieChart.addSeries(self.pieSerise)

        for i, data in enumerate(self.detailTime):
            self.pieChart.legend().markers(self.pieSerise)[i].setLabel(data[0])
            self.pieChart.legend().markers(self.pieSerise)[i].setFont(QFont("Arial", 11))
        self.pieChart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        self._chart_view = QChartView(self.pieChart)
        self._chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.pieSerise.setLabelsVisible(True)

        self.addChart = True
        wgs.pieChart.layout().addWidget(self._chart_view)