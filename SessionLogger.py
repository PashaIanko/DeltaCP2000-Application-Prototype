import logging


def Singleton(theClass):
    """ decorator for a class to make a singleton out of it """
    classInstances = {}

    def getInstance(*args, **kwargs):
        """ creating or just return the one and only class instance.
            The singleton depends on the parameters used in __init__ """
        key = (theClass, args, str(kwargs))
        if key not in classInstances:
            classInstances[key] = theClass(*args, **kwargs)
        return classInstances[key]

    return getInstance

@Singleton
class SessionLogger:
    Logger = None
    FileHandler = None
    Formatter = None

    def __init__(self, LoggerName, FileName, LogMode):
        self.Logger = logging.getLogger(LoggerName)
        self.Logger.setLevel(LogMode)

        self.FileHandler = logging.FileHandler(FileName + '.log')
        self.Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.FileHandler.setFormatter(self.Formatter)
        self.Logger.addHandler(self.FileHandler)

    def Info(self, msg):
        self.Logger.info(msg)