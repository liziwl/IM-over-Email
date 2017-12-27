from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(500, 340)
        Login.setMinimumSize(QtCore.QSize(500, 340))
        Login.setMaximumSize(QtCore.QSize(500, 400))
        self.lineEdit = QtWidgets.QLineEdit(Login)
        self.lineEdit.setGeometry(QtCore.QRect(100, 120, 291, 41))

        font16 = QtGui.QFont()
        font16.setFamily("Consolas")
        font16.setPointSize(16)
        self.lineEdit.setFont(font16)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(150, 250, 191, 41))
        self.pushButton.setFont(font16)
        self.pushButton.setObjectName("send_button")
        self.lineEdit_2 = QtWidgets.QLineEdit(Login)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 190, 291, 41))
        self.lineEdit_2.setFont(font16)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(70, 10, 381, 101))
        font36 = QtGui.QFont()
        font36.setFamily("Consolas")
        font36.setPointSize(36)
        font36.setBold(True)
        font36.setWeight(75)
        self.label.setFont(font36)
        self.label.setObjectName("label")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.retranslateUi(Login)
        self.pushButton.clicked.connect(Login.try_login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.lineEdit.setPlaceholderText(_translate("Login", "Email address"))
        self.pushButton.setText(_translate("Login", "Login"))
        self.lineEdit_2.setPlaceholderText(_translate("Login", "Password"))
        self.label.setText(_translate("Login", "Security IM"))
