bms_values = 0.0
PT1_value = 0.0
PT2_value = 0.0
PT3_value = 0.0
GUI_message = 0.0
brakes_signalled = 0.0
power_check = 0.0
    while(True):
        #LOADING----------------------------------------------------------------  
        if (current_state == 1):
            state1_message = "Brakes are not actuated \n Contactor turned off"
            print("Brakes are not actuated \n Contactor turned off")
            state1(state1_message)
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
                current_state = 2
                await sio.emit("heard_message", 'heard!', to=sid_save_value)
            else:
                print("GUI has not indicated start still!")
               
        #STARTING----------------------------------------------------------------
        if(current_state == 2):
            #SIGNAL THE BRAKES
            #SEND DATA to GUI 
            await sio.emit("PT1_value", PT1_value, to=sid_save_value)
            await sio.emit("PT2_value", PT2_value, to=sid_save_value)
            await sio.emit("BMS_value", BMS_value, to=sid_save_value)
            if(brakes_signalled == 1):
                print("t\The brakes have been signalled successfully")
            else:
                print("The brakes were not signalled successfully")

        #RUNNING--------------------------------------------------------------------
        if(current_state == 3):
            await sio.emit("PT1_value", PT1_value, to=sid_save_value)
            await sio.emit("PT2_value", PT2_value, to=sid_save_value)
            await sio.emit("BMS_value", BMS_value, to=sid_save_value)
            if (GUI_message == 4):
                print("GUI requested STOP")
                current_state = 4

            if(power_check == 1):
                print("Power check successful! ")
            else:
                print("Power check failed")
            current_state = 4
            
        #STOPPING-------------------------------------------------------------------------
        if(current_state == 4):
            #STOP
