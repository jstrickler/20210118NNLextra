# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tablewidget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TableWidget(object):
    def setupUi(self, TableWidget):
        TableWidget.setObjectName("TableWidget")
        TableWidget.resize(1048, 598)
        self.centralwidget = QtWidgets.QWidget(TableWidget)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_save = QtWidgets.QPushButton(self.centralwidget)
        self.bt_save.setGeometry(QtCore.QRect(290, 510, 128, 51))
        self.bt_save.setObjectName("bt_save")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 10, 1021, 471))
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.bt_revert = QtWidgets.QPushButton(self.centralwidget)
        self.bt_revert.setGeometry(QtCore.QRect(500, 510, 131, 51))
        self.bt_revert.setObjectName("bt_revert")
        TableWidget.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TableWidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        TableWidget.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TableWidget)
        self.statusbar.setObjectName("statusbar")
        TableWidget.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(TableWidget)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(TableWidget)
        self.actionExit.triggered.connect(TableWidget.close)
        QtCore.QMetaObject.connectSlotsByName(TableWidget)

    def retranslateUi(self, TableWidget):
        _translate = QtCore.QCoreApplication.translate
        TableWidget.setWindowTitle(_translate("TableWidget", "Table Widget Demo"))
        self.bt_save.setText(_translate("TableWidget", "Save Changes"))
        self.bt_revert.setText(_translate("TableWidget", "Revert Changes"))
        self.menuFile.setTitle(_translate("TableWidget", "File"))
        self.actionExit.setText(_translate("TableWidget", "Exit"))

