# run_loop.py
from app import sio
from utils import get_sid_save
import asyncio

async def run_loop() -> None:
    current_state = 1
    while True:
        try:
            if current_state == 1:
                state1_message = "Brakes are not actuated \nContactor turned off"
                print("BOOOOOO Brakes are not actuated \n Contactor turned off")
                sid_save_value = get_sid_save()
                await sio.emit('sum_result', state1_message, to=sid_save_value)
                print(sid_save_value)       
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            break
