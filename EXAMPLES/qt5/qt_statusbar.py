#!/usr/bin/env python
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_statusbar import Ui_StatusBar

class StatusBarMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self._count = 0

        # Setup the user interface from Designer.
        self.ui = Ui_StatusBar()
        self.ui.setupUi(self)

        self.ui.btPushMe.clicked.connect(self._pushed)
        self._update_statusbar() # <1>

    def _pushed(self, ev):
        self._update_statusbar()

    def _update_statusbar(self):
        self._count += 1
        msg = "Count is " + str(self._count)
        self.ui.statusbar.showMessage(msg, 0) # <2>


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBarMain()
    main.show()
    app.exec()


