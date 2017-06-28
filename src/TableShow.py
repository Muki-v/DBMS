
from PyQt5 import QtWidgets
from src.D_Select_Result import Ui_Dialog as Dialog

class tableShow(QtWidgets.QDialog):
    def __init__(self, result_list, parent=None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.ui = Dialog()
        self.ui.setupUi(self)
        self.do_showTable(result_list)

    def do_showTable(self, result_list):
        try:
            # use model to set the headerlabels of tableView
            # model.setHorizontalHeaderLabels(current_context[0])
            # self.ui.tableWidget_DSet.setModel(model)
            column_num = len(result_list[0])
            row_num = len(result_list)
            self.ui.tableWidget_resultDisplay.setColumnCount(column_num)
            self.ui.tableWidget_resultDisplay.setRowCount(row_num)
            self.ui.tableWidget_resultDisplay.setHorizontalHeaderLabels(result_list[0])
            # set the column size of all columns to 40 ( based on obervation)
            for i in range(column_num):
                self.ui.tableWidget_resultDisplay.setColumnWidth(i,200/column_num)

            # add all values to tableWidget
            for i in range(row_num):
                for j in range(column_num):
                    self.ui.tableWidget_resultDisplay.setItem(i-1, j, QtWidgets.QTableWidgetItem(result_list[i][j]))

        except Exception as e:
            print(e)