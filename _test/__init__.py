import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView

from forms.mainform import Ui_MainWindow
from _test.prepare_data import *


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.show()
        self.cmdBooks.clicked.connect(lambda: self.cmd_clicked('B'))
        self.cmdReaders.clicked.connect(lambda: self.cmd_clicked('R'))

    def cmd_clicked(self, typ):
        if typ == 'B':
            self.prepare_table(get_books(), ['Name', 'Author', 'Page Number', 'Short Description'])
        else:
            self.prepare_table(get_readers(), ['Name', 'Start Time', 'End Time', 'Read Books'])

        self.tableWidget.resizeColumnsToContents()

    def prepare_table(self, all_data, cols):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(len(all_data))
        self.tableWidget.setColumnCount(len(cols))
        self.tableWidget.setHorizontalHeaderLabels(cols)
        for count, _data in enumerate(all_data):
            self.tableWidget.setItem(count, 0, QTableWidgetItem(str(_data[cols[0]])))
            self.tableWidget.setItem(count, 1, QTableWidgetItem(str(_data[cols[1]])))
            self.tableWidget.setItem(count, 2, QTableWidgetItem(str(_data[cols[2]])))
            self.tableWidget.setItem(count, 3, QTableWidgetItem(str(_data[cols[3]])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainForm()
    sys.exit(app.exec_())
