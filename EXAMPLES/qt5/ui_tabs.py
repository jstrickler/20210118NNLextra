# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabs.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tabs(object):
    def setupUi(self, Tabs):
        Tabs.setObjectName("Tabs")
        Tabs.resize(526, 348)
        self.centralwidget = QtWidgets.QWidget(Tabs)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-7, 6, 525, 299))
        self.tabWidget.setObjectName("tabWidget")
        self.tabA = QtWidgets.QWidget()
        self.tabA.setObjectName("tabA")
        self.labA = QtWidgets.QLabel(self.tabA)
        self.labA.setGeometry(QtCore.QRect(34, 55, 471, 134))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.labA.setFont(font)
        self.labA.setObjectName("labA")
        self.tabWidget.addTab(self.tabA, "")
        self.tabB = QtWidgets.QWidget()
        self.tabB.setObjectName("tabB")
        self.labB = QtWidgets.QLabel(self.tabB)
        self.labB.setGeometry(QtCore.QRect(37, 59, 445, 134))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.labB.setFont(font)
        self.labB.setObjectName("labB")
        self.tabWidget.addTab(self.tabB, "")
        self.tabC = QtWidgets.QWidget()
        self.tabC.setObjectName("tabC")
        self.labC = QtWidgets.QLabel(self.tabC)
        self.labC.setGeometry(QtCore.QRect(46, 58, 454, 134))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.labC.setFont(font)
        self.labC.setObjectName("labC")
        self.tabWidget.addTab(self.tabC, "")
        Tabs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tabs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 526, 25))
        self.menubar.setObjectName("menubar")
        self.menuTabs = QtWidgets.QMenu(self.menubar)
        self.menuTabs.setObjectName("menuTabs")
        Tabs.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tabs)
        self.statusbar.setObjectName("statusbar")
        Tabs.setStatusBar(self.statusbar)
        self.actionA = QtWidgets.QAction(Tabs)
        self.actionA.setObjectName("actionA")
        self.actionB = QtWidgets.QAction(Tabs)
        self.actionB.setObjectName("actionB")
        self.actionC = QtWidgets.QAction(Tabs)
        self.actionC.setObjectName("actionC")
        self.actionQuit = QtWidgets.QAction(Tabs)
        self.actionQuit.setObjectName("actionQuit")
        self.menuTabs.addAction(self.actionA)
        self.menuTabs.addAction(self.actionB)
        self.menuTabs.addAction(self.actionC)
        self.menuTabs.addAction(self.actionQuit)
        self.menubar.addAction(self.menuTabs.menuAction())

        self.retranslateUi(Tabs)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Tabs)

    def retranslateUi(self, Tabs):
        _translate = QtCore.QCoreApplication.translate
        Tabs.setWindowTitle(_translate("Tabs", "Tabs"))
        self.labA.setText(_translate("Tabs", "Apple"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabA), _translate("Tabs", "A"))
        self.labB.setText(_translate("Tabs", "Banana"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabB), _translate("Tabs", "B"))
        self.labC.setText(_translate("Tabs", "Cherry"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabC), _translate("Tabs", "C"))
        self.menuTabs.setTitle(_translate("Tabs", "Tabs"))
        self.actionA.setText(_translate("Tabs", "A"))
        self.actionB.setText(_translate("Tabs", "B"))
        self.actionC.setText(_translate("Tabs", "C"))
        self.actionQuit.setText(_translate("Tabs", "Quit"))

