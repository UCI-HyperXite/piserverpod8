import limmy
import time


serial_port = '/dev/serial/by-id/usb-STMicroelectronics_ChibiOS_RT_Virtual_COM_Port_301-if00'
motor = limmy.VESC(serial_port=serial_port)

def motor_start():
    motor.engage(30, 30)
    time.sleep(5)

def motor_stop(): 
    motor.halt(0)
    time.sleep(1)
    motor.stop_heartbeat() #?? maybe


def get_motor_data():
    v_in = motor.get_v_in() # Input voltage to the Flipsky VESC, should match Orion BMS 2 Pack Voltage, roughly 44~48V
    motor_current = motor.get_motor_current() # Current being drawn by the motor, informs force output
    incoming_current = motor.get_incoming_current() # Current being drawn from the battery, should match Orion BMS 2 Pack Current
    return v_in, motor_current, incoming_current




'''
High Voltage System Electrical Diagram:

Note that each 44V Battery should be equppied with a 50 Amp fuse, High Current Switch
and unique contactor. The contactors should be controlled by the Raspberry Pi such that the
High Voltage system is always OFF when the Raspberry Pi is not running.

The Flipsky VESC's and Orion BMS 2 are connected to the Raspberry Pi via USB Serial.

In the future, both the VESC and BMS should be connected to the Raspberry Pi via CAN Bus. (TODO HX9)

Remember to always wear appropriate PPE when working with High Voltage systems,
and to always work with a partner. For any questions, contact Adrian or Saketh.

 ┌───────────────┐         ┌─────────────────┐
 │               │         │                 │
 │ 44V Battery 1 ├────────►│  Flipsky VESC 1 ├──┐
 │               │         │                 │  │
 └───────┬───────┘         └─────────────────┘  │ ┌────────────┐
         │                                      └►│LIM L       │
         │     ┌──────────────┐                   ├────────────┤
         │     │              │         ┌─────────┴────────────┴─────────────┐
         ├────►│ Orion BMS 2  │         │ I-Beam Rotor                       │
         │     │              │         └─────────┬────────────┬─────────────┘
         │     └──────────────┘                   ├────────────┤
         │                                      ┌►│LIM R       │
 ┌───────┴───────┐         ┌─────────────────┐  │ └────────────┘
 │               │         │                 │  │
 │ 44V Battery 2 ├────────►│  Flipsky VESC 2 ├──┘
 │               │         │                 │
 └───────────────┘         └─────────────────┘
 '''