import socketio
from app import *
from enum import Enum 

class STATE(Enum):
    LOADING = 1
    STARTING = 2
    RUNNING = 3
    STOPPING = 4
    STOPPED = 5

STATE = enum('STATE', ['LOADING', 'STARTING', 'RUNNING', 'STOPPING', 'STOPPED' ])

current_state = STATE.LOADING 

sio = socketio.AsyncServer(async_mode = "asgi", cors_allowed_origins = "http://localhost:3000")

app = app = socketio.ASGIApp(sio)

bms_values = 0.0
PT1_value = 0.0
PT2_value = 0.0
PT3_value = 0.0
GUI_message = 0.0
brakes_signalled = 0.0
power_check = 0.0

async def connect(sid, environ):
    print(sid, 'connected')

async def disconnect(sid):
    print(sid, 'disconnect ')

async def bms_communcation(sid, data):
    bms_comm = data

async def bms_values(sid, data):
    bms_values = data

async def PT1_value(sid, data):
    PT1_value = data 

async def PT2_value(sid, data):
    PT2_value = data

async def PT3_value(sid, data):
    PT3_value = data

async def GUI(sid, data):
    GUI_message = data  

def main():
    STATE = 1
    while(True):
        #-------???----------------EPR_COM_CHECK
        #-------???----------------BMS_COM_CHECK
        #-------???----------------GUI_CONNECTED

        if (current_state == STATE.LOADING):
            #CONTACTOR OFF----------------
            #BRAKES NOT ACTUATED----------
            state1_message = "Brakes are not actuated \n Contactor turned off"
            print("Brakes are not actuated \n Contactor turned off")
            state1(state1_message)

        '''          
        if(STATE == 2):
            #PT_CHECK--------------------
            if(PT1_value == 1):
                print("PT 1 Checked!")
            else:
                print("PT 1  Failed!")
            #OTHER_SENSORS_CHECK
            #THIS CHECKS IF GUI IS INDICATING TO MOVE TO RUNNING STATE!
            #GUI START => RUNNING STATE--------------------------------
            if (GUI_message == 2):
                STATE = 3
            else:
                #REPORT_TO_GUI
                #REPORT_IN_TERMINAL
                print("GUI has not indicated start still!")
               
        if(STATE == 3):
            #SIGNAL THE BRAKES
            if(brakes_signalled == 1):
                print("t\The brakes have been signalled successfully")
            else:
                print("The brakes were not signalled successfully")
            #CHECK EPR, BMS, PT, OTHER SENSORS
                #values checks + report this time from GUI + log
            #----------????????----------------------------------------CHECK AND DISPLAY WHEEL ENCODER -> SEND TO GUI
            #BMS THRESHOLD CHECK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #less than 3.4 -> ERROR -> disconnect battery from motors
            # log all cell values.

            #This GUI check is for seeing if GUI wants to STOP
            if (GUI_message == 4):
                print("GUI requested STOP")
                #SIGNAL BRAKES
                if(brakes == 1):
                    print("brakes are signalled")
                STATE = 4
        if(STATE == 4):
            #POWER CHECK
            if(power_check == 1):
                print("Power check successful! ")
            else:
                print("Power check failed")
            #INTERMEDIATE BRAKE STAGE
            STATE = 5

        if(STATE == 5):
            #GUI REPORTing
            print("f")
            #GO BACK TO STAGE U WANT
    '''
 
           
       
           
if __name__ == "__main__":
    main()         
