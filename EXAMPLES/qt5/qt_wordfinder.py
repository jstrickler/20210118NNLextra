#!/usr/bin/env python
import sys
import re

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from ui_wordfinder import Ui_WordFinder

class WordFinderMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        # Set up the user interface from Designer.
        self.ui = Ui_WordFinder()
        self.ui.setupUi(self)

        self.ui.actionQuit.triggered.connect(lambda:self.close())

        self.ui.actionLoad.triggered.connect(self._load_file)

        self.ui.lePattern.returnPressed.connect(self._search)

        # the following might be too time-consuming for large files
        # self.ui.lePattern.textChanged.connect(self._search)

        self.ui.btSearch.clicked.connect(self._search)
±jang
    def _load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, 'Open file for matching', '.'
        )
        if file_name:
            with open(file_name) as F:
                self._words = [ line.rstrip() for line in F ]

            self._numwords = len(self._words)
            self.ui.teText.clear()

            self.ui.teText.insertPlainText(
                '\n'.join(self._words))

    def _search(self):
        pattern = str(self.ui.lePattern.text())
        if pattern == '':
            pattern = '.'
        rx = re.compile(pattern)

        self.ui.teText.clear()
        self.ui.lePattern.setEnabled(False)
        # self.lePattern.setVisible(False)
        count = 0
        for word in self._words:
            if rx.search(word):
                self.ui.teText.insertPlainText(word + '\n')
                count += 1
        self.ui.lePattern.setEnabled(True)
        #self.ui.lePattern.setVisible(True)
        self.ui.statusbar.showMessage(
            "Matched {0} out of {1} words".format(count,self._numwords),
            0
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = WordFinderMain()
    main.show()
    sys.exit(app.exec_())


