import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView

from forms.mainform import Ui_MainWindow
from _test.data import *


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.show()
        self.cmdBooks.clicked.connect(lambda: self.cmd_clicked('B'))
        self.cmdReaders.clicked.connect(lambda: self.cmd_clicked('R'))

    def cmd_clicked(self, typ):
        if typ == 'B':
            self.prepare_table_for_books()
        else:
            self.prepare_table_for_readers()

        self.tableWidget.resizeColumnsToContents()

    def prepare_table_for_books(self):
        self.tableWidget.setRowCount(len(get_books()))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Author', 'Page number', 'Short description'])
        for count, book in enumerate(get_books()):
            self.tableWidget.setItem(count, 0, QTableWidgetItem(book['name']))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(book['Author']))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(str(book['Page_number'])))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(book['Short_Description']))

    def prepare_table_for_readers(self):
        self.tableWidget.setRowCount(len(get_readers()))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Start Time', 'End time', 'Before books'])
        for count, reader in enumerate(get_readers()):
            self.tableWidget.setItem(count, 0, QTableWidgetItem(reader['name']))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(reader['start_time']))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(str(reader['end_time'])))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(reader['before']))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    sys.exit(app.exec_())
