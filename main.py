from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys
from mido import Message, MidiFile, MidiTrack
import time
from pygame import midi

midi.init()
out = midi.Output(midi.get_default_output_id(), 0)


def play(instrument=0, note=72, duration=0.2):
    out.set_instrument(instrument)
    out.note_on(note, 127)
    time.sleep(duration)
    out.note_off(note, 127)


app = QApplication(sys.argv)


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('prototype1.ui', self)
        self.show()
        self.instrument = 0

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_C:
            if event.modifiers() == Qt.Key.Key_Shift:
                play(self.instrument, 75)
            else:
                play(self.instrument, 74)
        if event.key() == Qt.Key.Key_D:
            play(self.instrument, 76)
        if event.key() == Qt.Key.Key_E:
            play(self.instrument, 78)
        if event.key() == Qt.Key.Key_F:
            play(self.instrument, 79)
        if event.key() == Qt.Key.Key_G:
            play(self.instrument, 81)
        if event.key() == Qt.Key.Key_A:
            play(self.instrument, 83)
        if event.key() == Qt.Key.Key_B:
            play(self.instrument, 85)

        # if event.key() == Qt.Key.Key_c1:
        #     play(self.instrument, 86)


window = UI()
window.show()
sys.exit(app.exec_())
