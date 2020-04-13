from GraphicsShell import *
import ConnectionParameters
import Connector
import SessionLogger as Logger
import logging

class Test:
    def __init__(self):
        self.N = 0

    def Callback(self, connectionP):
        print(connectionP)
        print(connectionP.GetConnectionParameters())

class CallBackManager(GraphicsShell):

    def __init__(self, window):
        self.setupUi(window)

        self.TestCallBack = Test()

        # Connector to try connecting to FT
        self.Connector = Connector.Connector()

        # Connection Parameters Entity
        self.ConnectionParams = ConnectionParameters.ConnectionParameters()

        # Connecting signals
        self.ConnectComboBoxes()
        self.ConnectPushButtons()
        self.SyncSlidersandTexts()

    def SyncSlidersandTexts(self):
        self.FrequencySetSlider.valueChanged.connect(self.FrequencySetlineEditValueChange)
        self.FrequencySetlineEdit.textEdited.connect(self.FrequencySetSliderValueChange)


    def FrequencySetlineEditValueChange(self):
        try:
            #lineEditText = self.FrequencySetlineEdit.text()
            self.FrequencySetlineEdit.setText(str(self.FrequencySetSlider.value()/10))
        except:
            print('caught!')


    def FrequencySetSliderValueChange(self):
        lineEditText = self.FrequencySetlineEdit.text()
        if(len(lineEditText) == 0):
            lineEditText = '0'
        try:
            value = float(lineEditText) * 10
            self.FrequencySetSlider.setValue(value)
        except:
            pass
            # This exception implies some problems with the manual input
            # print('caught in slider')

    def ConnectComboBoxes(self):
        self.BaudRatecomboBox.currentIndexChanged.connect   (self.SetBaudRate)
        self.COMPortcomboBox.currentIndexChanged.connect    (self.SetCOMPort)
        self.ProtocolcomboBox.currentIndexChanged.connect   (self.SetProtocol)
        self.ByteSizecomboBox.currentIndexChanged.connect   (self.SetByteSize)
        self.ParitycomboBox.currentIndexChanged.connect     (self.SetParity)
        self.StopBitscomboBox.currentIndexChanged.connect   (self.SetStopBits)




    def ConnectPushButtons(self):
        self.ConnectpushButton.clicked.connect(self.Connect)
        self.TestpushButton.clicked.connect(lambda: self.TestCallBack.Callback(self.ConnectionParams))
        self.SetFreqpushButton.clicked.connect(lambda: self.Connector.SetOutputFrequency(self.FrequencySetlineEdit.text()))
        self.RunpushButton.clicked.connect(lambda: self.Connector.RunFT())


    def SetProtocol(self):
        arg = self.ProtocolcomboBox.currentText()
        if(len(arg)):
            self.ConnectionParams.SetProtocol(self.ProtocolcomboBox.currentText())# = self.ProtocolcomboBox.currentText()


    def SetByteSize(self):
        arg = self.ByteSizecomboBox.currentText()
        if(len(arg)):
            self.ConnectionParams.SetByteSize(int(arg))

    def SetParity(self):
        arg = self.ParitycomboBox.currentText()
        if(len(arg)):
            self.ConnectionParams.SetParity(arg)

    def SetStopBits(self):
        arg = self.StopBitscomboBox.currentText()
        if(len(arg)):
            self.ConnectionParams.SetStopBits(int(self.StopBitscomboBox.currentText()))


    def SetBaudRate(self):
        arg = self.BaudRatecomboBox.currentText()
        if(len(arg)):
            self.ConnectionParams.SetBaudRate(int(self.BaudRatecomboBox.currentText()))

        
    def SetCOMPort(self):
        arg = self.COMPortcomboBox.currentText()
        if(len(arg)):
            self.ConnectionParams.SetCOMPort(int(self.COMPortcomboBox.currentText()))


    def Connect(self):
        self.Connector.Connect(self.ConnectionParams.GetConnectionParameters())




if __name__ == "__main__":
    import sys

    SessionLogger = Logger.SessionLogger('TestLogger', "TestLog", logging.INFO)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CallBackManager(MainWindow)

    MainWindow.show()
    SessionLogger.Info('Application Started')


#    NewSessionLogger = Logger.SessionLogger('TestLogger', "TestLog", logging.INFO)
#    NewSessionLogger.Info("This msg is from another logger")
#    print('if the same', NewSessionLogger is SessionLogger)
    sys.exit(app.exec_())



