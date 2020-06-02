"""
countdown.py - Простой сценарий обратного отсчета.
"""

import time
import subprocess

timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft -= 1
subprocess.Popen(['start', 'alarm.wav'], shell=True)