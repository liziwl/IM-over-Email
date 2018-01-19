# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from Main.dao.user_dao import UserDao
from Main.singleton import MagicClass
from Main import utils


class Ui_show_group_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 500)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(QtCore.QRect(50, 20, 250, 32))
        self.label.setObjectName("label")

        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(50, 60, 250, 380))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(Dialog.right_click_menu)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 450, 200, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.ok)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        font12 = QtGui.QFont()
        font12.setFamily("等线")
        font12.setPointSize(12)

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Show Group"))
        self.label.setText(_translate("Dialog", "Group Name"))
        self.label.setFont(font12)


class show_group_win(QtWidgets.QDialog, Ui_show_group_Dialog):
    def __init__(self, emails=None):
        super().__init__()
        self.show_win = Ui_show_group_Dialog()
        self.show_win.setupUi(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource\\chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.ban_fig = QtGui.QIcon()
        self.ban_fig.addPixmap(QtGui.QPixmap('resource\\ban.png').scaledToHeight(80, QtCore.Qt.SmoothTransformation),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emails = emails
        if emails is not None:
            self.set_user()

    def set_emails(self, group_name, emails):

        self.emails = emails
        self.show_win.label.setText(group_name)
        print(self.emails)

    def set_user(self):
        source = MagicClass()
        self.current_email = source.current_email
        self.userDao = source.userDao

    def load_contact(self):
        font12 = QtGui.QFont()
        font12.setFamily("等线")
        font12.setPointSize(12)

        # remove old information
        self.show_win.listWidget.clear()
        for i in range(len(self.emails)):
            item = QListWidgetItem(self.emails[i])

            if self.userDao.is_account_blocked(self.emails[i]):
                item.setIcon(self.ban_fig)
            self.show_win.listWidget.addItem(self.emails[i])

    def right_click_menu(self):
        pos = QCursor.pos()
        email = self.show_win.listWidget.currentItem().text()
        if email is not None:
            menu = QMenu()
            if self.userDao.is_account_blocked(email):
                menu.addAction("UnBlock", lambda: self.unblock_contact(email))
            else:
                menu.addAction("Block", lambda: self.block_contact(email))
            menu.exec_(pos)

    def block_contact(self, email):
        print("block user", email)
        self.userDao.block_account(email)
        self.show_win.listWidget.currentItem().setIcon(self.ban_fig)

        # TODO update contact_log

    def unblock_contact(self, email):
        print("unblock user", email)
        self.userDao.unblock_account(email)
        self.show_win.listWidget.currentItem().setIcon(QIcon())
        # TODO update contact_log

    def ok(self):
        self.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    emails = ["123@123.com", "222@222.com"]
    ex = show_group_win(emails)
    ex.show()
    sys.exit(app.exec_())
