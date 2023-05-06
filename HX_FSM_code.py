<<<<<<< HEAD
from app import *
from enum import Enum 
import uvicorn

import threading

def run_loop():
    global current_state
    while True:
        #-------???----------------EPR_COM_CHECK
        #-------???----------------BMS_COM_CHECK
        #-------???----------------GUI_CONNECTED

        if current_state == 1:
            #CONTACTOR OFF----------------
            #BRAKES NOT ACTUATED----------
            state1_message = "Brakes are not actuated \n Contactor turned off"
            print("BOOOOOO Brakes are not actuated \n Contactor turned off")
            state1(state1_message)

def main():
    # start the loop in a separate thread
    loop_thread = threading.Thread(target=run_loop)
    loop_thread.start()

    # start the web server in the main thread
    uvicorn.run(
        "app:app",
        port=8000,
        log_level="info",
        access_log=False,
        use_colors=True,
        reload=True,
    )
           
if __name__ == "__main__":
    
    
    main()
    
           
