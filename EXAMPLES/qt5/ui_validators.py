# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'validators.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Validators(object):
    def setupUi(self, Validators):
        Validators.setObjectName("Validators")
        Validators.resize(386, 253)
        self.centralwidget = QtWidgets.QWidget(Validators)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lab_alphanum = QtWidgets.QLabel(self.formLayoutWidget)
        self.lab_alphanum.setObjectName("lab_alphanum")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lab_alphanum)
        self.le_alphanum = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_alphanum.setObjectName("le_alphanum")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_alphanum)
        self.lab_letters_space = QtWidgets.QLabel(self.formLayoutWidget)
        self.lab_letters_space.setObjectName("lab_letters_space")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lab_letters_space)
        self.le_lcspace = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_lcspace.setObjectName("le_lcspace")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_lcspace)
        self.lab_nums_1_100 = QtWidgets.QLabel(self.formLayoutWidget)
        self.lab_nums_1_100.setObjectName("lab_nums_1_100")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lab_nums_1_100)
        self.le_nums_1_100 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_nums_1_100.setObjectName("le_nums_1_100")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_nums_1_100)
        self.lab_float = QtWidgets.QLabel(self.formLayoutWidget)
        self.lab_float.setObjectName("lab_float")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lab_float)
        self.le_float = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_float.setObjectName("le_float")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_float)
        self.bt_save = QtWidgets.QPushButton(self.centralwidget)
        self.bt_save.setGeometry(QtCore.QRect(140, 170, 110, 32))
        self.bt_save.setObjectName("bt_save")
        Validators.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Validators)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 386, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Validators.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Validators)
        self.statusbar.setObjectName("statusbar")
        Validators.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(Validators)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Validators)
        self.actionQuit.triggered.connect(Validators.close)
        QtCore.QMetaObject.connectSlotsByName(Validators)

    def retranslateUi(self, Validators):
        _translate = QtCore.QCoreApplication.translate
        Validators.setWindowTitle(_translate("Validators", "MainWindow"))
        self.lab_alphanum.setText(_translate("Validators", "Alphanumeric"))
        self.lab_letters_space.setText(_translate("Validators", "Lower case letters and spaces"))
        self.lab_nums_1_100.setText(_translate("Validators", "Numbers 1 to 100"))
        self.lab_float.setText(_translate("Validators", "Floating point"))
        self.bt_save.setText(_translate("Validators", "Save"))
        self.menuFile.setTitle(_translate("Validators", "File"))
        self.actionQuit.setText(_translate("Validators", "Quit"))

