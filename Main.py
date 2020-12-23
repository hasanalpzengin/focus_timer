from PyQt5.QtWidgets import QApplication
from MainWindow import Window
from Controller import Controller
import sys

app = QApplication(sys.argv)
win = Window(app)
controller = Controller(win)

sys.exit(app.exec_())