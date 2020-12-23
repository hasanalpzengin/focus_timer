import schedule
import time
import threading
import os
from dnd import startDndForMac
from Database import Database
from notifypy import Notify
from playsound import playsound

class Controller:
    scheduleRunning = True
    def __init__(self, window):
        window.scheduleButton.clicked.connect(self.scheduleFocus)
        window.startButton.clicked.connect(self.startFocus)
        window.deleteButton.clicked.connect(self.deleteSchedule)
        self.db = Database()
        self.window = window
        self.updateScheduleList()

        self.job = threading.Thread(target=self.checkForSchedule)
        self.job.start()

    def startFocus(self):
        self.showNotification("Focus time started")
        playsound("bell.wav")
        if os.name=="Darwin" :
            #snooze for 1 hour
            wakeupTime = str(time.localtime().tm_hour+1)+":"+str(time.localtime().tm_min)
            startDndForMac(wakeupTime);

    def stopFocus(self):
        self.showNotification("Focus time ended")
        playsound("bell.wav")
        
    def scheduleFocus(self):
        qtime = self.window.timeEdit.time()
        timeString = qtime.toString()
        self.createSchedule(timeString)
        
    def checkForSchedule(self):
        while self.scheduleRunning:
            schedule.run_pending()
            time.sleep(1)

    def deleteSchedule(self):
        if(self.window.listWidget.currentItem()):
            self.db.deleteTime(self.window.listWidget.currentItem().text())
            self.updateScheduleList()

    def createSchedule(self, time):
        self.db.addTime(time)
        self.updateScheduleList()
        self.showNotification("Focus time set to "+time)

    def updateScheduleList(self):
        times = self.db.listTime()  
        print(times)
        self.window.listWidget.clear()
        schedule.clear()
        for time in times:
            self.window.listWidget.addItem(time[0])
            schedule.every().day.at(time[0]).do(self.startFocus)
            cancelFocusTime = time[0].split(":")
            cancelFocusTime = str(int(cancelFocusTime[0])+1)+":"+cancelFocusTime[1]+":"+cancelFocusTime[2]
            schedule.every().day.at(time[0]).do(self.startFocus)
            schedule.every().day.at(cancelFocusTime).do(self.stopFocus)

    def showNotification(self, text):
        notification = Notify()
        notification.title = "Tiktak Focus Timer"
        notification.message = text
        notification.icon = "icon.png"
        notification.send()