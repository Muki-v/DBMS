import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from src.SystemVariable import VAR

import re


from src.D_Insert import Ui_Dialog as Dialog


class tableAdd(QtWidgets.QDialog):
    def __init__(self, table_index, db, parent=None ):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.ui = Dialog()
        self.ui.setupUi(self)
        self.cur_index = table_index
        self.ui.pushButton_ok.clicked.connect(self.addInfo)
        self.ui.pushButton_hint.clicked.connect(self.showHint)
        self.ui.lineEdit_tableName.setText(self.cur_index)
        self.db = db

    def addInfo(self):
        target_context = self.ui.lineEdit_values.text()
        target_table = self.ui.lineEdit_tableName.text()

        if target_table == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Table Name Missing.")
            # msg.setInformativeText("Missing table name.")
            msg.setWindowTitle("Value Error")
            print(msg.exec_())
        elif target_context == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Missing Key Value.")
            # msg.setInformativeText("Missing key values in value input field")
            msg.setWindowTitle("Value Error")
            print(msg.exec_())

        context_list = re.split(',+| +|\*|\n',target_context)
        # print(context_list)
        while len(context_list) < len(self.db[target_table][0]):
            context_list.append("N/A")
        if len(context_list) > len(self.db[target_table][0]):
            context_list = context_list[:len(self.db[target_table][0])]
        self.db[target_table].append(context_list)

        self.close()

    def showHint(self):
        target_table = self.ui.lineEdit_tableName.text()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Input Format: " + str(self.db[target_table][0]))
        # msg.setInformativeText("Missing table name.")
        msg.setWindowTitle("Hint Message")

        print(msg.exec_())