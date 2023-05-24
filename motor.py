import limmy
from limmy.protocol.interface import encode_request, encode, decode
from limmy.VESC.messages import VedderCmd, VedderGPD
import time

# serial port that VESC is connected to. Something like "COM3" for windows
serial_port = 'COM15'
motor = limmy.VESC(serial_port=serial_port)
print("Firmware: ", motor.get_firmware_version())

time.sleep(1)
motor.send_terminal_cmd('foc_openloop {current} {rpm}'.format(current=30, rpm=2700))

time.sleep(5)
#     # IMPORTANT: YOU MUST STOP THE HEARTBEAT IF IT IS RUNNING BEFORE IT GOES OUT OF SCOPE. Otherwise, it will not clean-up properly.
motor.stop_heartbeat()
