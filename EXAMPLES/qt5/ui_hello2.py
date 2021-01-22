# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Hello2(object):
    def setupUi(self, Hello2):
        Hello2.setObjectName("Hello2")
        Hello2.resize(203, 164)
        self.centralwidget = QtWidgets.QWidget(Hello2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 141, 21))
        self.label.setObjectName("label")
        Hello2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Hello2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 203, 25))
        self.menubar.setObjectName("menubar")
        Hello2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Hello2)
        self.statusbar.setObjectName("statusbar")
        Hello2.setStatusBar(self.statusbar)

        self.retranslateUi(Hello2)
        QtCore.QMetaObject.connectSlotsByName(Hello2)

    def retranslateUi(self, Hello2):
        _translate = QtCore.QCoreApplication.translate
        Hello2.setWindowTitle(_translate("Hello2", "Hello2"))
        self.label.setText(_translate("Hello2", "Hello PyQt5 World"))

