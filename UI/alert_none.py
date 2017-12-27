# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_alert(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 150)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 110, 220, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 290, 60))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        font14 = QtGui.QFont()
        font14.setFamily("等线")
        font14.setPointSize(14)
        font14.setBold(True)
        Dialog.setWindowTitle(_translate("Dialog", "Alert"))
        self.label.setText(_translate("Dialog", "Wrong server Config."))
        self.label.setFont(font14)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")

class alert_win(QtWidgets.QDialog, Ui_alert):
    def __init__(self):
        super().__init__()
        self.con_win = Ui_alert()  # The name of my top level object is MainWindow
        self.con_win.setupUi(self)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = alert_win()
    ex.show()
    sys.exit(app.exec_())