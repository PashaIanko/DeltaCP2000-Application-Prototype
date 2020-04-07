from PyQt5.QtWidgets import  QMessageBox

class CrashNotifier(object):

    # CrashNotifier implements SingleTon pattern

    obj = None

    def __new__(cls, *dt, **mp):
        if cls.obj is None:
            cls.obj = object.__new__(cls, *dt, **mp)  # вызовем __new__ родительского класса
            return cls.obj

    def ExceptionNotify(self, window_message):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(window_message)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def ValueErrorNotify(self, window_message):
        msg = QMessageBox()
        msg.setWindowTitle("Value error")
        msg.setText(window_message)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def UnexpectedErrorNotify(self, window_message):
        msg = QMessageBox()
        msg.setWindowTitle("Unexpected error")
        msg.setText('Unexpected error in ' + str(window_message))
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()