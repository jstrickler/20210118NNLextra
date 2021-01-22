# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectables.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Selectables(object):
    def setupUi(self, Selectables):
        Selectables.setObjectName("Selectables")
        Selectables.resize(149, 215)
        self.centralwidget = QtWidgets.QWidget(Selectables)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 141, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        Selectables.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Selectables)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 149, 25))
        self.menubar.setObjectName("menubar")
        Selectables.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Selectables)
        self.statusbar.setObjectName("statusbar")
        Selectables.setStatusBar(self.statusbar)

        self.retranslateUi(Selectables)
        QtCore.QMetaObject.connectSlotsByName(Selectables)

    def retranslateUi(self, Selectables):
        _translate = QtCore.QCoreApplication.translate
        Selectables.setWindowTitle(_translate("Selectables", "Selectable Buttons"))
        self.radioButton_2.setText(_translate("Selectables", "Milk"))
        self.radioButton_3.setText(_translate("Selectables", "Half-and-half"))
        self.radioButton.setText(_translate("Selectables", "Soy Milk"))
        self.checkBox.setToolTip(_translate("Selectables", "Check to add sugar"))
        self.checkBox.setText(_translate("Selectables", "Sugar"))

