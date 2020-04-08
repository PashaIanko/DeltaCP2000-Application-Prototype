from pymodbus.client.sync import ModbusSerialClient as ModbusClient

from pymodbus.constants import Defaults
Defaults.RetryOnEmpty = True
Defaults.Timeout = 5
Defaults.Retries = 5


class FTClient(ModbusClient):
    # Frequency Transducer Client
    def __init__\
        (
                self,
                Protocol,
                COMPort,
                Timeout,
                StopBits,
                ByteSize,
                Parity,
                BaudRate
        ):

        self.if_connected = False
        self.client = ModbusClient\
            (
                method = Protocol,
                port = COMPort,
                timeout = Timeout,
                stopbits = StopBits,
                bytesize = ByteSize,
                parity = Parity,
                baudrate = BaudRate
            )
        self.Tesing_mode = True

    def Connect(self):
        if(self.Tesing_mode == False):
            self.if_connected = self.client.connect()
            return self.if_connected
        else:
            return True

    def WriteOutputFreqRegister(self, FreqStr):
        print('writing the f=' + str(FreqStr) + ' in the output register')
        pass

    def SendRunCommand(self):
        pass

# Source Code from video on Youtube:
#client = ModbusClient(
#    method = 'rtu',
#    port = 'COM4',
#    timeout = 2,
#    stopbits = 1,
#    bytesize = 8,
#    parity = 'N',
#    baudrate = 2400
#)

#while True:
   # hh = client.read_holding_registers(address = 245, count = 8, unit = 1)
   # h2 = hh.registers[7]/10

   # print(h2)