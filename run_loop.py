# run_loop.py
from app import sio
from utils import get_sid_save, get_current_state, set_current_state
import asyncio
from basic_braking_rpi import start, stop
from current import vplus, vminus, shunt_current
#from pneumatics import message
BMS_value = 0.0
PT1_value = 0.0
PT2_value = 0.0
PT3_value = 0.0
GUI_message = 0.0
brakes_signalled = 0.0
power_check = 0.0
async def run_loop() -> None:
    while True:
        try:
            if (get_current_state() == 1):
                print("CURRENT STATE2", get_current_state())
                state1_message = "Brakes are not actuated \n Contactor turned off"
                print("Brakes are not actuated \n Contactor turned off")
                sid_save_value  = get_sid_save()
                await sio.emit("state1", state1_message, to=sid_save_value)
                await sio.emit("vplus", vplus, to=sid_save_value)
                await sio.emit("vminus", vminus, to=sid_save_value)
                await sio.emit("shunt", shunt_current, to=sid_save_value)
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
                #GUI Indicates that we want to run the pod then:
                if (GUI_message == 2):
                    set_current_state(2)
                    await sio.emit("heard_message", 'heard!', to=sid_save_value)
                else:
                    print("GUI has not indicated start still!")
            #STARTING----------------------------------------------------------------
            if(get_current_state() == 2):
                print("CURRENT STATE2", get_current_state())

                #SIGNAL THE BRAKES
                start()
                #SEND DATA to GUI 
                await sio.emit("PT1_value", PT1_value, to=sid_save_value)
                await sio.emit("PT2_value", PT2_value, to=sid_save_value)
                await sio.emit("BMS_value", BMS_value, to=sid_save_value)
                if(brakes_signalled == 1):
                    print("t\The brakes have been signalled successfully")
                else:
                    print("The brakes were not signalled successfully")

            #RUNNING--------------------------------------------------------------------
            if(get_current_state() == 3):
                await sio.emit("PT1_value", PT1_value, to=sid_save_value)
                await sio.emit("PT2_value", PT2_value, to=sid_save_value)
                await sio.emit("BMS_value", BMS_value, to=sid_save_value)
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
                stop()
                print("Breaking")
                
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            break
