import winsound
import time


def rise(firstTime):
    winsound.Beep(370, firstTime) #F#4
    winsound.Beep(440, 275) #A4
    winsound.Beep(554, 500) #C#5
    winsound.Beep(440, 500) #A4
    winsound.Beep(370, 300) #F#4

def wii():
#    winsound.Beep(294, 500) #D4
    rise(500)
    for i in range(3):
        winsound.Beep(294, 250) #C#4
    time.sleep(1)
    winsound.Beep(277, 260) #C4
    winsound.Beep(294, 310) #C#4
    rise(250)
    winsound.Beep(659, 920) #E5
    winsound.Beep(622, 300) #D#5
    winsound.Beep(587, 175) #D5
##    time.sleep(1)
##    winsound.Beep(415, 380) #G#4
##    winsound.Beep(554, 590) #C#5
##    winsound.Beep(370, 330) #F#4
##    winsound.Beep(554, 590) #
    

    
    
    
wii()
