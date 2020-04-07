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
            return self.client.connect()
        else:
            return True


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