#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import QRegExp

from ui_validators import Ui_Validators

class ValidatorsMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_Validators()

        self.ui.setupUi(self)
        self._set_validators()

        self.ui.bt_save.clicked.connect(self._save_pushed)

    def _set_validators(self):
        # Set up the validators (could be in separate function or module)
        reg_ex = QRegExp(r"[A-Za-z0-9]{1,10}") # <1>
        val_alphanum = QRegExpValidator(reg_ex, self.ui.le_alphanum)  # <2>
        self.ui.le_alphanum.setValidator(val_alphanum) # <3>

        reg_ex = QRegExp(r"[a-z ]{0,30}") # <1>
        val_lcspace = QRegExpValidator(reg_ex, self.ui.le_lcspace)  # <2>
        self.ui.le_lcspace.setValidator(val_lcspace) # <3>

        val_nums_1_100 = QIntValidator(1, 100, self.ui.le_nums_1_100)  # <4>
        self.ui.le_nums_1_100.setValidator(val_nums_1_100)  # <5>

        val_float = QDoubleValidator(0.0, 20.0, 2, self.ui.le_float)  # <6>
        self.ui.le_float.setValidator(val_float)  # <7>

    def _save_pushed(self):
        alphanum = self.ui.le_alphanum.text()
        lcspace = self.ui.le_lcspace.text()
        nums = self.ui.le_nums_1_100.text()
        fl = self.ui.le_float.text()
        msg = '{}/{}/{}/{}'.format(alphanum, lcspace, nums, fl)
        self.ui.statusbar.showMessage(msg, 0) # <8>

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ValidatorsMain()
    main.show()
    sys.exit(app.exec_())


