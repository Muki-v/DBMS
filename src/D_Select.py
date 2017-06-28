# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D_Select.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(531, 162)
        self.widget_background = QtWidgets.QWidget(Dialog)
        self.widget_background.setGeometry(QtCore.QRect(30, 20, 481, 131))
        self.widget_background.setObjectName("widget_background")
        self.groupBox_insert = QtWidgets.QGroupBox(self.widget_background)
        self.groupBox_insert.setGeometry(QtCore.QRect(0, 0, 471, 121))
        self.groupBox_insert.setObjectName("groupBox_insert")
        self.pushButton_s_hint = QtWidgets.QPushButton(self.groupBox_insert)
        self.pushButton_s_hint.setGeometry(QtCore.QRect(90, 90, 75, 23))
        self.pushButton_s_hint.setObjectName("pushButton_s_hint")
        self.widget_inputArea_2 = QtWidgets.QWidget(self.groupBox_insert)
        self.widget_inputArea_2.setGeometry(QtCore.QRect(20, 20, 441, 51))
        self.widget_inputArea_2.setObjectName("widget_inputArea_2")
        self.lineEdit_s_values = QtWidgets.QLineEdit(self.widget_inputArea_2)
        self.lineEdit_s_values.setGeometry(QtCore.QRect(270, 20, 171, 21))
        self.lineEdit_s_values.setObjectName("lineEdit_s_values")
        self.label_3 = QtWidgets.QLabel(self.widget_inputArea_2)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_s_tableName = QtWidgets.QLineEdit(self.widget_inputArea_2)
        self.lineEdit_s_tableName.setGeometry(QtCore.QRect(120, 20, 71, 21))
        self.lineEdit_s_tableName.setObjectName("lineEdit_s_tableName")
        self.label_4 = QtWidgets.QLabel(self.widget_inputArea_2)
        self.label_4.setGeometry(QtCore.QRect(202, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_s_ok = QtWidgets.QPushButton(self.groupBox_insert)
        self.pushButton_s_ok.setGeometry(QtCore.QRect(280, 90, 75, 23))
        self.pushButton_s_ok.setObjectName("pushButton_s_ok")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_insert.setTitle(_translate("Dialog", "Select"))
        self.pushButton_s_hint.setText(_translate("Dialog", "Hint"))
        self.label_3.setText(_translate("Dialog", "SELECT FROM"))
        self.label_4.setText(_translate("Dialog", "WHERE"))
        self.pushButton_s_ok.setText(_translate("Dialog", "OK"))

