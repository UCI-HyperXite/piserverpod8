from multiprocessing import Process, Value
import RPi.GPIO as GPIO
import time

outputA = 14
outputB = 15

def gpioSetup():
    ''' Sets up GPIO for Wheel Encoder'''
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(outputA, GPIO.IN)
    GPIO.setup(outputB, GPIO.IN)

def readWheel(distanceValue: Value):
    #setup:
    gpioSetup()
    t1 = time.time() #* 1000 # Don't know why the 1000 is here? Should we just delete it everywhere?
    aLastState = GPIO.input(outputA)
    deltad = 1.0 / 8.0

    #loop    
    while True:
        aState = GPIO.input(outputA)
        if aState != aLastState:
            t2 = time.time() #* 1000

            if GPIO.input(outputB) != aState:
                counter += 1
                dir = 1
            else:
                counter -= 1
                dir = -1
            deltat = t2 - t1
            calc = deltad / deltat #1000 * deltad / deltat
            t1 = t2

        aLastState = aState
        distanceValue.value = counter

def main():
    counter = Value('i', 0)
    speed = Value('d', 0.0)
    p = Process(target=readWheel, args=(counter,speed))
    p.start()
    try:
        while True:
            # time.sleep(0.5)
            print(counter.value, speed.value)

    except Exception as e:        
        print('"killing" child process before termination')
        p.join()

if __name__  == '__main__':
    main()


