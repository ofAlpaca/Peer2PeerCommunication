from peer_ui import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from MessageCenter import Peer, MessageCenter
import sys

class MyForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.p = None
        self.ui.save_btn.clicked.connect(self.save_info)
        self.ui.info_btn.clicked.connect(self.send_info)

    def save_info(self):
        myname = self.ui.lineEdit_id.text()
        host_ip = self.ui.lineEdit_ip.text()
        host_port = int(self.ui.lineEdit_port.text())
        self.p = Peer(5, host_port, myname, host_ip)
        self.p.start()

    def send_info(self):
        send_ip = self.ui.lineEdit_to_ip.text()
        send_port = int(self.ui.lineEdit_to_port.text())
        self.p.connectandsend(send_ip, send_port, 'info', 'I am good.', )



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())