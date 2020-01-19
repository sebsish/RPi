import time
#import pymodbus #trengs denne? kjor test. 
from modbusserver import modbusserver
from videoStream import videoStream
# til pwm og kjoring av bil
import os
import pigpio
import atexit 

# --------------------------------------------------------------------------- #
# def run_test oppretter en loop nar shallRun er true. shallRun settes 
# false ved keyboardinterrupt. akse verdiene for kjoring av bilen blir hentet 
# fra pymodbus UDP server (ved navn modbusserver.py). serverobj er trad som 
# er gitt av modbusserver.py. 
# --------------------------------------------------------------------------- #
def run_test():
    shallRun = True
    pi=pigpio.pi()
    pi.set_mode(13, pigpio.OUTPUT) # GPIO 13 as output
    pi.set_mode(18, pigpio.OUTPUT) # GPIO 18 as output
    pi.set_servo_pulsewidth(13, 1500)
    pi.set_servo_pulsewidth(18, 1500)

    try:
        while shallRun:   
            #henter modbus verdier
            axis_x = serverobj.getHoldingRegisterValue(0)
            axisX = int(axis_x[0]) #endrer datatype
            axis_y = serverobj.getHoldingRegisterValue(1)
            axisY = int(axis_y[0]) #endrer datatype
            axis_z = serverobj.getHoldingRegisterValue(2)

            # Under er oppretting av pwm signal til servo og esc. 
            pi.set_servo_pulsewidth(13, axisY)     #pulsbredde til ESC
            pi.set_servo_pulsewidth(18, axisX)     #pulsbredde signal til servo motor

            #videolink, skal den inn her? 

    except KeyboardInterrupt: #her ma det legges inn en quit som er mye bedre. Vis ikke ma Pi restartes hver gang programmet stoppes.  
        shallRun = False
        serverobj.stop()
        vidobj.stop()
        serverobj.join()
        atexit.register(all_done)
        exit()



# if setning under er som void i c#. Den setter igang alle "class" i programmet. 
# Over er run_test definert og blir videre kjort via main under. 
if __name__ == '__main__':
    serverobj = modbusserver()
    serverobj.start()
    vidobj = videoStream()
    vidobj.start()
    run_test()
    
