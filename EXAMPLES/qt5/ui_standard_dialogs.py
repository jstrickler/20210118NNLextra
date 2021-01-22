# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'standarddialogs.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StandardDialogs(object):
    def setupUi(self, StandardDialogs):
        StandardDialogs.setObjectName("StandardDialogs")
        StandardDialogs.resize(285, 221)
        self.centralwidget = QtWidgets.QWidget(StandardDialogs)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 3, 279, 165))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btColor = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btColor.setObjectName("btColor")
        self.verticalLayout.addWidget(self.btColor)
        self.btFile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btFile.setObjectName("btFile")
        self.verticalLayout.addWidget(self.btFile)
        self.btMessage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btMessage.setObjectName("btMessage")
        self.verticalLayout.addWidget(self.btMessage)
        self.btInput = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btInput.setObjectName("btInput")
        self.verticalLayout.addWidget(self.btInput)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        StandardDialogs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StandardDialogs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 285, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        StandardDialogs.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StandardDialogs)
        self.statusbar.setObjectName("statusbar")
        StandardDialogs.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(StandardDialogs)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(StandardDialogs)
        QtCore.QMetaObject.connectSlotsByName(StandardDialogs)

    def retranslateUi(self, StandardDialogs):
        _translate = QtCore.QCoreApplication.translate
        StandardDialogs.setWindowTitle(_translate("StandardDialogs", "StandardDialogs"))
        self.btColor.setText(_translate("StandardDialogs", "Select Color"))
        self.btFile.setText(_translate("StandardDialogs", "Select File"))
        self.btMessage.setText(_translate("StandardDialogs", "Show Error Message"))
        self.btInput.setText(_translate("StandardDialogs", "Input Text"))
        self.label.setText(_translate("StandardDialogs", "Push a button..."))
        self.menuFile.setTitle(_translate("StandardDialogs", "File"))
        self.actionQuit.setText(_translate("StandardDialogs", "Quit"))

