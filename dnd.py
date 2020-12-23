# Author: Joseph Slater <joseph.slater@wright.edu>
# Copyright: This script has been placed in the public domain.
# Github: https://raw.githubusercontent.com/josephcslater/Do-Not-Disturb/master/dnd.py

import sys
import os
import subprocess
import time
import logging

def startDndForMac(endtime):
    os.environ['PATH'] = os.path.normpath(
        os.environ['PATH'] + ':/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:')

    a1 = subprocess.check_output(
        ['defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturb -boolean true'], shell=True)

    a = subprocess.check_output(['date -u +"%Y-%m-%d %H:%M:%S +0000"'], shell=True)
    b = a.decode('utf-8')

    a2 = subprocess.Popen(
        ['defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturbDate -date "' + b + '"'], shell=True)

    a3 = subprocess.Popen(['killall NotificationCenter'], shell=True)

    curhour = time.localtime().tm_hour
    curmin = time.localtime().tm_min

    numin = 0
    if str.find(endtime, ':') != -1:
        time = str.split(":")
        hour = float(time[0])
        min = float(time[1])
        numin = (hour - curhour) * 60 + (min - curmin)

    a5 = subprocess.Popen(['killall sleep -s;sleep ' + str(numin * 60) + ';defaults -currentHost write \
                    ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturb -boolean false; \
                    defaults -currentHost delete ~/Library/Preferences/ByHost/com.apple.notificationcenterui \
                    doNotDisturbDate; killall NotificationCenter'], shell=True)
    print('Sleeping for ' + str(numin) + ' min.')
