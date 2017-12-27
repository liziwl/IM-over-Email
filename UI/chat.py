from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 620)
        MainWindow.setMinimumSize(QtCore.QSize(960, 620))
        MainWindow.setMaximumSize(QtCore.QSize(960, 620))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 10, 250, 600))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 170, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.text_display_widget = QtWidgets.QWidget(self.centralwidget)
        self.text_display_widget.setGeometry(QtCore.QRect(270, 10, 680, 510))
        self.text_display_widget.setObjectName("text_display_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.text_display_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.friend_name_label = QtWidgets.QLabel(self.text_display_widget)
        self.friend_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.friend_name_label.setObjectName("friend_name_label")
        self.verticalLayout.addWidget(self.friend_name_label)

        self.textBrowser = QtWidgets.QTextBrowser(self.text_display_widget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(270, 530, 590, 80))
        self.textEdit.setObjectName("textEdit")
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(870, 530, 80, 80))
        self.send_button.setObjectName("send_button")
        self.send_button.clicked.connect(MainWindow.send_mess)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 80, 210, 470))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.new_group_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_group_button.setGeometry(QtCore.QRect(35, 560, 200, 35))
        self.new_group_button.setObjectName("new_group_button")
        self.new_group_button.clicked.connect(MainWindow.new_group)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)

        font12 = QtGui.QFont()
        font12.setFamily("等线")
        font12.setPointSize(12)

        font16 = QtGui.QFont()
        font16.setFamily("等线")
        font16.setPointSize(16)

        MainWindow.setWindowTitle("ChatRoom")
        self.label.setText("Friends")
        self.label.setFont(font16)
        self.friend_name_label.setText("Friend name")
        self.friend_name_label.setFont(font16)
        self.send_button.setText("Send")
        self.send_button.setFont(font12)
        self.new_group_button.setText("Create new group")
        self.new_group_button.setFont(font12)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)



class chatwin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.map_ui = Ui_MainWindow()  # The name of my top level object is MainWindow
        self.map_ui.setupUi(self)

    def send_mess(self):
        print("click")
        pass

    def new_group(self):
        print("click2")
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = chatwin()
    ex.show()
    sys.exit(app.exec_())
