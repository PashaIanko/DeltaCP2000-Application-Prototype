import logging

class SessionLogger:
    Logger = None
    FileHandler = None
    Formatter = None

    '''def __new__(self, LoggerName, FileName, LogMode):
        if not hasattr(self, 'instance'):
            self.instance = super(SessionLogger, self).__new__(self)
            self.Logger = logging.getLogger(LoggerName)
            self.Logger.setLevel(LogMode)

            self.FileHandler = logging.FileHandler(FileName + '.log')
            self.Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            self.FileHandler.setFormatter(self.Formatter)
            self.Logger.addHandler(self.FileHandler)'''

    def __init__(self, LoggerName, FileName, LogMode):
        self.Logger = logging.getLogger(LoggerName)
        self.Logger.setLevel(LogMode)

        self.FileHandler = logging.FileHandler(FileName + '.log')
        self.Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.FileHandler.setFormatter(self.Formatter)
        self.Logger.addHandler(self.FileHandler)

    def Info(self, msg):
        self.Logger.info(msg)