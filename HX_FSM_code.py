<<<<<<< HEAD
from app import *
from enum import Enum 
import uvicorn


class STATE(Enum):
    LOADING = 1
    STARTING = 2
    RUNNING = 3
    STOPPING = 4
    STOPPED = 5

STATE = Enum('STATE', ['LOADING', 'STARTING', 'RUNNING', 'STOPPING', 'STOPPED' ])

current_state = 1

bms_values = 0.0
PT1_value = 0.0
PT2_value = 0.0
PT3_value = 0.0
GUI_message = 0.0
brakes_signalled = 0.0
power_check = 0.0 

def main():
    uvicorn.run(
        "app:app",
        port=8000,
        log_level="info",
        access_log=False,
        use_colors=True,
        reload=True,
    )
    STATE = 1
    while(True):
        #-------???----------------EPR_COM_CHECK
        #-------???----------------BMS_COM_CHECK
        #-------???----------------GUI_CONNECTED

        if (current_state == 1):
            #CONTACTOR OFF----------------
            #BRAKES NOT ACTUATED----------
            state1_message = "Brakes are not actuated \n Contactor turned off"
            print("BOOOOOO Brakes are not actuated \n Contactor turned off")
            state1(state1_message)
       
           
if __name__ == "__main__":
    
    
    main()
    
           
