import RPi.GPIO as GPIO
import time
from asyncgpio import Gpio
from utils import set_break_state, get_break_state
from asyncgpio import Gpio

brake_pin = 26 
brake_gpio = Gpio(brake_pin, direction=Gpio.OUTPUT)

def brake_start():
    brake_gpio.set(1) 
def brake_stop():
    brake_gpio.set(0)



