# pyuic6 -o mainUI.py mainUI.ui
# pyqt6rc -o asserts.py asserts.qrc
from . mainUI import Ui_Studious
from . conUI import *
from . pinDialog import Ui_Dialog
from . fsUI import StudiousFS
from . breathUI import BreathingCircleAnimation # Press button to breath
from . weekDialog import Week_Dialog # Edit task in week
from . chatmessage import ChatLogModel, DrawSpeechBubbleDelegate
from . colorFunc import comboCompanies