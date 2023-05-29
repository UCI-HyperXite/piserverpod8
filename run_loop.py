# run_loop.py
from app import sio
from utils import get_sid_save, get_current_state, set_current_state, get_v, get_break_state
import asyncio
import RPi.GPIO as GPIO

# from pt_test import pt300
#from basic_braking_rpi import break_start, break_stop
#from current import vplus, vminus, shunt_current
#from podmotor import motor_start, motor_stop, get_motor_data
#from bms import read_bms
#from wheel_encoder import calc, distance
#from contactor import contactor_start, contactor_stop
#from pneumatics import pressureValue300, pressureMax5000
BMS_value = 0.0
PT_5000 = 0.0
PT_300 = 0.0
PT3_value = 0.0
GUI_message = 0.0
brakes_signalled = 0
power_check = 0.0
calc = 0


async def send_data():
    sid_save_value  = get_sid_save()
#     await sio.emit("pressure300", pt300(), to=sid_save_value)

    #bms = read_bms()
    #BMS_value = bms["highest_cell_voltage"]
    #await sio.emit("vplus", round(vplus, 7), to=sid_save_value)
    #await sio.emit("speed", round(calc, 2), to=sid_save_value)
    #await sio.emit("vminus", round(vminus, 7), to=sid_save_value)
    #await sio.emit("shunt", round(shunt_current, 7), to=sid_save_value)
    #await sio.emit("bmsHigh", round(BMS_value, 7), to=sid_save_value)
    #await sio.emit("pressure300", round(pressureValue300, 7), to=sid_save_value)
    #await sio.emit("pressure5000", round(pressureMax5000, 7), to=sid_save_value)
    #await sio.emit("BMSCells", bms["cells"], to=sid_save_value)
    #await sio.emit("Motor data", get_motor_data(), to=sid_save_value)
    #await sio.emit("Distance", distance, to=sid_save_value)

async def run_loop() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    while True:
        try:
            if (get_current_state() == 1):
                #contactor_start()
                #bms = read_bms()
                #BMS_value = bms["highest_cell_voltage"]
                print("CURRENT STATE 1", get_current_state())
                state1_message = "Brakes are not actuated \n Contactor turned off"
                print("Brakes are not actuated \n Contactor turned off")
                sid_save_value  = get_sid_save()
                await sio.emit("state1", state1_message, to=sid_save_value)
#                 await sio.emit("pressure300", pt300(), to=sid_save_value)

                #PT_5000 = pressureMax5000
                #PT_300 = pressureValue300
                #send_data()
                
                if(PT_5000 >= 2950 and PT_5000 <= 3500):
                    print("PT 5000 OK!")
                elif (PT_5000 < 0):
                    print("PT 5000 OUT OF RANGE")
                if(PT_300 >= 105 and PT_300 <= 145):
                    print("PT 300 Checked + in range!")
                else:
                    print("PT 300  OUT OF RANGE!")
                if(BMS_value < 3.4):
                    print("Error in BMS values!")#disconnect battery from motors
                else:
                    print("Log all cell values")
                if (calc < 0.5):
                    print("Wheel Encoder OK!")
                
                GPIO.output(26, GPIO.HIGH)
                #turn on contactor to begin to check high voltage (contactor, two inverters)
                #given code to check inverters

                #GUI Indicates that we want to run the pod then:
            #STARTING----------------------------------------------------------------
            if(get_current_state() == 2):
                print("CURRENT STATE 2", get_current_state())

                #SIGNAL THE BRAKES
                #motor_start()
                #SEND DATA to GUI 
                if(PT_5000 >= 2950 and PT_5000 <= 3500):
                    print("PT 5000 OK!")
                elif (PT_5000 < 0):
                    print("PT 5000 OUT OF RANGE")
                if(PT_300 >= 105 and PT_300 <= 145):
                    print("PT 300 Checked + in range!")
                else:
                    print("PT 300  OUT OF RANGE!")
                send_data()
                if(get_break_state() == 1):
                    print("t\The brakes have been signalled successfully!")
                else:
                    print("The brakes were NOT signalled successfully")
                set_current_state(3)

            #RUNNING--------------------------------------------------------------------
            if(get_current_state() == 3):
                #send_data()
                if(PT_5000 >= 2950 and PT_5000 <= 3500):
                    print("PT 5000 OK!")
                elif (PT_5000 < 0):
                    print("PT 5000 OUT OF RANGE")
                if(PT_300 >= 105 and PT_300 <= 145):
                    print("PT 300 Checked + in range!")
                else:
                    print("PT 300  OUT OF RANGE!")
                if(power_check == 1):
                    print("Power check successful! ")
                else:
                    print("Power check failed")
                
            #STOPPING-------------------------------------------------------------------------
            if(get_current_state() == 4):
                
                GPIO.output(26, GPIO.LOW) 
                #STOP
                #contactor_stop()
                #motor_stop()
                #break_stop()
                if(PT_5000 >= 2950 and PT_5000 <= 3500):
                    print("PT 5000 OK!")
                elif (PT_5000 < 0):
                    print("PT 5000 OUT OF RANGE")
                if(PT_300 >= 105 and PT_300 <= 145):
                    print("PT 300 Checked + in range!")
                else:
                    print("PT 300  OUT OF RANGE!")
                #send_data()
                print("Braking")
                set_current_state(1)
                
            #LOADING--------------switches breaks off/on out of fsm, returns to state 1-----
            if(get_current_state() == 5):
                print("enters loading")
                if(PT_5000 >= 2950 and PT_5000 <= 3500):
                    print("PT 5000 OK!")
                elif (PT_5000 < 0):
                    print("PT 5000 OUT OF RANGE")
                if(PT_300 >= 105 and PT_300 <= 145):
                    print("PT 300 Checked + in range!")
                else:
                    print("PT 300  OUT OF RANGE!")
                #if (get_break_state() == 0):
                    #break_start()
                #else:
                   # break_stop()
                send_data()
                set_current_state(1)
                print("Brake Switch")
                
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            break

