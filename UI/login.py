from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(500, 340)
        Login.setMinimumSize(QtCore.QSize(500, 340))
        Login.setMaximumSize(QtCore.QSize(500, 340))
        self.account_lineEdit = QtWidgets.QLineEdit(Login)
        self.account_lineEdit.setGeometry(QtCore.QRect(100, 120, 290, 40))

        font16 = QtGui.QFont()
        font16.setFamily("等线")
        font16.setPointSize(16)
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

        self.pushButton = QtWidgets.QPushButton(Login)
        self.pushButton.setGeometry(QtCore.QRect(150, 250, 190, 40))
        self.pushButton.setFont(font16)
        self.pushButton.setObjectName("send_button")

        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(90, 10, 380, 100))
        font36 = QtGui.QFont()
        font36.setFamily("等线")
        font36.setPointSize(36)
        font36.setBold(True)
        font36.setWeight(75)
        self.label.setFont(font36)
        self.label.setObjectName("label")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.pushButton.clicked.connect(Login.try_login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        Login.setWindowTitle("Login")
        self.account_lineEdit.setPlaceholderText("Email address")
        self.pushButton.setText("Login")
        self.pwd_lineEdit.setPlaceholderText("Password")
        self.label.setText("Security IM")