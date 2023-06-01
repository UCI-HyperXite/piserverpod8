# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Sample code and test for adafruit_ina219"""

import time
import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219


i2c_bus = board.I2C()  # uses board.SCL and board.SDA
# i2c_bus = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

ina219 = INA219(i2c_bus, 0x41)
'''
print("ina219 test")

# display some of the advanced field (just to test)
print("Config register:")
print("  bus_voltage_range:    0x%1X" % ina219.bus_voltage_range)
print("  gain:                 0x%1X" % ina219.gain)
print("  bus_adc_resolution:   0x%1X" % ina219.bus_adc_resolution)
print("  shunt_adc_resolution: 0x%1X" % ina219.shunt_adc_resolution)
print("  mode:                 0x%1X" % ina219.mode)
print("")
'''

# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_128S
ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_128S
# optional : change voltage range to 16V
ina219.bus_voltage_range = BusVoltageRange.RANGE_16V
ina219.set_calibration_16V_400mA()

# measure and display loop
def pt300():
    bus_voltage = ina219.bus_voltage  # voltage on V- (load side)
    shunt_voltage = ina219.shunt_voltage  # voltage between V+ and V- across the shunt
    current = ina219.current  # current in mA
    print("low pressure current", current)
    power = ina219.power  # power in watts
    pressure = (ina219.current/1000-0.005)*(300-14.7)/(0.020-0.005)+14.7
    print("300 PT CURRENT: ", current)
    # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
    print("Voltage (VIN+) : {:6.3f}   V".format(bus_voltage + shunt_voltage))
    print("Voltage (VIN-) : {:6.3f}   V".format(bus_voltage))
    print("Shunt Voltage  : {:8.5f} V".format(shunt_voltage))
    print("Shunt Current  : {:7.4f}  A".format(current / 1000))
    print("Pressure (300 PT): {:7.4f}  PSI".format(pressure))
    print("Power Calc.    : {:8.5f} W".format(bus_voltage * (current / 1000)))
    print("Power Register : {:6.3f}   W".format(power))
    print("")
    return pressure
    # Check internal calculations haven't overflowed (doesn't detect ADC overflows)
    if ina219.overflow:
        '''
        print("Internal Math Overflow Detected!")
        print("")
        '''

if __name__ == "__main__":
    while True:
        pt300()
        time.sleep(0.1)