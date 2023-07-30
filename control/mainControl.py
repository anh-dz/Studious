from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtMultimedia import *
from main import *
from random import choice
from view import *
import sys
import time

class StudiousFunc:
    def __init__(self, widgets):
        super().__init__()
        global wgs
        wgs = widgets

        #random qoutes and print in app
        list_quotes = ["Chúng ta có thể gặp nhiều thất bại nhưng chúng ta không được bị đánh bại – Maya Angelou",
                       "Tất cả những sự khó khăn thường là để chuẩn bị cho những người bình thường một số phận phi thường – C.S. Lewis",
                        "Không ai trở nên nghèo khó bằng việc chia sẻ và cho đi – Anne Frank",
                        "Không một hành động tử tế nào, dù nhỏ đến đâu, lại bị lãng phí – Aesop",
                        "Lúc này nếu ngủ bạn sẽ có một giấc mơ. Nhưng lúc này nếu học bạn sẽ giải thích được giấc mơ.",
                        "Mỗi ngày, hãy làm một việc khiến bạn cảm thấy sợ hãi. Chắc chắn bạn có thể chiến thắng nó.",
                        "Người có lòng tin vào chính mình sẽ có được lòng tin của người khác. – Ngạn ngữ Do Thái.",
                        "Hãy làm những gì bạn có thể với tất cả những gì bạn có – Theodore Roosevelt."]
        self.qoutes = choice(list_quotes)
        wgs.lb_m_quote.setText(self.qoutes)

        #connect start/stop button with clock
        self.wtime, self.rtime = 25, 5
        self.mtime = self.wtime
        wgs.lb_m_time.setText(f"{self.mtime}:00")
        wgs.btn_m_startstop.clicked.connect(self.start_clock)
        self.countdown = countdown(self.wtime, self.rtime)
        self.clock_onoff = False

        #Put clock to next session
        wgs.btn_m_next.clicked.connect(self.next_clock)

        #Turn on/off music in app
        wgs.btn_m_audio.clicked.connect(self.onoff_audio)
        self.media_content = QUrl.fromLocalFile('.\\assert\\music.mp3')
        self.music_onoff = True
        self.media_player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.audio.setVolume(40)
        self.media_player.setAudioOutput(self.audio)
        self.media_player.setSource(self.media_content)
        self.onoff_audio()

        #Turn on pinDialog
        wgs.btn_m_pin.clicked.connect(self.start_dialog)

        #Turn on full screen mode
        wgs.btn_m_fs.clicked.connect(self.start_fs)

        #Change label task connect
        wgs.cB_m_task.currentIndexChanged.connect(self.on_combobox_changed)
        

    #Func control app
    def start_clock(self):
        if self.clock_onoff == False:
            self.clock_onoff = True
            self.countdown.start_timer()
            wgs.cB_m_task.setEnabled(not self.clock_onoff)
        elif self.clock_onoff == True:
            self.clock_onoff = False
            self.countdown.stop_timer()
            wgs.cB_m_task.setEnabled(not self.clock_onoff)
    
    def next_clock(self):
        self.countdown.next_timer()
        self.clock_onoff = False
        wgs.cB_m_task.setEnabled(True)
        self.mtime = self.countdown.mtime
        wgs.lb_m_time.setText(f"{self.mtime}:00")
        try: Pwgs.lb_time.setText(f"{self.mtime}:00")
        except: pass
        try: Fwgs.lb_time.setText(f"{self.mtime}:00")
        except: pass

    def onoff_audio(self):
        if self.music_onoff:
            print("start")
            self.media_player.play()
            self.music_onoff = False
        elif self.music_onoff == False:
            print("stop")
            self.media_player.stop()
            self.music_onoff = True
    
    def on_combobox_changed(self):
        try: selected_option = Fwgs.cB_task.currentText()
        except: selected_option = wgs.cB_m_task.currentText()
        try:
            Pwgs.lb_task.setText(selected_option)
            wgs.cB_m_task.setCurrentText(selected_option)
        except: pass
    
    def start_dialog(self):
        self.diaLog = DialogFunc()
        Pwgs.lb_time.setText(f"{self.mtime}:00")

    def start_fs(self):
        self.fs = fullScreenFunc()
        Fwgs.cB_task.currentIndexChanged.connect(self.on_combobox_changed)
        Fwgs.lb_time.setText(f"{self.countdown.mtime}:00")
        Fwgs.btn_startstop.clicked.connect(self.start_clock)
        Fwgs.btn_next.clicked.connect(self.next_clock)
        Fwgs.btn_audio.clicked.connect(self.onoff_audio)
        Fwgs.cB_task.setCurrentText(wgs.cB_m_task.currentText())
        Fwgs.btn_exit.clicked.connect(lambda: Fwgs.close())
        Fwgs.bottomQuote.setText(self.qoutes)


class DialogFunc:
    def __init__(self):
        global Pwgs
        Pwgs = Ui_Dialog()
        Pwgs.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        Pwgs.lb_task.setText(wgs.cB_m_task.currentText())
        Pwgs.show()


class fullScreenFunc(StudiousFS):
    def __init__(self):
        super().__init__()
        global Fwgs
        Fwgs = self
        Fwgs.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        Fwgs.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        Fwgs.show()

    def close_fs(self):
        Fwgs.close()

    def focusOutEvent(self, event):
        # Prevent the window from losing focus
        self.activateWindow()

        return super().event(event)

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
        try: self.timer.disconnect()
        except: pass

    def update_countdown(self):
        self.time_left -= 1

        if self.time_left >= 0:
            # Format the remaining time as MM:SS
            self.minutes, self.seconds = divmod(self.time_left, 60)
            wgs.lb_m_time.setText(f"{self.minutes:02}:{self.seconds:02}")
            wgs.lb_m_time.setStyleSheet('color: rgb(251, 238, 172)')
            try:    
                Pwgs.lb_time.setText(f"{self.minutes:02}:{self.seconds:02}")
                Pwgs.lb_m_time.setStyleSheet('color: rgb(251, 238, 172)')
            except: pass
            try:    
                Fwgs.lb_time.setText(f"{self.minutes:02}:{self.seconds:02}")
                Fwgs.lb_time.setStyleSheet('color: rgb(251, 238, 172)')
            except: pass
        else:
            self.timer.stop()
            self.next_timer()

    def next_timer(self):
        try: self.timer.disconnect()
        except: pass
        if self.work_or_rest == True:
            self.work_or_rest = False
            self.mtime = self.rtime
            print("False")
        else:
            self.work_or_rest = True
            self.mtime = self.wtime
            print("True")
        self.time_left = self.mtime*60
