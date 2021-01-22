# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpresinfo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PresInfo(object):
    def setupUi(self, PresInfo):
        PresInfo.setObjectName("PresInfo")
        PresInfo.resize(377, 309)
        self.centralwidget = QtWidgets.QWidget(PresInfo)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 381, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labTermNum = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labTermNum.setObjectName("labTermNum")
        self.horizontalLayout_2.addWidget(self.labTermNum)
        self.leTermNum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.leTermNum.setObjectName("leTermNum")
        self.horizontalLayout_2.addWidget(self.leTermNum)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.btGetInfo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btGetInfo.setObjectName("btGetInfo")
        self.verticalLayout_2.addWidget(self.btGetInfo)
        self.pteInfo = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.pteInfo.setObjectName("pteInfo")
        self.verticalLayout_2.addWidget(self.pteInfo)
        PresInfo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PresInfo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 377, 25))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        PresInfo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PresInfo)
        self.statusbar.setObjectName("statusbar")
        PresInfo.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(PresInfo)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFIle.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(PresInfo)
        QtCore.QMetaObject.connectSlotsByName(PresInfo)

    def retranslateUi(self, PresInfo):
        _translate = QtCore.QCoreApplication.translate
        PresInfo.setWindowTitle(_translate("PresInfo", "President Info"))
        self.labTermNum.setText(_translate("PresInfo", "Enter Term Number:"))
        self.btGetInfo.setText(_translate("PresInfo", "Get Information"))
        self.menuFIle.setTitle(_translate("PresInfo", "FIle"))
        self.actionQuit.setText(_translate("PresInfo", "Quit"))

