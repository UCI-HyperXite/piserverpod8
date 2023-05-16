# run_loop.py
from app import sio
from utils import get_sid_save
import asyncio
from pneumatics import message
#from pneumatics import message

async def run_loop() -> None:
    current_state = 1
    while True:
        try:
            if current_state == 1:
                state1_message = "Brakes are not actuated \nContactor turned off"
                print("BOOOOOO Brakes are not actuated \n Contactor turned off")
                sid_save_value = get_sid_save()
                await sio.emit('sum_result', message, to=sid_save_value)
                await sio.emit('PT1', 0.0, to=sid_save_value)
                print(0.0)
                print(sid_save_value)
                #print(message)       
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            break
