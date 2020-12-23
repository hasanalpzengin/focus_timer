from PyQt5.QtWidgets import *
from Controller import Controller
import sys
import os
import signal

class TrayIcon(QSystemTrayIcon):
    def __init__(self, icon, app, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        menu = QMenu(parent)
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(self.quit)
        self.setContextMenu(menu)

    def quit(self):
        exit(0)
        os.kill(os.getpid(), signal.SIGUSR1)

