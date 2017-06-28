# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D_Update.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(532, 204)
        self.widget_background = QtWidgets.QWidget(Dialog)
        self.widget_background.setGeometry(QtCore.QRect(30, 20, 481, 171))
        self.widget_background.setObjectName("widget_background")
        self.groupBox_insert = QtWidgets.QGroupBox(self.widget_background)
        self.groupBox_insert.setGeometry(QtCore.QRect(0, 0, 471, 161))
        self.groupBox_insert.setObjectName("groupBox_insert")
        self.pushButton_u_hint = QtWidgets.QPushButton(self.groupBox_insert)
        self.pushButton_u_hint.setGeometry(QtCore.QRect(90, 120, 75, 23))
        self.pushButton_u_hint.setObjectName("pushButton_u_hint")
        self.widget_inputArea_3 = QtWidgets.QWidget(self.groupBox_insert)
        self.widget_inputArea_3.setGeometry(QtCore.QRect(20, 20, 441, 81))
        self.widget_inputArea_3.setObjectName("widget_inputArea_3")
        self.lineEdit_u_values = QtWidgets.QLineEdit(self.widget_inputArea_3)
        self.lineEdit_u_values.setGeometry(QtCore.QRect(210, 20, 201, 21))
        self.lineEdit_u_values.setObjectName("lineEdit_u_values")
        self.label_5 = QtWidgets.QLabel(self.widget_inputArea_3)
        self.label_5.setGeometry(QtCore.QRect(0, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_u_tableName = QtWidgets.QLineEdit(self.widget_inputArea_3)
        self.lineEdit_u_tableName.setGeometry(QtCore.QRect(70, 20, 71, 21))
        self.lineEdit_u_tableName.setObjectName("lineEdit_u_tableName")
        self.label_6 = QtWidgets.QLabel(self.widget_inputArea_3)
        self.label_6.setGeometry(QtCore.QRect(160, 20, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_inputArea_3)
        self.label_7.setGeometry(QtCore.QRect(0, 50, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_u_requirements = QtWidgets.QLineEdit(self.widget_inputArea_3)
        self.lineEdit_u_requirements.setGeometry(QtCore.QRect(70, 50, 341, 21))
        self.lineEdit_u_requirements.setObjectName("lineEdit_u_requirements")
        self.pushButton_u_ok = QtWidgets.QPushButton(self.groupBox_insert)
        self.pushButton_u_ok.setGeometry(QtCore.QRect(280, 120, 75, 23))
        self.pushButton_u_ok.setObjectName("pushButton_u_ok")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_insert.setTitle(_translate("Dialog", "Update"))
        self.pushButton_u_hint.setText(_translate("Dialog", "Hint"))
        self.label_5.setText(_translate("Dialog", "UPDATE"))
        self.label_6.setText(_translate("Dialog", "SET"))
        self.label_7.setText(_translate("Dialog", "WHERE"))
        self.pushButton_u_ok.setText(_translate("Dialog", "OK"))

