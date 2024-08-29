from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
from mido import Message, MidiFile, MidiTrack
import time
import asyncio
from pygame import midi

app = QApplication(sys.argv)
k = Qt.Key

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        #uic.loadUi('prototype1.ui', self)
        self.setupUi(self)
        self.show()
        self.piano()
        midi.init()
        self.out = midi.Output(midi.get_default_output_id(), 0)
        self.out.set_instrument(self.instrument)
        self.tasks = []

    def drums(self):
        self.channel = 9
        self.keys = {
            k.Key_C: 35,
            k.Key_D: 46,
            k.Key_E: 36,
            k.Key_F: 50,
            k.Key_G: 44,
            k.Key_A: 64,
            k.Key_B: 59
        }
        self.instrument = 116

    def piano(self):
        self.channel = 0
        self.instrument = 0
        self.keys = {
            k.Key_C: 74,
            k.Key_D: 76,
            k.Key_E: 78,
            k.Key_F: 79,
            k.Key_G: 81,
            k.Key_A: 83,
            k.Key_B: 85,
            k.Key_S: 86,
            k.Key_R: 88
        }

    def guitar(self):
        self.channel = 0
        self.instrument = 28
        self.keys = {
            k.Key_C: 74,
            k.Key_D: 76,
            k.Key_E: 78,
            k.Key_F: 79,
            k.Key_G: 81,
            k.Key_A: 83,
            k.Key_B: 85,
            k.Key_S: 86,
            k.Key_R: 88
        }

    async def play(self, instrument=0, note=72, duration=0.2):
        self.out.set_instrument(instrument)
        self.out.note_on(note, 127, self.channel)
        await asyncio.sleep(duration)
        self.out.note_off(note, 127, self.channel)

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
            elif event.modifiers() == m.NoModifier:
                note -= (87-74)
            task = asyncio.run(self.play(self.instrument, note))
            self.tasks.append(task)

    def setupUi(self, MainWindow):
        # -*- coding: utf-8 -*-

        ################################################################################
        ## Form generated from reading UI file 'prototype1LaaJJv.ui'
        ##
        ## Created by: Qt User Interface Compiler version 5.15.2
        ##
        ## WARNING! All changes made in this file will be lost when recompiling UI file!
        ################################################################################
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(892, 817)
        MainWindow.setStyleSheet(u"/*background: url(bg.jpg);*/\n"
        "background: blue;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 93, 991, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(160, 220, 101, 101))
        self.pushButton_17.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-image: url(piano.jpg) no-repeat center center fixed;\n")

        self.pushButton_17.clicked.connect(self.piano)

        self.pushButton_18 = QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(160, 440, 101, 101))
        self.pushButton_18.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color : white;\n"
"border-color: white;"
"border-image: url(guitar.jfif) no-repeat center center fixed;\n")

        self.pushButton_18.clicked.connect(self.guitar)

        self.pushButton_19 = QPushButton(self.centralwidget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(160, 330, 101, 101))
        self.pushButton_19.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-image: url(drums.jpg) no-repeat center center fixed;\n")

        self.pushButton_19.clicked.connect(self.drums)

        self.pushButton_20 = QPushButton(self.centralwidget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(270, 440, 101, 101))
        self.pushButton_20.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color : white;")
        self.pushButton_21 = QPushButton(self.centralwidget)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(490, 220, 101, 101))
        self.pushButton_21.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color : white;")
        self.pushButton_22 = QPushButton(self.centralwidget)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(380, 220, 101, 101))
        self.pushButton_22.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color : white;")
        self.pushButton_23 = QPushButton(self.centralwidget)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(270, 220, 101, 101))
        self.pushButton_23.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background: rgb(0, 0, 0);")
        self.pushButton_24 = QPushButton(self.centralwidget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(380, 330, 101, 101))
        self.pushButton_24.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color : white;")
        self.pushButton_25 = QPushButton(self.centralwidget)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(490, 330, 101, 101))
        self.pushButton_25.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color : white;\n"
"border-color: rgb(255, 255, 255);\n"
"border:10px;")
        self.pushButton_26 = QPushButton(self.centralwidget)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(490, 440, 101, 101))
        self.pushButton_26.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color : white;")
        self.pushButton_27 = QPushButton(self.centralwidget)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(380, 440, 101, 101))
        self.pushButton_27.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color : white;")
        self.pushButton_28 = QPushButton(self.centralwidget)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(600, 330, 101, 101))
        self.pushButton_28.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color : white;")
        self.pushButton_29 = QPushButton(self.centralwidget)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(600, 440, 101, 101))
        self.pushButton_29.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color : white;")
        self.pushButton_30 = QPushButton(self.centralwidget)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(600, 220, 101, 101))
        self.pushButton_30.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color : white;")
        self.pushButton_31 = QPushButton(self.centralwidget)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(270, 330, 101, 101))
        self.pushButton_31.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color : white;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Soundwave - Feel the Wave", u"Soundwave - Feel the Wave", None))
        self.pushButton_17.setText("")
        self.pushButton_18.setText("")
        self.pushButton_19.setText("")
        self.pushButton_20.setText("")
        self.pushButton_21.setText("")
        self.pushButton_22.setText("")
        self.pushButton_23.setText("")
        self.pushButton_24.setText("")
        self.pushButton_25.setText("")
        self.pushButton_26.setText("")
        self.pushButton_27.setText("")
        self.pushButton_28.setText("")
        self.pushButton_29.setText("")
        self.pushButton_30.setText("")
        self.pushButton_31.setText("")
    # retranslateUi




window = UI()
window.show()
sys.exit(app.exec_())
