from pymodbus.exceptions import ParameterException

import FTClient

class Connector:
    def __init__(self):

        self.ConnectionParameters = {}

        self.Protocol = ""
        self.COMPort = 0
        self.StopBits = 0
        self.ByteSize = 0
        self.Parity = ""
        self.BaudRate = 0
        self.Timeout = 2

        self.IfClientConnected = False

        self.DeltaCPClient = 0

    def Connect(self, connectionparameters):
        self.ConnectionParameters = connectionparameters

        for ParamName, Value in self.ConnectionParameters.items():
            self.FillConnectionParameters(ParamName, Value)

        # Fit Parameters into proper formats for PyModbus Library
        self.ProxyFiltParameters()

        try:
            self.DeltaCPClient = FTClient.FTClient (
                self.Protocol,
                self.COMPort,
                self.Timeout,
                self.StopBits,
                self.ByteSize,
                self.Parity,
                self.BaudRate
            )
            self.IfClientConnected = self.DeltaCPClient.Connect()
            print('If connected:', self.IfClientConnected)
        except ParameterException:
            print("Invalid Parameters!")


    def ProxyFiltParameters(self):
        self.Protocol = self.Protocol.lower()

        COM_str = "COM" + str(self.COMPort)
        self.COMPort = COM_str

    def FillConnectionParameters(self, ParamName, Value):
        ParamName_ = ParamName.lower()
        if (ParamName_ == 'protocol'):
            self.Protocol = Value
        if (ParamName_ == 'comport'):
            self.COMPort = Value
        if(ParamName_ == 'stopbits'):
            self.StopBits = Value
        if(ParamName_ == 'bytesize'):
            self.ByteSize = Value
        if(ParamName_ == 'parity'):
            self.Parity = Value
        if(ParamName_ == 'baudrate'):
            self.BaudRate = Value



