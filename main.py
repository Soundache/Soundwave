from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import uic
import sys
from mido import Message, MidiFile, MidiTrack
import pygame as pyg
from pygame import midi

# mid = MidiFile()
# track = MidiTrack()
# mid.tracks.append(track)

# track.append(Message('program_change', program=12, time=0))
# track.append(Message('note_on', note=64, velocity=64, time=32))
# track.append(Message('note_off', note=64, velocity=127, time=32))
# mid.save('song.mid')

pyg.init()
pyg.mixer.music.load('song1.mid')
pyg.mixer.music.play()

midi.init()
out = midi.Output()
out.set_instrument(40)
out.note_on(21)
out.note_off(21)

app = QApplication(sys.argv)


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('prototype1.ui', self)
        self.show()


window = UI()
window.show()
sys.exit(app.exec_())
