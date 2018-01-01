# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(500, 340)
        Login.setMinimumSize(QtCore.QSize(500, 340))
        Login.setMaximumSize(QtCore.QSize(500, 340))

        font12 = QtGui.QFont()
        font12.setFamily("等线")
        font12.setPointSize(12)

        font16 = QtGui.QFont()
        font16.setFamily("等线")
        font16.setPointSize(16)
        self.account_lineEdit = QtWidgets.QLineEdit(Login)
        self.account_lineEdit.setGeometry(QtCore.QRect(100, 120, 290, 40))
        self.account_lineEdit.setFont(font16)
        self.account_lineEdit.setText("")
        self.account_lineEdit.setObjectName("account_lineEdit")
        self.account_lineEdit.returnPressed.connect(self.account_lineEdit.focusNextChild)

        self.pwd_lineEdit = QtWidgets.QLineEdit(Login)
        self.pwd_lineEdit.setGeometry(QtCore.QRect(100, 190, 290, 40))
        self.pwd_lineEdit.setFont(font16)
        self.pwd_lineEdit.setText("")
        self.pwd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd_lineEdit.setObjectName("pwd_lineEdit")
        self.pwd_lineEdit.returnPressed.connect(Login.try_login)

        self.login_button = QtWidgets.QPushButton(Login)
        self.login_button.setGeometry(QtCore.QRect(200, 250, 190, 40))
        self.login_button.setFont(font16)
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(Login.try_login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        self.set_button = QtWidgets.QPushButton(Login)
        self.set_button.setGeometry(QtCore.QRect(100, 250, 80, 40))
        self.set_button.setFont(font12)
        self.set_button.setObjectName("login_button")
        self.set_button.clicked.connect(Login.try_setting)
        QtCore.QMetaObject.connectSlotsByName(Login)

        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(90, 10, 380, 100))
        font36 = QtGui.QFont()
        font36.setFamily("等线")
        font36.setPointSize(36)
        font36.setBold(True)
        font36.setWeight(75)
        self.label.setFont(font36)
        self.label.setObjectName("label_q")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource\\chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        Login.setWindowTitle("Login")
        self.account_lineEdit.setPlaceholderText("Email address")
        self.login_button.setText("Login")
        self.set_button.setText("Setting")
        self.pwd_lineEdit.setPlaceholderText("Password")
        self.label.setText("Security IM")
