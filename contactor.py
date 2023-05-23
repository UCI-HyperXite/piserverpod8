import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.OUT)

#pts
#turning contactor on 
def contactor_start():
    gpio.output(20, gpio.HIGH)
    time.sleep(4)
     
#off
def contactor_stop():
        gpio.output(20, gpio.LOW)
        time.sleep(4)
        



