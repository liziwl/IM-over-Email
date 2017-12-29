# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.alert_none import *
import sys

config_qq = {
    "imap_server": "imap.qq.com",
    "imap_port": 993,
    "smtp_server": "smtp.qq.com",
    "smtp_port": 465
}

config_163 = {
    "imap_server": "imap.163.com",
    "imap_port": 993,
    "smtp_server": "smtp.163.com",
    "smtp_port": 25
}

config_sustech = {
    "imap_server": "imap.exmail.qq.com",
    "imap_port": 993,
    "smtp_server": "smtp.exmail.qq.com",
    "smtp_port": 465
}


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 270)

        self.alert = alert_win("Wrong server Config.")

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 230, 200, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 600, 220))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.qq_button = QtWidgets.QRadioButton(self.tab)
        self.qq_button.setGeometry(QtCore.QRect(80, 20, 145, 30))
        self.qq_button.setObjectName("qq_button")

        pic_q = QtGui.QPixmap('resource\\qq.png').scaledToHeight(150, QtCore.Qt.SmoothTransformation)
        self.label_q = QtWidgets.QLabel(self.tab)
        self.label_q.setGeometry(QtCore.QRect(20, 40, 72, 15))
        self.label_q.setObjectName("label_q")
        self.label_q.setPixmap(pic_q)
        self.label_q.resize(pic_q.width(), pic_q.height())

        self.r163_button = QtWidgets.QRadioButton(self.tab)
        self.r163_button.setGeometry(QtCore.QRect(260, 20, 145, 30))
        self.r163_button.setObjectName("r163_button")

        pic_163 = QtGui.QPixmap('resource\\163.png').scaledToHeight(150, QtCore.Qt.SmoothTransformation)
        self.label_163 = QtWidgets.QLabel(self.tab)
        self.label_163.setGeometry(QtCore.QRect(220, 40, 72, 15))
        self.label_163.setObjectName("label_163")
        self.label_163.setPixmap(pic_163)
        self.label_163.resize(pic_163.width(), pic_163.height())

        self.sustech_button = QtWidgets.QRadioButton(self.tab)
        self.sustech_button.setGeometry(QtCore.QRect(450, 20, 145, 30))
        self.sustech_button.setObjectName("sustech_button")

        pic_sus = QtGui.QPixmap('resource\\sustech.png').scaledToHeight(150, QtCore.Qt.SmoothTransformation)
        self.label_sus = QtWidgets.QLabel(self.tab)
        self.label_sus.setGeometry(QtCore.QRect(420, 40, 72, 15))
        self.label_sus.setObjectName("label_sus")
        self.label_sus.setPixmap(pic_sus)
        self.label_sus.resize(pic_sus.width(), pic_sus.height())

        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit_is = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_is.setGeometry(QtCore.QRect(30, 30, 320, 32))
        self.lineEdit_is.setObjectName("lineEdit_is")
        self.lineEdit_ss = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_ss.setGeometry(QtCore.QRect(30, 100, 320, 32))
        self.lineEdit_ss.setObjectName("lineEdit_ss")
        self.lineEdit_ip = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_ip.setGeometry(QtCore.QRect(370, 30, 150, 32))
        self.lineEdit_ip.setText("")
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.lineEdit_sp = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_sp.setGeometry(QtCore.QRect(370, 100, 150, 32))
        self.lineEdit_sp.setObjectName("lineEdit_sp")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

        font14 = QtGui.QFont()
        font14.setFamily("等线")
        font14.setPointSize(14)

        Dialog.setWindowTitle(_translate("Dialog", "Mail server Setting"))
        self.qq_button.setText(_translate("Dialog", "QQ"))
        self.r163_button.setText(_translate("Dialog", "163"))
        self.sustech_button.setText(_translate("Dialog", "SUSTech"))
        self.qq_button.setFont(font14)
        self.r163_button.setFont(font14)
        self.sustech_button.setFont(font14)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Fast setting"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Custom setting"))
        self.tabWidget.setFont(font14)

        self.lineEdit_is.setPlaceholderText(_translate("Dialog", "IMAP server"))
        self.lineEdit_ss.setPlaceholderText(_translate("Dialog", "SMTP server"))
        self.lineEdit_ip.setPlaceholderText(_translate("Dialog", "IMAP port"))
        self.lineEdit_sp.setPlaceholderText(_translate("Dialog", "SMTP port"))


class config_win(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.con_win = Ui_Dialog()  # The name of my top level object is MainWindow
        self.con_win.setupUi(self)
        self.user_config = {}

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource\\chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def accept(self):
        if self.con_win.tabWidget.currentIndex() == 0:
            if self.con_win.qq_button.isChecked():
                print("QQ is selected")
                self.user_config = config_qq
                self.close()
            elif self.con_win.r163_button.isChecked():
                print("163 is selected")
                self.user_config = config_163
                self.close()
            elif self.con_win.sustech_button.isChecked():
                print("Sustech is selected")
                self.user_config = config_sustech
                self.close()
            else:
                print("none is selected")
                if self.con_win.alert.exec_() == 0:
                    self.close()
        else:
            imap_server = self.con_win.lineEdit_is.text().strip()
            imap_port = self.con_win.lineEdit_ip.text().strip()
            smtp_server = self.con_win.lineEdit_ss.text().strip()
            smtp_port = self.con_win.lineEdit_sp.text().strip()
            # 如果为空
            if imap_server and imap_port and smtp_server and smtp_port:
                print(imap_server, ":", imap_port)
                print(smtp_server, ":", smtp_port)
                self.user_config["imap_server"] = imap_server
                self.user_config["imap_port"] = imap_port
                self.user_config["smtp_server"] = smtp_server
                self.user_config["smtp_port"] = smtp_port
                self.close()
            else:
                print("none is entered")
                if self.con_win.alert.exec_() == 0:
                    self.close()

    def reject(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = config_win()
    ex.show()
    sys.exit(app.exec_())
