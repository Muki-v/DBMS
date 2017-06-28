# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D_Select_Result.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(372, 288)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 40, 331, 241))
        self.widget.setObjectName("widget")
        self.tableWidget_resultDisplay = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_resultDisplay.setGeometry(QtCore.QRect(10, 10, 311, 221))
        self.tableWidget_resultDisplay.setObjectName("tableWidget_resultDisplay")
        self.tableWidget_resultDisplay.setColumnCount(0)
        self.tableWidget_resultDisplay.setRowCount(0)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(21, 14, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select Results:"))

