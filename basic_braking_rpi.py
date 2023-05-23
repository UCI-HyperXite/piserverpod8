import RPi.GPIO as GPIO
import time
from pneumatics import pressureValue300 as pt
from utils import set_break_state, get_break_state
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)

#pts
#turning brakes on 
def start():
        set_break_state(1)
        if pt < 25:
                print("no pressure")
        elif pt < 105:
                stop()
        elif pt <= 145:
    
                gpio.output(23, gpio.HIGH)
        else:
                print("too much pressure")
        time.sleep(4)
     
#turning brakes off
def stop():
        set_break_state(0)
        gpio.output(23, gpio.LOW)
        time.sleep(4)
        



