#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel # <1>

class HelloWindow(QMainWindow): # <2>

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)  # <3>
        self._label = QLabel("Hello PyQt5 World")
        self.setCentralWidget(self._label)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # <4>
    main_window = HelloWindow()
    main_window.show()
    sys.exit(app.exec_())
