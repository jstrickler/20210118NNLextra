#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_hello2 import Ui_Hello2  # <1>

class Hello2Main(QMainWindow):   
    def __init__(self):
        QMainWindow.__init__(self)

        # <2>
        self.ui = Ui_Hello2()  # <3>
        self.ui.setupUi(self)  # <4>

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Hello2Main()
    main.show()
    sys.exit(app.exec_())


