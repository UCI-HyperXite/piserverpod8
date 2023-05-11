import spidev
import RPi.GPIO as GPIO

sensorPin5000 = 17  # SPI channel 0 a1
sensorPin300 = 27  # SPI channel 1 a0
voltageOutputMin = 0.88  # measured @ 14.7 psi
voltageOutputMax = 4.4  # 20*10^-3*220 (20 mA to A)*(220 ohm)
pressureMax5000 = 5000
pressureMax300 = 300
pressureMin = 0
message = ""
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI channel 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)  # Pin 17 as input for channel 1

while True:
    # Read the value from the sensors
    sensorValue5000 = spi.xfer2([1, (8 + sensorPin5000) << 4, 0])
    sensorValue300 = GPIO.input(17)

    scaledSensorValue5000 = (sensorValue5000[1] * 5) / 1023
    scaledSensorValue300 = (sensorValue300 * 5) / 1023

    pressureValue5000 = ((scaledSensorValue5000 - voltageOutputMin) * (pressureMax5000 - pressureMin)) / (
            voltageOutputMax - voltageOutputMin)
    pressureValue300 = ((scaledSensorValue300 - voltageOutputMin) * (pressureMax300 - pressureMin)) / (
            voltageOutputMax - voltageOutputMin)

    print("5000 PT Value: ", pressureValue5000, "        300 PT Value: ", pressureValue300)

    # Delay for 100 milliseconds
    time.sleep(0.1)
