# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wordfinder.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WordFinder(object):
    def setupUi(self, WordFinder):
        WordFinder.setObjectName("WordFinder")
        WordFinder.resize(408, 353)
        self.centralwidget = QtWidgets.QWidget(WordFinder)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(14, 11, 381, 284))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labPattern = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labPattern.setObjectName("labPattern")
        self.horizontalLayout.addWidget(self.labPattern)
        self.lePattern = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lePattern.setObjectName("lePattern")
        self.horizontalLayout.addWidget(self.lePattern)
        self.btSearch = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btSearch.setObjectName("btSearch")
        self.horizontalLayout.addWidget(self.btSearch)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.teText = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.teText.setObjectName("teText")
        self.verticalLayout.addWidget(self.teText)
        WordFinder.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WordFinder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 408, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        WordFinder.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WordFinder)
        self.statusbar.setObjectName("statusbar")
        WordFinder.setStatusBar(self.statusbar)
        self.actionLoad = QtWidgets.QAction(WordFinder)
        self.actionLoad.setObjectName("actionLoad")
        self.actionQuit = QtWidgets.QAction(WordFinder)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(WordFinder)
        QtCore.QMetaObject.connectSlotsByName(WordFinder)

    def retranslateUi(self, WordFinder):
        _translate = QtCore.QCoreApplication.translate
        WordFinder.setWindowTitle(_translate("WordFinder", "WordFinder"))
        self.labPattern.setText(_translate("WordFinder", "Pattern:"))
        self.btSearch.setText(_translate("WordFinder", "Search"))
        self.menuFile.setTitle(_translate("WordFinder", "File"))
        self.actionLoad.setText(_translate("WordFinder", "Load..."))
        self.actionQuit.setText(_translate("WordFinder", "Quit"))

