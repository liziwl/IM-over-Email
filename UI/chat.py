from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 626)
        font14 = QtGui.QFont()
        font14.setFamily("Consolas")
        font14.setPointSize(12)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 10, 256, 591))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 171, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 10, 611, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.listWidget_2 = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout.addWidget(self.listWidget_2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(300, 570, 480, 30))
        self.textEdit.setObjectName("textEdit")
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setFont(font14)
        self.send_button.setGeometry(QtCore.QRect(790, 570, 120, 30))
        self.send_button.setObjectName("send_button")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 80, 210, 470))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.new_group_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_group_button.setFont(font14)
        self.new_group_button.setGeometry(QtCore.QRect(40, 560, 200, 35))
        self.new_group_button.setObjectName("new_group_button")
        MainWindow.setCentralWidget(self.centralwidget)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt;\">Friends</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:16pt;\">Friend name</span></p></body></html>"))
        self.send_button.setText(_translate("MainWindow", "Send"))
        self.new_group_button.setText(_translate("MainWindow", "Create new group"))


class chatwin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.map_ui = Ui_MainWindow()  # The name of my top level object is MainWindow
        self.map_ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = chatwin()
    ex.show()
    sys.exit(app.exec_())
