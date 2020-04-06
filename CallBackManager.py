from GraphicsShell import *
import ConnectionParameters
import Connector


class CallBackManager(GraphicsShell):

    def __init__(self, window):
        self.setupUi(window)


        # Connector to try connecting to FT
        self.Connector = Connector.Connector()

        # Connection Parameters Entity
        self.ConnectionParams = ConnectionParameters.ConnectionParameters()

        self.ConnectCallBacks()
        self.ConnectPushButtons()



    def ConnectCallBacks(self):
        self.BaudRatecomboBox.currentIndexChanged.connect   (self.SetBaudRate)
        self.COMPortcomboBox.currentIndexChanged.connect    (self.SetCOMPort)
        self.ProtocolcomboBox.currentIndexChanged.connect   (self.SetProtocol)
        self.ByteSizecomboBox.currentIndexChanged.connect   (self.SetByteSize)
        self.ParitycomboBox.currentIndexChanged.connect     (self.SetParity)
        self.StopBitscomboBox.currentIndexChanged.connect   (self.SetStopBits)


    def ConnectPushButtons(self):
        self.ConnectpushButton.clicked.connect(self.Connect)


    def SetProtocol(self):
        self.ConnectionParams.SetProtocol(self.ProtocolcomboBox.currentText())# = self.ProtocolcomboBox.currentText()


    def SetByteSize(self):
        self.ConnectionParams.SetByteSize(int(self.ByteSizecomboBox.currentText()))

    def SetParity(self):
        self.ConnectionParams.SetParity(self.ParitycomboBox.currentText())

    def SetStopBits(self):
        self.ConnectionParams.SetStopBits(int(self.StopBitscomboBox.currentText()))


    def SetBaudRate(self):
        self.ConnectionParams.SetBaudRate(int(self.BaudRatecomboBox.currentText()))

        
    def SetCOMPort(self):
        self.ConnectionParams.SetCOMPort(int(self.COMPortcomboBox.currentText()))


    def Connect(self):
        self.Connector.Connect(self.ConnectionParams.GetConnectionParameters())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = CallBackManager(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())