# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem, QPushButton, QHeaderView

from EasyEraser import Ui_Dialog


class EasyEraserMainDialog(QDialog):
    root_path = '/'

    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.dir_text.setPlainText('/opt')
        self.ui.file_table.setRowCount(10)
        self.ui.file_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.ui.file_table.setColumnWidth(0, 650)
        # self.ui.file_table.setColumnWidth(1, 200)
        # self.ui.file_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

    def search_file(self):
        search_dir = self.ui.dir_text.toPlainText()
        search_file = self.ui.file_text.toPlainText()
        if not search_file:
            QMessageBox.information(self, '搜索结果提示框', '请输入文件名', QMessageBox.Yes)
            return

        has_file_flag = False
        counter = 0
        for parent, _, files in os.walk(search_dir):
            for file_ in files:
                if search_file in file_:
                    has_file_flag = True
                    _file_path = QTableWidgetItem(str(Path(parent).joinpath(file_)))
                    self.ui.file_table.setItem(counter, 0, _file_path)
                    _rm_btn = QPushButton('删除')
                    _rm_btn.setDown(True)
                    self.ui.file_table.setCellWidget(counter, 1, _rm_btn)
                    counter += 1

        if not has_file_flag:
            msg = '在目录{}下，未找到{}文件'.format(search_dir, search_file)
            QMessageBox.information(self, '搜索结果提示框', msg, QMessageBox.Yes)
            return

    def select_dir(self):
        select_dir_path = QFileDialog.getExistingDirectory(self, self.root_path)
        if not select_dir_path:
            self.ui.dir_text.setPlainText(self.root_path)
        else:
            self.ui.dir_text.setPlainText(select_dir_path)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, '选择文件', self.root_path, "All Files(*.*)")
        if not file_name:
            self.ui.file_text.setPlainText('')
        else:

            self.ui.file_text.setPlainText(file_name)

    def delete_file(self, row_num, col_num):
        cell = self.ui.file_table.item(row_num, col_num)
        if not cell:
            return

        _file_path = cell.text()
        msg = '确定要删除{}吗？'.format(_file_path)
        result = QMessageBox.question(self, '删除确认框', msg, QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            Path(_file_path).unlink(missing_ok=True)
            self.ui.file_table.removeRow(row_num)
        return


if __name__ == '__main__':
    easy_eraser_app = QApplication(sys.argv)
    easy_eraser_dlg = EasyEraserMainDialog()
    easy_eraser_dlg.show()
    sys.exit(easy_eraser_app.exec_())
