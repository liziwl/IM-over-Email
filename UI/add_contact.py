# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_add_contact_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(400, 300)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 60, 400, 32))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(50, 100, 300, 120))
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)  # 自动换行
        self.textEdit.setObjectName("textEdit")

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 240, 340, 32))
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
        Dialog.setWindowTitle(_translate("Dialog", "Add new contact"))
        self.label.setText(_translate("Dialog", "Add new contact"))
        self.label.setFont(font14_b)
        self.textEdit.setFont(font12)
        self.textEdit.setPlaceholderText(
            "Contact Email address (Semicolon separated)\nContact_a@cs.com;\nContact_b@cs.com;")
        self.buttonBox.setFont(font12)


class add_contact_win(QtWidgets.QWidget, Ui_add_contact_Dialog):
    def __init__(self):
        super().__init__()
        self.add_win = Ui_add_contact_Dialog()
        self.add_win.setupUi(self)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource\\chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def accept(self):
        self.hide()

    def reject(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = add_contact_win()
    ex.show()
    sys.exit(app.exec_())
