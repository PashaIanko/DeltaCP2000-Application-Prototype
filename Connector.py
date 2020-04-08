from pymodbus.exceptions import ParameterException
import PopUpNotifier
import CrashNotifier
import FTClient
import sys

class Connector:
    def __init__(self):

        self.ConnectionParameters = {}

        self.Protocol = " "
        self.COMPort = 0
        self.StopBits = 0
        self.ByteSize = 0
        self.Parity = " "
        self.BaudRate = 0
        self.Timeout = 2

        self.IfClientConnected = False

        #self.DeltaCPClient = 0
        self.PopUpNotifier = PopUpNotifier.PopUpNotifier()
        self.CrashNotifier = CrashNotifier.CrashNotifier()

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
            self.PopUpNotifier.ConnectionProgressNotify(self.IfClientConnected)
            #self.DeltaCPClient.Connect()
            #self.PopUpNotifier.ConnectionProgressNotify(self.DeltaCPClient.if_connected)


        except ParameterException:
            self.CrashNotifier.ExceptionNotify("Invalid Parameters")
        except:
            error_name = sys.exc_info()
            if (error_name is ValueError):
                self.CrashNotifier.ValueErrorNotify("Value error in Connector.Connect()")
            if(error_name is ZeroDivisionError):
                self.CrashNotifier.ValueErrorNotify("Zero division in Connector.Connect(), please set Bauв Rate")
            else:
                self.CrashNotifier.UnexpectedErrorNotify(' in Connector.Connect()')



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

    def CheckClientConnection(self):
        return self.IfClientConnected

    def SetOutputFrequency(self, freq_str):
        # print('in Connector')
        # print(freq_str)
        if(len(freq_str) == 0):
            freq_str = '0'
        if(self.CheckClientConnection()):
            self.DeltaCPClient.WriteOutputFreqRegister(freq_str)
        else:
            self.PopUpNotifier.ClientNotConnectedNotify()

    def RunFT(self):
        if(self.CheckClientConnection()):
            self.DeltaCPClient.SendRunCommand()
        else:
            self.CrashNotifier.CrashNotify("Sending Run Command: Client is not connected!")







