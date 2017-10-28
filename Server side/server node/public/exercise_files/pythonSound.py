import os
from datetime import datetime

DEBUG = False

def playASound(n):
    if DEBUG == True:
        print (n, end=" - ")
        print (daySounds[n])

    todaySound = "aplay " + sayDayDirectory + daySounds[n] + ".wav -R 1"
    os.system(todaySound)

sayDayDirectory = "/home/pi/exercise_files/dayOfWeekSounds/"

daySounds = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

todaysDate = datetime.now()
todaysDay = datetime.weekday(todaysDate)

playASound(todaysDay)

if DEBUG == True:
    print ("Other sounds are...")
    for n in range(0,7):
        playASound(n)
            
