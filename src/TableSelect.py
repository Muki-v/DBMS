
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from src.D_Select import Ui_Dialog as Dialog
from src.TableShow import tableShow
import re
from copy import deepcopy

class tableSelect(QtWidgets.QDialog):
    def __init__(self, table_index, db, parent=None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.ui = Dialog()
        self.ui.setupUi(self)
        self.db = db
        self.cur_index = table_index
        self.ui.pushButton_s_ok.clicked.connect(self.selectInfo)
        self.ui.lineEdit_s_tableName.setText(self.cur_index)

    def selectInfo(self):
        target_context = self.ui.lineEdit_s_values.text()
        target_table = self.ui.lineEdit_s_tableName.text()

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

        context_list = re.split(', +|,+| +|\*|\n', target_context)
        # print(context_list)
        result_list = deepcopy(self.db[target_table])
        for form in context_list:
            form_list = self.do_understand_form(form)
            if result_list:
                result_list = self.do_select(form_list, result_list)
            else:
                return 0
        self.result_display(result_list)

    def do_understand_form(self, form):
        form_list = re.split('>=|<=|>|<|=', form)
        # split the form into 3 parts,  target, operator and requirements
        if ">=" in form:
            form_list = form.split(">=")
            form_list.append(">=")
        elif "<=" in form:
            form_list = form.split("<=")
            form_list.append("<=")
        elif ">" in form:
            form_list = form.split(">")
            form_list.append(">")
        elif "<" in form:
            form_list = form.split("<")
            form_list.append("<")
        elif "=" in form:
            form_list = form.split("=")
            form_list.append("=")
        else:
            return []
        return form_list

    def do_select(self, form_list, input_list):
        if len(form_list)<3:
            return None
        target = form_list[0]
        value = form_list[1]
        operator = form_list[2]
        result_list = []
        try:
            pos = input_list[0].index(target)
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Index Not Found")
            # msg.setInformativeText("Missing table name.")
            msg.setWindowTitle("Value Error")
            print(msg.exec_())
            return None
        if operator == ">=":
            for row in input_list[1:]:
                if row[pos] >= value:
                    result_list.append(row)
        elif operator == "<=":
            for row in input_list[1:]:
                if row[pos] <= value:
                    result_list.append(row)
        elif operator == ">":
            for row in input_list[1:]:
                if row[pos] > value:
                    result_list.append(row)
        elif operator == "<":
            for row in input_list[1:]:
                if row[pos] < value:
                    result_list.append(row)
        elif operator == "=":
            for row in input_list[1:]:
                if row[pos] == value:
                    result_list.append(row)
        # print(result_list)
        result_list.insert(0, input_list[0])
        # print(self.db)
        return result_list

    def result_display(self, result_list):
        page = tableShow(result_list)
        print(page.exec_())
        print(page.result() == QtWidgets.QDialog.Accepted)

