# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'peer.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 247)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.host_name_label = QtWidgets.QLabel(self.centralwidget)
        self.host_name_label.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.host_name_label.setObjectName("host_name_label")
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(100, 20, 141, 20))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(250, 20, 75, 81))
        self.save_btn.setObjectName("save_btn")
        self.host_ip_label = QtWidgets.QLabel(self.centralwidget)
        self.host_ip_label.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.host_ip_label.setObjectName("host_ip_label")
        self.host_port_label = QtWidgets.QLabel(self.centralwidget)
        self.host_port_label.setGeometry(QtCore.QRect(20, 80, 81, 21))
        self.host_port_label.setObjectName("host_port_label")
        self.lineEdit_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ip.setGeometry(QtCore.QRect(100, 50, 141, 20))
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.lineEdit_port = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_port.setGeometry(QtCore.QRect(100, 80, 141, 20))
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.to_host_ip_label = QtWidgets.QLabel(self.centralwidget)
        self.to_host_ip_label.setGeometry(QtCore.QRect(20, 150, 81, 21))
        self.to_host_ip_label.setObjectName("to_host_ip_label")
        self.to_host_port_label = QtWidgets.QLabel(self.centralwidget)
        self.to_host_port_label.setGeometry(QtCore.QRect(20, 180, 81, 21))
        self.to_host_port_label.setObjectName("to_host_port_label")
        self.lineEdit_to_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_to_ip.setGeometry(QtCore.QRect(100, 150, 141, 20))
        self.lineEdit_to_ip.setObjectName("lineEdit_to_ip")
        self.lineEdit_to_port = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_to_port.setGeometry(QtCore.QRect(100, 180, 141, 20))
        self.lineEdit_to_port.setObjectName("lineEdit_to_port")
        self.info_btn = QtWidgets.QPushButton(self.centralwidget)
        self.info_btn.setGeometry(QtCore.QRect(250, 150, 75, 51))
        self.info_btn.setObjectName("info_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.host_name_label.setText(_translate("MainWindow", "My Name"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.host_ip_label.setText(_translate("MainWindow", "Host IP"))
        self.host_port_label.setText(_translate("MainWindow", "Host Port"))
        self.to_host_ip_label.setText(_translate("MainWindow", "To Host IP"))
        self.to_host_port_label.setText(_translate("MainWindow", "To Host Port"))
        self.info_btn.setText(_translate("MainWindow", "Send"))

