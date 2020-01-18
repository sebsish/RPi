
#!/usr/bin/env python
"""
Pymodbus Synchronous Server Example
--------------------------------------------------------------------------
The synchronous server is implemented in pure python without any third
party libraries (unless you need to use the serial protocols which require
pyserial). This is helpful in constrained or old environments where using
twisted is just not feasible. What follows is an example of its use:
--------------------------------------------------------------------------
"""

from pymodbus.server.sync import StartUdpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from threading import Thread

# --------------------------------------------------------------------------- #
# configure the service logging
# Oppretter en logfil og logger hva som skjer
# --------------------------------------------------------------------------- #
import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.WARNING)

# --------------------------------------------------------------------------- #
# Insert info about class
# --------------------------------------------------------------------------- #

class modbusserver(Thread):
    def __init__(self):
        ''' Constructor. '''
        Thread.__init__(self)
        self.store = ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [17]*100),
            co=ModbusSequentialDataBlock(0, [17]*100),
            hr=ModbusSequentialDataBlock(0, [13]*100),
            ir=ModbusSequentialDataBlock(0, [17]*100))
        self.identity = ModbusDeviceIdentification()
        self.identity.VendorName = 'Pymodbus'
        self.identity.ProductCode = 'PM'
        self.identity.VendorUrl = 'http://github.com/riptideio/pymodbus/'
        self.identity.ProductName = 'Pymodbus Server'
        self.identity.ModelName = 'Pymodbus Server'
        self.identity.MajorMinorRevision = '2.3.0'

    # Insert info about def run(self) 
    # Starter UDP serveren          
    def run(self):    
        self.context = ModbusServerContext(slaves=self.store, single=True)
        StartUdpServer(self.context, identity=self.identity, address=("0.0.0.0", 502))

    # Insert info about def stop(f)
    # egen def for å stoppe serveren
    def stop(self):
        StopServer()
    
    # def henter holdingregister verdier, den lister 3stk.  
    def getHoldingRegisterValue(self, regNr):
        # UNIT = 0x1
        return self.store.getValues(3,regNr,1)