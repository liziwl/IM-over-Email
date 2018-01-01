# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_create_group_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 500)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 250, 32))
        self.lineEdit.setObjectName("lineEdit")

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 60, 250, 380))
        self.tableWidget.setObjectName("tableWidget")

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 450, 200, 32))
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

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create Group"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Group Name"))
        self.lineEdit.setFont(font12)


class create_group_win(QtWidgets.QDialog, Ui_create_group_Dialog):
    def __init__(self, contacts=[]):
        super().__init__()
        self.cr_win = Ui_create_group_Dialog()
        self.cr_win.setupUi(self)
        self.contacts = contacts
        self.re_dat = {}
        self.group_member = []

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource\\chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.load_contact(contacts)

    def load_contact(self, contacts):
        font12 = QtGui.QFont()
        font12.setFamily("等线")
        font12.setPointSize(12)

        self.cr_win.tableWidget.setColumnCount(1)
        self.cr_win.tableWidget.setRowCount(len(contacts))
        for i in range(len(contacts)):
            # 行表头
            item_head = QtWidgets.QTableWidgetItem()
            item_head.setFont(font12)
            item_head.setText("{}".format(i + 1))
            self.cr_win.tableWidget.setVerticalHeaderItem(i, item_head)
            # 行数据
            item_data = QtWidgets.QTableWidgetItem()
            item_data.setFont(font12)
            item_data.setText(contacts[i])
            item_data.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item_data.setCheckState(QtCore.Qt.Unchecked)
            self.cr_win.tableWidget.setItem(i, 0, item_data)
        # 列表头
        item_head = QtWidgets.QTableWidgetItem()
        item_head.setFont(font12)
        item_head.setText("Name")
        self.cr_win.tableWidget.setHorizontalHeaderItem(0, item_head)
        self.cr_win.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.cr_win.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

    def ok(self):
        row_num = self.cr_win.tableWidget.rowCount()
        for i in range(row_num):
            item_data = self.cr_win.tableWidget.item(i, 0)
            if item_data.checkState() == QtCore.Qt.Checked:
                self.group_member.append(contacts[i])
        self.re_dat["name"] = self.cr_win.lineEdit.text()
        self.re_dat["group"] = self.group_member
        print(self.re_dat)
        self.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    contacts = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    ex = create_group_win(contacts)
    ex.show()
    sys.exit(app.exec_())
