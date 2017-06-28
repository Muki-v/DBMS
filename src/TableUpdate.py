from PyQt5 import QtWidgets
from src.D_Update import Ui_Dialog as Dialog
from PyQt5.QtWidgets import QMessageBox
import re
from copy import deepcopy

class tableUpdate(QtWidgets.QDialog):
    def __init__(self, table_index, db, parent=None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.ui = Dialog()
        self.ui.setupUi(self)
        self.cur_index = table_index
        self.db = db
        self.ui.lineEdit_u_tableName.setText(self.cur_index)
        self.ui.pushButton_u_ok.clicked.connect(self.updateInfo)

    def updateInfo(self):
        table_name = self.ui.lineEdit_u_tableName.text()
        forms = self.ui.lineEdit_u_requirements.text()
        if table_name == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Table Name Missing.")
            # msg.setInformativeText("Missing table name.")
            msg.setWindowTitle("Value Error")
            print(msg.exec_())
        elif forms == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Missing Key Value.")
            # msg.setInformativeText("Missing key values in value input field")
            msg.setWindowTitle("Value Error")
            print(msg.exec_())

        context_list = re.split(', +|,+| +|\*|\n', forms)
        # print(context_list)
        result_list = self.db[table_name]
        for form in context_list:
            form_list = self.do_understand_form(form)
            if result_list:
                result_list = self.do_select(form_list, result_list)
            else:
                return 0
        values = self.ui.lineEdit_u_values.text()
        values_list = re.split(', +|,+| +|\*|\n', values)
        for value in values_list:
            value_list = self.do_understand_value(value)
            self.do_set_values(result_list, value_list)
        # print(result_list)
        self.close()

    def do_understand_value(self, values):
        if "=" in values:
            value_list = re.split('=+', values)
            value_list.append("=")
            return value_list
        else:
            raise ValueError("Illegal value format")

    def do_set_values(self, choosen_list, value_list):
        print(choosen_list)
        print(value_list)
        set_index = choosen_list[0].index(value_list[0])
        for record in choosen_list[1:]:
            record[set_index] = value_list[1]
        return choosen_list

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

