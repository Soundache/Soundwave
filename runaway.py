

# from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
# from PyQt5.QtCore import Qt
# from PyQt5 import uic
# import sys
# from mido import Message, MidiFile, MidiTrack
import time
from pygame import midi

midi.init()
out = midi.Output(midi.get_default_output_id(), 0)


def play(instrument=0, note=72, duration=1.3):
    out.set_instrument(instrument)
    out.note_on(note, 127)
    time.sleep(duration)
    out.note_off(note, 127)


play(46, 88)
play(46, 88)
play(46, 88)
play(46, 76)
play(46, 87)
play(46, 87)
play(46, 87)
play(46, 75)
play(46, 85)
play(46, 85)
play(46, 85)
play(46, 73)
play(46, 81)
play(46, 81)
play(46, 80)
play(46, 88)
