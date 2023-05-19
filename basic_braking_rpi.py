import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)


#turning brakes on 
def start():
        gpio.output(23, gpio.HIGH)
        time.sleep(4)
     
#turning brakes off
def stop():
        gpio.output(23, gpio.LOW)
        time.sleep(4)
        



