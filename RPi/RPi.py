import time
import pymodbus #trengs denne? kjør test. 
from pymodbusServerSyncUDP import modbusserver
# til pwm og kjøring av bil
import RPi.GPIO as GPIO
import os
import pigpio
import atexit

# --------------------------------------------------------------------------- #
# def run_test oppretter en loop når shallRun er true. shallRun settes 
# false ved keyboardinterrupt. akse verdiene for kjøring av bilen blir hentet 
# fra pymodbus UDP server (ved navn modbusserver.py). serverobj er tråd som 
# er gitt av modbusserver.py. 
# --------------------------------------------------------------------------- #
def run_test():
    shallRun = True
    try:
        while shallRun:   
            #henter modbus verdier
            axis_x = serverobj.getHoldingRegisterValue(0)
            axis_y = serverobj.getHoldingRegisterValue(1)
            axis_z = serverobj.getHoldingRegisterValue(2)

            # Under er oppretting av pwm signal til servo og esc. 
            pi=pigpio.pi()
            pi.set_servo_pulsewidth(13, axis_y)     #pulsbredde til ESC
            pi.set_servo_pulsewidth(18, axis_x)     #pulsbredde signal til servo motor

            #videolink
            vid.pipeline.set_state(Gst.State.PLAYING)

    except KeyboardInterrupt: #her må det legges inn en quit som er mye bedre. Vis ikke må Pi restartes hver gang. 
        shallRun = False
        serverobj.stop()
        serverobj.join()
        vidobj.stop()

# if setning under er som void i c#. Den setter igang alle "class" i programmet. 
# Over er run_test definert og blir videre kjørt via main under. 
if __name__ == '__main__':
    serverobj = modbusserver()
    serverobj.start()
    vidobj = videoStream()
    vidobj.start()
    run_test()
    
