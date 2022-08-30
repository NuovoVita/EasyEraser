import sys

from PyQt5 import QtCore, QtWidgets


class WidgetGallery(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        self.table = QtWidgets.QTableWidget(10, 3)
        col_1 = QtWidgets.QTableWidgetItem("first_col")
        col_2 = QtWidgets.QTableWidgetItem("second_col")
        deleteButton = QtWidgets.QPushButton("delete_this_row")
        deleteButton.clicked.connect(self.deleteClicked)
        self.table.setItem(0, 0, col_1)
        self.table.setItem(0, 1, col_2)
        self.table.setCellWidget(0, 2, deleteButton)

        col_1 = QtWidgets.QTableWidgetItem("2first_col")
        col_2 = QtWidgets.QTableWidgetItem("2second_col")
        deleteButton = QtWidgets.QPushButton("2delete_this_row")
        deleteButton.clicked.connect(self.deleteClicked)
        self.table.setItem(1, 0, col_1)
        self.table.setItem(1, 1, col_2)
        self.table.setCellWidget(1, 2, deleteButton)
        self.mainLayout = QtWidgets.QGridLayout(self)
        self.mainLayout.addWidget(self.table)

    @QtCore.pyqtSlot()
    def deleteClicked(self):
        button = self.sender()
        if button:
            row = self.table.indexAt(button.pos()).row()
            self.table.removeRow(row)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = WidgetGallery()
    w.show()
    sys.exit(app.exec_())
