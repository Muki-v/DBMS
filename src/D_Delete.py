# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D_Delete.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(526, 159)
        self.widget_background = QtWidgets.QWidget(Dialog)
        self.widget_background.setGeometry(QtCore.QRect(20, 20, 481, 131))
        self.widget_background.setObjectName("widget_background")
        self.groupBox_insert = QtWidgets.QGroupBox(self.widget_background)
        self.groupBox_insert.setGeometry(QtCore.QRect(0, 0, 471, 121))
        self.groupBox_insert.setObjectName("groupBox_insert")
        self.pushButton_d_hint = QtWidgets.QPushButton(self.groupBox_insert)
        self.pushButton_d_hint.setGeometry(QtCore.QRect(90, 90, 75, 23))
        self.pushButton_d_hint.setObjectName("pushButton_d_hint")
        self.widget_inputArea = QtWidgets.QWidget(self.groupBox_insert)
        self.widget_inputArea.setGeometry(QtCore.QRect(20, 20, 441, 51))
        self.widget_inputArea.setObjectName("widget_inputArea")
        self.lineEdit_d_values = QtWidgets.QLineEdit(self.widget_inputArea)
        self.lineEdit_d_values.setGeometry(QtCore.QRect(270, 20, 171, 21))
        self.lineEdit_d_values.setObjectName("lineEdit_d_values")
        self.label = QtWidgets.QLabel(self.widget_inputArea)
        self.label.setGeometry(QtCore.QRect(0, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_d_tableName = QtWidgets.QLineEdit(self.widget_inputArea)
        self.lineEdit_d_tableName.setGeometry(QtCore.QRect(124, 20, 71, 21))
        self.lineEdit_d_tableName.setObjectName("lineEdit_d_tableName")
        self.label_2 = QtWidgets.QLabel(self.widget_inputArea)
        self.label_2.setGeometry(QtCore.QRect(206, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_d_ok = QtWidgets.QPushButton(self.groupBox_insert)
        self.pushButton_d_ok.setGeometry(QtCore.QRect(280, 90, 75, 23))
        self.pushButton_d_ok.setObjectName("pushButton_d_ok")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_insert.setTitle(_translate("Dialog", "Delete"))
        self.pushButton_d_hint.setText(_translate("Dialog", "Hint"))
        self.label.setText(_translate("Dialog", "DELETE FROM"))
        self.label_2.setText(_translate("Dialog", "WHERE"))
        self.pushButton_d_ok.setText(_translate("Dialog", "OK"))

