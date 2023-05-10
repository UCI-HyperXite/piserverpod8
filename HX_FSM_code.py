from app import sio, get_sid_save
from enum import Enum 
import uvicorn
import asyncio
import time

async def run_loop() -> None:
    current_state = 1
    while True:
        #-------???----------------EPR_COM_CHECK
        #-------???----------------BMS_COM_CHECK
        #-------???----------------GUI_CONNECTED
        try:
            if current_state == 1:
                #CONTACTOR OFF----------------
                #BRAKES NOT ACTUATED----------
                state1_message = "Brakes are not actuated \nContactor turned off"
                print("BOOOOOO Brakes are not actuated \n Contactor turned off")
                sid_save_value = get_sid_save()
                sio.emit('sum_result', state1_message, broadcast=True)
                print(sid_save_value)       
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            # currently not working :(
            break
        


config = uvicorn.Config(
    "app:app",
    port=8000,
    log_level="info",
    access_log=True,
    use_colors=True,
    reload=True,
)
server = uvicorn.Server(config)


async def main() -> None:
    """Run Uvicorn server and FSM concurrently"""
    await asyncio.gather(server.serve(), run_loop(), return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())