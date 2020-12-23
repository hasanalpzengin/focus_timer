import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from TrayIcon import TrayIcon

class Window(QWidget):
    def __init__(self, app, *args, **kwargs):
        self.font = QFont()
        self.font.setPointSize(20)
        self.font.setBold(True)

        QWidget.__init__(self, *args, **kwargs)
        self.label = QLabel("When you'll focus today ?", self)
        self.label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setFont(self.font)

        self.timeEditFont = QFont()
        self.timeEditFont.setPointSize(50)
        self.font.setBold(True)

        self.timeEdit = QTimeEdit()
        self.timeEdit.setFont(self.timeEditFont)
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.timeEdit.setObjectName("timeEdit")

        self.scheduleButton = QPushButton("Schedule Focus", self)
        self.scheduleButton.setFixedHeight(105)

        self.timeLayout = QHBoxLayout()
        self.timeLayout.setAlignment(Qt.AlignHCenter)
        self.timeLayout.addWidget(self.timeEdit, 2)
        self.timeLayout.addWidget(self.scheduleButton, 1)
        

        self.startButton = QPushButton("Start Focus Now", self)
        self.startButton.setFixedHeight(40)

        self.listWidget = QListWidget()

        self.deleteButton = QPushButton("Delete Schedule", self)
        self.deleteButton.setFixedHeight(40)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.addWidget(self.label)
        self.layout.addLayout(self.timeLayout)
        self.layout.addWidget(self.scheduleButton)
        self.layout.addWidget(self.startButton)
        self.layout.addWidget(self.listWidget)
        self.layout.addWidget(self.deleteButton)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setFixedSize(600, 400)

        self.trayIcon = TrayIcon(QIcon("icon.png"), app, self)
        self.trayIcon.show()

        self.setWindowTitle("Tiktak Focus")
        self.setLayout(self.layout)
        self.setWindowIcon(QIcon("icon.png"))
        self.show()


