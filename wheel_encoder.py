import time
import RPi.GPIO as GPIO

outputA = 4 #green/black/black
outputB = 2 #white/red/white,  brown/orange/blue
counter = 0
aState = 0
aLastState = 0
t1 = 0
t2 = 0
deltad = 0.0
deltat = 0.0
calc = 0.0

def setup():
    global aLastState, t1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(outputA, GPIO.IN)
    GPIO.setup(outputB, GPIO.IN)
    t1 = time.time() * 1000
    aLastState = GPIO.input(outputA)
    print("Setup complete.")

def loop():
    global aState, counter, t2, bLastState, deltat, t1, t2, aLastState
    aState = GPIO.input(outputA)

    deltad = 1.0 / 8.0

    if aState != aLastState:
        t2 = time.time() * 1000

        if GPIO.input(outputB) != aState:
            counter -= 1
        else:
            counter += 1
            print("counter: ", counter)
            deltat = t2 - t1
            calc = 1000 * deltad / deltat
            print("Instantaneous Speed:", calc)
            t1 = t2


    aLastState = aState

def main():
    setup()
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Program terminated.")

if __name__ == '__main__':
    main()

'''
//Code Explanation:
/*
First we need to define the pins to which our encoder is connected and define some variales needed for the prog. In the setup section we need to define two pins as inputs. start the serial communication for testing and prinitng
the results on the serial monitor, as well as read the initial value of the output A and put the values into the variable aLastState.

Then in the loop section we read the output A again but now we put the value into the aState variable. So we rotate the encoder and a pulse is generated, these 2 values will differ and the first "if" statement will become true. 
Right after that using the second "if" statement we determine the rotation direction. If the output B state differ from the output A state the counter will be increased by 1, else it will be decreased. At the end, after printing the
results on the serial monitor, we need to update the aLastState variable with aState variable.
*/

/*
// constants won't change. Used here to set a pin number:
const int ledPin =  LED_BUILTIN;// the number of the LED pin

// Variables will change:
int ledState = LOW;             // ledState used to set the LED

// Generally, you should use "unsigned long" for variables that hold time
// The value will quickly become too large for an int to store
unsigned long previousMillis = 0;        // will store last time LED was updated

// constants won't change:
const long interval = 1000;           // interval at which to blink (milliseconds)

void setup() {
  // set the digital pin as output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // here is where you'd put code that needs to be running all the time.

  // check to see if it's time to blink the LED; that is, if the difference
  // between the current time and last time you blinked the LED is bigger than
  // the interval at which you want to blink the LED.
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    // save the last time you blinked the LED
    previousMillis = currentMillis;

    // if the LED is off turn it on and vice-versa:
    if (ledState == LOW) {
      ledState = HIGH;
    } else {
      ledState = LOW;
    }

    // set the LED with the ledState of the variable:
    digitalWrite(ledPin, ledState);
  }}
*/
'''