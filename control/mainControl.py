from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtMultimedia import *
from main import *
from random import choice
from view import *

class StudiousFunc:
    def __init__(self, widgets):
        super().__init__()
        global wgs
        wgs = widgets

        #random qoutes and print in app
        list_quotes = ["Chúng ta có thể gặp nhiều thất bại nhưng chúng ta không được bị đánh bại – Maya Angelou",
                       "Tất cả những sự khó khăn thường là để chuẩn bị cho những người bình thường một số phận phi thường – C.S. Lewis",
                       "Mọi người sẽ quên những gì bạn nói, quên những gì bạn đã làm, nhưng họ sẽ không bao giờ quên cảm xúc mà bạn mang lại cho họ – Maya Angelou."]
        wgs.lb_m_quote.setText(f"{choice(list_quotes)}")

        #connect start/stop button with clock
        wgs.btn_m_startstop.clicked.connect(self.start_clock)
        self.countdown = countdown()
        self.clock_onoff = False

        #Put clock to next session
        wgs.btn_m_next.clicked.connect(self.next_clock)

        #Turn on/off music in app
        wgs.btn_m_audio.clicked.connect(self.onoff_audio)
        self.media_content = QUrl.fromLocalFile('.\\assert\\music.mp3')
        self.music_onoff = True
        self.media_player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.media_player.setAudioOutput(self.audio)
        self.media_player.setSource(self.media_content)
        self.onoff_audio()

        #Turn on pinDialog
        wgs.btn_m_pin.clicked.connect(DialogFunc)
        

    def start_clock(self):
        if self.clock_onoff == False:
            self.clock_onoff = True
            self.countdown.start_timer()
        elif self.clock_onoff == True:
            self.clock_onoff = False
            self.countdown.stop_timer()
    
    def next_clock(self):
        self.countdown = None
        self.countdown = countdown()

    def onoff_audio(self):
        if self.music_onoff:
            print("start")
            self.media_player.play()
            self.music_onoff = False
        elif self.music_onoff == False:
            print("stop")
            self.media_player.stop()
            self.music_onoff = True


class DialogFunc:
    def __init__(self):
        global Pwgs
        Pwgs = Ui_Dialog()
        Pwgs.show()
class countdown:
    def __init__(self):
        self.mtime = 25
        wgs.lb_m_time.setText(f"{self.mtime}:00")
        self.start_time = self.mtime*60
        self.time_left = self.start_time
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
            minutes, seconds = divmod(self.time_left, 60)
            wgs.lb_m_time.setText(f"{minutes:02}:{seconds:02}")
            try:    Pwgs.lb_time.setText(f"{minutes:02}:{seconds:02}")
            except: pass
        else:
            self.timer.stop()
            wgs.lb_m_time.setText("00:00")
            try:    Pwgs.lb_time.setText("00:00")
            except: pass
