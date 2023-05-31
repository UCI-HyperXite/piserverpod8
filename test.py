import RPi.GPIO as GPIO
import time
#from pneumatics import pressureValue300 as pt
#from utils import set_break_state, get_break_state
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)

def break_start():
        #set_break_state(1)
        GPIO.output(26, GPIO.HIGH)
        time.sleep(4)
    
        return 1
     
#turning brakes off
def break_stop():
        set_break_state(0)
        GPIO.output(26, GPIO.LOW)
        #time.sleep(4)
        return 0


def main():
    b = 0
    while True:
        if b == 0:
            b = break_start()
            print("hello")
#pts
#turning brakes on 

if __name__ == "__main__":
    main()






