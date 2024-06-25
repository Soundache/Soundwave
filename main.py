from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5 import uic
import sys

app = QApplication(sys.argv)

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('prototype1.ui', self)
        self.show()


window = UI()
window.show()
sys.exit(app.exec_())

