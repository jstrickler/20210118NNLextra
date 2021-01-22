# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statusbar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StatusBar(object):
    def setupUi(self, StatusBar):
        StatusBar.setObjectName("StatusBar")
        StatusBar.resize(203, 132)
        self.centralwidget = QtWidgets.QWidget(StatusBar)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btPushMe = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btPushMe.setObjectName("btPushMe")
        self.verticalLayout.addWidget(self.btPushMe)
        StatusBar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StatusBar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 203, 25))
        self.menubar.setObjectName("menubar")
        StatusBar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StatusBar)
        self.statusbar.setObjectName("statusbar")
        StatusBar.setStatusBar(self.statusbar)

        self.retranslateUi(StatusBar)
        QtCore.QMetaObject.connectSlotsByName(StatusBar)

    def retranslateUi(self, StatusBar):
        _translate = QtCore.QCoreApplication.translate
        StatusBar.setWindowTitle(_translate("StatusBar", "StatusBar"))
        self.label.setToolTip(_translate("StatusBar", "I\'m a tooltip!"))
        self.label.setText(_translate("StatusBar", "Hello PyQt5 World"))
        self.btPushMe.setText(_translate("StatusBar", "Push Me"))

