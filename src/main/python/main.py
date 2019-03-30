from fbs_runtime.application_context import ApplicationContext
from PySide2.QtWidgets import *
from PySide2.QtNetwork import QTcpSocket

import sys

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Add components
        self.layout = QVBoxLayout(self)
        self.chat = QTextEdit(self)
        self.chat.setReadOnly(True)
        self.lineEdit = QLineEdit(self)
        self.sendButton = QPushButton(self)
        self.sendButton.setText("Send")

        # Connect to sendText
        self.lineEdit.returnPressed.connect(self.sendText)
        self.sendButton.clicked.connect(self.sendText)

        # Conect TCP
        self.socket = QTcpSocket(self)
        self.socket.connectToHost("localhost", 33000)
        self.socket.readyRead.connect(self.readText)
        
        # Set layout
        self.layout.addWidget(self.chat)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.sendButton)
        
        # Set window settings
        self.setWindowTitle("kszképzés chat")
        self.setLayout(self.layout)
        self.resize(350, 350)

    # Read text over TCP
    def readText(self):
        data = self.socket.readAll()
        self.chat.append(str(data, 'utf-8'))

    # Write text text over TCP
    def sendText(self):
        self.socket.write(self.lineEdit.text().encode('utf-8'))
        self.lineEdit.clear()

    # Send quit when the window is closed
    def closeEvent(self, event):
        self.socket.write("{quit}".encode('utf-8'))

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):                              # 2. Implement run()
        window = MainWindow()
        version = self.build_settings['version']
        window.setWindowTitle("chat v" + version)
        window.show()
        return self.app.exec_()                 # 3. End run() with this line

if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)