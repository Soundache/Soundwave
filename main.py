from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys
from mido import Message, MidiFile, MidiTrack
import time
import asyncio
from pygame import midi

app = QApplication(sys.argv)


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('prototype1.ui', self)
        self.show()
        self.instrument = 0
        k = Qt.Key
        self.keys = {
            k.Key_C: 74,
            k.Key_D: 76,
            k.Key_E: 78,
            k.Key_F: 79,
            k.Key_G: 81,
            k.Key_A: 83,
            k.Key_B: 85
        }
        midi.init()
        self.out = midi.Output(midi.get_default_output_id(), 0)
        self.out.set_instrument(self.instrument)
        self.tasks = []

    async def play(self, instrument=0, note=72, duration=0.2):
        self.out.set_instrument(instrument)
        self.out.note_on(note, 127)
        await asyncio.sleep(duration)
        self.out.note_off(note, 127)

    def keyPressEvent(self, event):
        m = Qt.KeyboardModifier
        if self.keys.get(event.key()):
            note = self.keys[event.key()]
            if event.modifiers() == m.AltModifier:
                note += 1
            elif event.modifiers() == m.ControlModifier:
                note -= 1
            if event.modifiers() == m.ShiftModifier:
                note += (87-74)
            task = asyncio.run(self.play(self.instrument, note))
            self.tasks.append(task)


window = UI()
window.show()
sys.exit(app.exec_())
