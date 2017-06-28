"""
## Warning: This page is not used in this program.
## It only appeared in the test section.
## If you need to use this program to test this program. Need to change the Folder path in src.SystemVariable.py
## into ".\src\DBfile"

"""

import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QStandardItemModel
from src.SystemVariable import VAR
from src.TableAdd import tableAdd
from src.TableSelect import tableSelect
from src.TableUpdate import tableUpdate
from src.TableDelete import tableDelete
from os import listdir
from os import path
from src.DiskInteract import diskToMemory

from src.D_Main import Ui_MainWindow as index


class MainWindow(QtWidgets.QDialog):
    closeSignal = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.ui = index()
        self.ui.setupUi(self)
        # disable all push buttons in the beginning.
        self.ui.pushButton_Add.setDisabled(True)
        self.ui.pushButton_Delete.setDisabled(True)
        self.ui.pushButton_Search.setDisabled(True)
        self.ui.pushButton_Update.setDisabled(True)
        self.ui.pushButton_DSetShow.setDisabled(True)
        self.ui.action_FtoM.triggered.connect(self.readFile)
        self.ui.pushButton_DSetShow.clicked.connect(self.showData)
        # self.ui.pushButton_Search.clicked.connect(self.showSearch)
        self.ui.pushButton_Search.clicked.connect(self.showSearch)
        self.ui.pushButton_Add.clicked.connect(self.addRecord)
        self.ui.pushButton_Update.clicked.connect(self.showUpdate)
        self.ui.pushButton_Delete.clicked.connect(self.showDelete)
        self.ui.action_Extract.triggered.connect(self.extract)
        self.db = {}
        self.readFile()

    def readFile(self):
        try:
            cur_path = VAR.FOLDER_PATH
            # print(cur_path)
            #find all files in the current work directory. Exclude db file based on the .txt suffix
            datafiles = [f for f in listdir(cur_path) if path.isfile(path.join(cur_path, f)) and ".txt" in f]
            # print(datafiles)
            for f in datafiles:
                self.do_read_file(f) # read all files in target directory.
            # get the memory use of self.db
            size = sys.getsizeof(self.db)
            size += sum(map(sys.getsizeof, self.db.values())) + sum(map(sys.getsizeof, self.db.keys()))
            # print(size)
            # add the items to comboBox.
            for f in datafiles:
                self.ui.comboBox_DSetChoose.addItem(f.split(".")[0])
            self.ui.pushButton_DSetShow.setDisabled(False)
        except Exception as e:
            print(e)

    def do_read_file(self, filename):
        cur_path = VAR.FOLDER_PATH
        # print(sys.getsizeof(cur_path))  # get the size of a variable
        curfile = cur_path+ "\\" +filename
        # print(curfile)
        file_index = filename.split(".")[0]
         # extract the index of a datafile, use this index to store the datafile in variable "self.db"
        # print(file_index)
        f = open(curfile, 'r')
        lines = f.readlines()
        self.db[file_index] = []
        for line in lines:
            line = line.strip("\n")  # remove \n
            line = line.split()     # split based on space
            if line == []:
                continue
            # print(line)
            self.db[file_index].append(line)
        # print(self.db)

    def showData(self):
        self.ui.tableWidget_DSet.clearContents()
        cur_index = self.ui.comboBox_DSetChoose.currentText()
        # print(cur_index)
        current_context = self.db[cur_index]
        print(current_context)
        try:
            # use model to set the headerlabels of tableView
            # model = QStandardItemModel()
            # model.setHorizontalHeaderLabels(current_context[0])
            # self.ui.tableWidget_DSet.setModel(model)
            column_num = len(current_context[0])
            row_num = len(current_context)
            self.ui.tableWidget_DSet.setColumnCount(column_num)
            self.ui.tableWidget_DSet.setRowCount(row_num)
            self.ui.tableWidget_DSet.setHorizontalHeaderLabels(current_context[0])
            # set the column size of all columns to 40 ( based on obervation)
            for i in range(column_num):
                self.ui.tableWidget_DSet.setColumnWidth(i,200/column_num)

            # add all values to tableWidget
            new_current_context = current_context[1:]
            for i in range(row_num-1):
                for j in range(column_num):
                    self.ui.tableWidget_DSet.setItem(i, j, QtWidgets.QTableWidgetItem(new_current_context[i][j]))

            self.ui.pushButton_Add.setDisabled(False)
            self.ui.pushButton_Delete.setDisabled(False)
            self.ui.pushButton_Search.setDisabled(False)
            self.ui.pushButton_Update.setDisabled(False)
        except Exception as e:
            print(e)

    def addRecord(self):
        cur_index = self.ui.comboBox_DSetChoose.currentText()
        page = tableAdd(cur_index, self.db)
        print(page.exec_()) # 这两句话必须要
        print(page.result() == QtWidgets.QDialog.Accepted)
        self.showData()

    def showSearch(self):
        cur_index = self.ui.comboBox_DSetChoose.currentText()
        page =tableSelect(cur_index, self.db)
        print(page.exec_())
        print(page.result() == QtWidgets.QDialog.Accepted)

    def showUpdate(self):
        cur_index = self.ui.comboBox_DSetChoose.currentText()
        page = tableUpdate(cur_index, self.db)
        print(page.exec_())
        print(page.result() == QtWidgets.QDialog.Accepted)
        self.showData()

    def showDelete(self):
        cur_index = self.ui.comboBox_DSetChoose.currentText()
        page = tableDelete(cur_index, self.db)
        print(page.exec_())
        print(page.result() == QtWidgets.QDialog.Accepted)
        self.showData()

    def extract(self):
        dtm = diskToMemory(self.db)
        dtm.analysisTotalUsage()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainpage = MainWindow()
    print(mainpage.exec_())
    print(mainpage.result() == QtWidgets.QDialog.Accepted)
