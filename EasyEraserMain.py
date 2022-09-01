# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox, QTableWidgetItem, QHeaderView
from timeout_decorator import timeout, timeout_decorator

from EasyEraser import Ui_Dialog


class EasyEraserMainDialog(QDialog):
    root_path = '/'
    max_timeout = 30

    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.file_table.setRowCount(10)
        self.ui.file_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.ui.file_table.setColumnWidth(0, 650)
        # self.ui.file_table.setColumnWidth(1, 200)
        # self.ui.file_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

    @timeout(max_timeout)
    def _find_all_files(self, find_dir, find_file):
        find_file_lst = []
        for parent, _, files in os.walk(find_dir):
            for file_ in files:
                if find_file in file_:
                    _file_path = QTableWidgetItem(str(Path(parent).joinpath(file_)))
                    find_file_lst.append(_file_path)
                    self.ui.file_table.setItem(len(find_file_lst) - 1, 0, _file_path)
                    # _rm_btn = QPushButton('删除')
                    # _rm_btn.setDown(True)
                    # self.ui.file_table.setCellWidget(counter, 1, _rm_btn)
        return find_file_lst

    def search_file(self):
        search_dir = self.ui.dir_text.toPlainText()
        if not search_dir:
            QMessageBox.information(self, '搜索结果提示框', '请输入文件路径', QMessageBox.Yes)
            return

        search_file = self.ui.file_text.toPlainText()
        if not search_file:
            QMessageBox.information(self, '搜索结果提示框', '请输入文件名', QMessageBox.Yes)
            return

        try:
            result = self._find_all_files(search_dir, search_file)
            if not result:
                msg = '在目录“{}”下未找到“{}”文件'.format(search_dir, search_file)
                QMessageBox.information(self, '搜索结果提示框', msg, QMessageBox.Yes)
                return
        except timeout_decorator.TimeoutError:
            msg = '在目录“{}”下搜索文件“{}”超时，请重新搜索'.format(search_dir, search_file)
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
        msg = '确定要擦除“{}”吗？'.format(_file_path)
        result = QMessageBox.question(self, '擦除确认框', msg, QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            try:
                if Path(_file_path).is_file():
                    Path(_file_path).unlink()
                self.ui.file_table.removeRow(row_num)
            except Exception as e:
                print(e)
        return


if __name__ == '__main__':
    easy_eraser_app = QApplication(sys.argv)
    easy_eraser_dlg = EasyEraserMainDialog()
    easy_eraser_dlg.show()
    sys.exit(easy_eraser_app.exec_())
