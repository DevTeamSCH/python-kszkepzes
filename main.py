import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile, QByteArray
from PySide2.QtNetwork import QTcpSocket
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.socket = QTcpSocket()
        self.socket.connectToHost("localhost", 33000)
        self.socket.readyRead.connect(self.readText)
        self.ui.lineEdit.returnPressed.connect(self.sendText)

    def readText(self):
        data = self.socket.readAll()
        self.ui.chat.append(str(data, 'utf-8'))

    def sendText(self):
        self.socket.write(self.ui.lineEdit.text().encode('utf-8'))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
