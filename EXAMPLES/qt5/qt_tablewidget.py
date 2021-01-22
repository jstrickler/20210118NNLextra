#!/usr/bin/env python
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_tablewidget import Ui_TableWidget


class TableWidgetMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_TableWidget()
        self.ui.setupUi(self)

        self._setupDB()

        self.ui.bt_save.clicked.connect(self._save_changes)
        self.ui.bt_revert.clicked.connect(self._revert)

    def _setupDB(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('../../DATA/presidents.db')
        if not db.open():
            raise Error("Could not open the database")

        self.ui.model = QSqlTableModel(self, db)
        self.ui.model.setTable("presidents")
        self.ui.model.EditStrategy(QSqlTableModel.OnManualSubmit)
        self.ui.tableView.setModel(self.ui.model)
        self.ui.tableView.setSortingEnabled(True)

    def _save_changes(self):
        self.ui.model.submitAll()

    def _revert(self):
        self.ui.model.revertAll()
        self.ui.model.revert()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidgetMain()
    main.show()
    sys.exit(app.exec_())
