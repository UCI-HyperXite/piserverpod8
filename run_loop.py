# run_loop.py
from app import sio
from utils import get_sid_save, get_break_state, get_current_state, set_current_state
import asyncio
from basic_braking_rpi import start, stop
from current import vplus, vminus, shunt_current
from bms import read_bms
from wheel_encoder import calc
from contactor import contactor_start, contactor_stop
from pneumatics import pressureValue300, pressureMax5000
BMS_value = 0.0
PT1_value = 0.0
PT2_value = 0.0
PT3_value = 0.0
GUI_message = 0.0
brakes_signalled = 0.0
power_check = 0.0


async def send_data():
    sid_save_value  = get_sid_save()
    bms = read_bms()
    BMS_value = bms["highest_cell_voltage"]
    await sio.emit("vplus", vplus, to=sid_save_value)
    await sio.emit("speed", calc, to=sid_save_value)
    await sio.emit("vminus", vminus, to=sid_save_value)
    await sio.emit("shunt", shunt_current, to=sid_save_value)
    await sio.emit("bmsHigh", BMS_value, to=sid_save_value)
    await sio.emit("pressure300", pressureValue300, to=sid_save_value)
    await sio.emit("pressure5000", pressureMax5000, to=sid_save_value)
    await sio.emit("BMSCells", bms["cells"], to=sid_save_value)

async def run_loop() -> None:
    while True:
        try:
            if (get_current_state() == 1):
                contactor_start()
                bms = read_bms()
                BMS_value = bms["highest_cell_voltage"]
                print("CURRENT STATE 1", get_current_state())
                state1_message = "Brakes are not actuated \n Contactor turned off"
                print("Brakes are not actuated \n Contactor turned off")
                sid_save_value  = get_sid_save()
                await sio.emit("state1", state1_message, to=sid_save_value)
                PT1_value = pressureMax5000
                PT2_value = pressureValue300
                send_data()
                if(PT1_value == 1):
                    print("PT 1 Checked!")
                else:
                    print("PT 1  Failed!")

                if(PT2_value == 1):
                    print("PT 2 Checked!")
                else:
                    print("PT 2  Failed!")
                if(BMS_value < 3.4):
                    print("Error in BMS values!")
                    #disconnect battery from motors
                else:
                    print("Log all cell values")
                start()

                #turn on contactor to begin to check high voltage (contactor, two inverters)
                #given code to check inverters

                #GUI Indicates that we want to run the pod then:
                if (GUI_message == 2):
                    set_current_state(2)
                    await sio.emit("heard_message", 'heard!', to=sid_save_value)
                else:
                    print("GUI has not indicated start still!")
            #STARTING----------------------------------------------------------------
            if(get_current_state() == 2):
                print("CURRENT STATE 2", get_current_state())

                #SIGNAL THE BRAKES
                start()
                #SEND DATA to GUI 
                send_data()
                if(brakes_signalled == 1):
                    print("t\The brakes have been signalled successfully")
                else:
                    print("The brakes were not signalled successfully")

            #RUNNING--------------------------------------------------------------------
            if(get_current_state() == 3):
                
                send_data()
                if (GUI_message == 4):
                    print("GUI requested STOP")
                    set_current_state(4)

                if(power_check == 1):
                    print("Power check successful! ")
                else:
                    print("Power check failed")
                set_current_state(4)
                
            #STOPPING-------------------------------------------------------------------------
            if(get_current_state() == 4):
                #STOP
                contactor_stop()
                stop()
                send_data()
                print("Braking")
            if(get_current_state() == 5):
                if (get_break_state() == 0):
                    start()
                else:
                    stop()
                send_data()
                set_current_state(1)
                print("Brake Switch")
                
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            break
