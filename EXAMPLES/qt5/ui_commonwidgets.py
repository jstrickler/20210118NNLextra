# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commonwidgets.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CommonWidgets(object):
    def setupUi(self, CommonWidgets):
        CommonWidgets.setObjectName("CommonWidgets")
        CommonWidgets.resize(336, 196)
        self.centralwidget = QtWidgets.QWidget(CommonWidgets)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btPushMe = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btPushMe.setObjectName("btPushMe")
        self.verticalLayout.addWidget(self.btPushMe)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labName.setObjectName("labName")
        self.horizontalLayout.addWidget(self.labName)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.cbFruits = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cbFruits.setObjectName("cbFruits")
        self.verticalLayout.addWidget(self.cbFruits)
        CommonWidgets.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CommonWidgets)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 25))
        self.menubar.setObjectName("menubar")
        CommonWidgets.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CommonWidgets)
        self.statusbar.setObjectName("statusbar")
        CommonWidgets.setStatusBar(self.statusbar)
        self.labName.setBuddy(self.lineEdit)

        self.retranslateUi(CommonWidgets)
        QtCore.QMetaObject.connectSlotsByName(CommonWidgets)

    def retranslateUi(self, CommonWidgets):
        _translate = QtCore.QCoreApplication.translate
        CommonWidgets.setWindowTitle(_translate("CommonWidgets", "Common Widgets"))
        self.btPushMe.setText(_translate("CommonWidgets", "PushButton"))
        self.labName.setText(_translate("CommonWidgets", "&Name"))

