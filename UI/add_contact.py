# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_add_contact_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(400, 300)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 40, 400, 32))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.name_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.name_lineEdit.setGeometry(QtCore.QRect(50, 100, 290, 32))

        self.email_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(50, 150, 290, 32))

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 240, 340, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.ok)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        font12 = QtGui.QFont()
        font12.setFamily("等线")
        font12.setPointSize(12)

        font16_b = QtGui.QFont()
        font16_b.setFamily("等线")
        font16_b.setPointSize(16)
        font16_b.setBold(True)

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add contact"))
        self.label.setText(_translate("Dialog", "Add contact"))
        self.label.setFont(font16_b)
        self.name_lineEdit.setFont(font12)
        self.email_lineEdit.setFont(font12)
        self.name_lineEdit.setPlaceholderText("Name")
        self.email_lineEdit.setPlaceholderText("Email account")
        self.buttonBox.setFont(font12)


class add_contact_win(QtWidgets.QDialog, Ui_add_contact_Dialog):
    def __init__(self):
        super().__init__()
        self.add_win = Ui_add_contact_Dialog()
        self.add_win.setupUi(self)
        self.new_contact = {}

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource\\chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def ok(self):
        self.new_contact["name"] = self.add_win.name_lineEdit.text()
        self.new_contact["email"] = self.add_win.email_lineEdit.text()
        # print(self.new_contact)
        self.accept()

    def get_newcontact(self):
        temp = self.new_contact
        self.new_contact = {}
        self.add_win.name_lineEdit.clear()
        self.add_win.email_lineEdit.clear()
        return temp


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = add_contact_win()
    ex.show()
    sys.exit(app.exec_())
