# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.main import *
import sys


class Ui_unlock(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 60, 400, 32))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 140, 281, 31))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(Dialog.accept)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 340, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        font12 = QtGui.QFont()
        font12.setFamily("等线")
        font12.setPointSize(12)

        font14_b = QtGui.QFont()
        font14_b.setFamily("等线")
        font14_b.setPointSize(14)
        font14_b.setBold(True)

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Unlock"))
        self.label.setText(_translate("Dialog", "Unlock password"))
        self.label.setFont(font14_b)
        self.lineEdit.setFont(font12)
        self.buttonBox.setFont(font12)


class unlock_win(QtWidgets.QWidget, Ui_unlock):
    def __init__(self):
        super().__init__()
        self.unlo_win = Ui_unlock()
        self.login_win = LoginUI()
        self.alert = alert_win("Wrong lock password.")
        self.unlo_win.setupUi(self)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource\\chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def accept(self):
        self.authorize()

    def reject(self):
        self.close()

    def authorize(self):
        if self.unlo_win.lineEdit.text() == "123":
            self.login_win.show()
            self.close()
        else:
            if self.alert.exec_() == 0:
                self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = unlock_win()
    ex.show()
    sys.exit(app.exec_())
