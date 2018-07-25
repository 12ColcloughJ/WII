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
    winsound.Beep(659, 910) #E5
    winsound.Beep(622, 300) #D#5
    winsound.Beep(587, 175) #D5
    time.sleep(1)
    winsound.Beep(415, 450) #G#4
    winsound.Beep(554, 390) #C#5
    winsound.Beep(370, 450) #F#4
    winsound.Beep(554, 590) #C#5
    winsound.Beep(415, 420) #G#4
    winsound.Beep(554, 460) #C#5
    winsound.Beep(392, 320) #G4
    winsound.Beep(370, 340) #F#4
    time.sleep(0.05)
    winsound.Beep(330, 800)
    for i in range(3):
        winsound.Beep(294, 300) #C#4
    time.sleep(0.6)
    for i in range(3):
        winsound.Beep(294, 300) #C#4
    time.sleep(1)
    winsound.Beep(330, 650)
    winsound.Beep(311, 550)
    winsound.Beep(294, 450)
    time.sleep(0.3)
    #winsound.Beep(340, 350)
    


while True:
    wii()
    
