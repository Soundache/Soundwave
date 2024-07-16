from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import uic
import sys
from mido import Message, MidiFile, MidiTrack
import pygame as pyg

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=64, velocity=64, time=32))
track.append(Message('note_off', note=64, velocity=127, time=32))
track.append(Message('note_on', note=65, velocity=64, time=32))
track.append(Message('note_off', note=65, velocity=127, time=32))
track.append(Message('note_on', note=60, velocity=64, time=32))
track.append(Message('note_off', note=60, velocity=127, time=32))

mid.save('song.mid')
pyg.mixer.init()
pyg.mixer.music.load('song.mid')
pyg.mixer.music.play()

app = QApplication(sys.argv)


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('prototype1.ui', self)
        self.show()


window = UI()
window.show()
sys.exit(app.exec_())
