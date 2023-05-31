from multiprocessing import Process, Value
import RPi.GPIO as GPIO
import time

outputA = 14
outputB = 15

#I do not know which of these are actually supposed to live inside of the process
counter = 0
aState = 0
aLastState = 0
t1 = 0
t2 = 0
deltad = 0.0
deltat = 0.0
calc = 0.0

def gpioSetup(): #uh I sure hope I'm allowed to call this in the other process???
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(outputA, GPIO.IN)
    GPIO.setup(outputB, GPIO.IN)

def readWheel(distanceValue: Value):
    #setup:
    gpioSetup()
    t1 = time.time()
    aLastState = GPIO.input(outputA)

    
    while True:
        aState = GPIO.input(outputA)

        deltad = 1.0 / 8.0

        if aState != aLastState:
            t2 = time.time() * 1000

            if GPIO.input(outputB) != aState:
                counter += 1
                deltat = t2 - t1
                calc = 1000 * deltad / deltat
                print(t1)
                print(t2)
                print("Instantaneous Speed:", calc)
                t1 = t2
            else:
                counter -= 1
        
        aLastState = aState
        distanceValue.value = counter

def main():
    counter = Value('i', 0.0)
    p = Process(target=readWheel, args=counter)
    p.start()
    try:
        while True:
            # time.sleep(0.5)
            print(counter.value)

    except KeyboardInterrupt:        
        print('"killing" child process')
        p.join()

if __name__  == '__main__':
    main()


