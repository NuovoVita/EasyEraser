import sys
import time

from PyQt5 import QtCore, QtWidgets
from timeout_decorator import timeout, timeout_decorator


class WidgetGallery(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        self.table = QtWidgets.QTableWidget(10, 3)
        col_1 = QtWidgets.QTableWidgetItem("first_col")
        col_2 = QtWidgets.QTableWidgetItem("second_col")
        deleteButton = QtWidgets.QPushButton("delete_this_row")
        deleteButton.clicked.connect(self.delete_clicked)
        self.table.setItem(0, 0, col_1)
        self.table.setItem(0, 1, col_2)
        self.table.setCellWidget(0, 2, deleteButton)

        col_1 = QtWidgets.QTableWidgetItem("2first_col")
        col_2 = QtWidgets.QTableWidgetItem("2second_col")
        deleteButton = QtWidgets.QPushButton("2delete_this_row")
        deleteButton.clicked.connect(self.delete_clicked)
        self.table.setItem(1, 0, col_1)
        self.table.setItem(1, 1, col_2)
        self.table.setCellWidget(1, 2, deleteButton)
        self.mainLayout = QtWidgets.QGridLayout(self)
        self.mainLayout.addWidget(self.table)

    @QtCore.pyqtSlot()
    def delete_clicked(self):
        button = self.sender()
        if button:
            row = self.table.indexAt(button.pos()).row()
            self.table.removeRow(row)


class WidgetTableExample(object):
    @classmethod
    def run(cls):
        app = QtWidgets.QApplication(sys.argv)
        w = WidgetGallery()
        w.show()
        sys.exit(app.exec_())


class TimeoutExample(object):
    time_out = 5

    @classmethod
    @timeout(time_out)
    def worker(cls):
        print('Start')
        for index in range(1, 10):
            time.sleep(1)
            print('{} seconds have passed'.format(index))

    @classmethod
    def run(cls):
        try:
            cls.worker()
        except timeout_decorator.TimeoutError:
            print('Run TIMEOUT!!!')


if __name__ == '__main__':
    # WidgetTableExample.run()
    TimeoutExample.run()
