# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.add_contact import *
from UI.chat_log import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Email.MessageService import *
import sys
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 620)
        MainWindow.setMinimumSize(QtCore.QSize(960, 620))
        MainWindow.setMaximumSize(QtCore.QSize(960, 620))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.contact_label = QtWidgets.QLabel(self.centralwidget)
        self.contact_label.setGeometry(QtCore.QRect(50, 30, 170, 30))
        self.contact_label.setAlignment(QtCore.Qt.AlignCenter)
        self.contact_label.setObjectName("label_q")
        self.text_display_widget = QtWidgets.QWidget(self.centralwidget)
        self.text_display_widget.setGeometry(QtCore.QRect(270, 10, 680, 510))
        self.text_display_widget.setObjectName("text_display_widget")
        self.right_verticalLayout = QtWidgets.QVBoxLayout(self.text_display_widget)
        self.right_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.right_verticalLayout.setObjectName("right_verticalLayout")
        self.friend_name_label = QtWidgets.QLabel(self.text_display_widget)
        self.friend_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.friend_name_label.setObjectName("friend_name_label")
        self.right_verticalLayout.addWidget(self.friend_name_label)

        self.textBrowser = QtWidgets.QTextBrowser(self.text_display_widget)
        self.textBrowser.setObjectName("textBrowser")
        self.right_verticalLayout.addWidget(self.textBrowser)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(270, 530, 560, 80))
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)  # 自动换行
        self.textEdit.setObjectName("textEdit")

        send_fig = QtGui.QIcon()
        send_fig.addPixmap(QtGui.QPixmap('resource\\send.png').scaledToHeight(80, QtCore.Qt.SmoothTransformation),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(870, 530, 80, 80))
        self.send_button.setIcon(send_fig)
        self.send_button.setObjectName("send_button")
        self.send_button.clicked.connect(MainWindow.send_mess)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        up_fig = QtGui.QIcon()
        up_fig.addPixmap(QtGui.QPixmap('resource\\up_fig.png').scaledToHeight(30, QtCore.Qt.SmoothTransformation),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_pic_button = QtWidgets.QPushButton(self.centralwidget)
        self.up_pic_button.setGeometry(QtCore.QRect(830, 530, 40, 40))
        self.up_pic_button.setIcon(up_fig)
        self.up_pic_button.setObjectName("up_pic_button")
        self.up_pic_button.clicked.connect(MainWindow.send_pic)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        up_file = QtGui.QIcon()
        up_file.addPixmap(QtGui.QPixmap('resource\\up_file.png').scaledToHeight(30, QtCore.Qt.SmoothTransformation),
                          QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.up_file_button.setGeometry(QtCore.QRect(830, 570, 40, 40))
        self.up_file_button.setIcon(up_file)
        self.up_file_button.setObjectName("up_file_button")
        self.up_file_button.clicked.connect(MainWindow.send_file)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.left_verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.left_verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 250, 600))
        self.left_verticalLayoutWidget.setObjectName("left_verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.left_verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contact_label = QtWidgets.QLabel(self.left_verticalLayoutWidget)
        self.contact_label.setAlignment(QtCore.Qt.AlignCenter)
        self.contact_label.setObjectName("contact_label")
        self.verticalLayout_2.addWidget(self.contact_label)

        self.listWidget = QtWidgets.QListWidget(self.left_verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(MainWindow.switch_contact)
        self.verticalLayout_2.addWidget(self.listWidget)

        self.new_contact_button = QtWidgets.QPushButton(self.left_verticalLayoutWidget)
        self.new_contact_button.setObjectName("new_contact_button")
        self.verticalLayout_2.addWidget(self.new_contact_button)
        self.new_contact_button.clicked.connect(MainWindow.new_contact)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)

        font10 = QtGui.QFont()
        font10.setFamily("等线")
        font10.setPointSize(10)

        font12 = QtGui.QFont()
        font12.setFamily("等线")
        font12.setPointSize(12)

        font16 = QtGui.QFont()
        font16.setFamily("等线")
        font16.setPointSize(16)

        MainWindow.setWindowTitle("ChatRoom")
        self.contact_label.setText("Friends")
        self.contact_label.setFont(font16)
        self.listWidget.setFont(font12)
        self.new_contact_button.setText("Create new contact")
        self.new_contact_button.setFont(font12)

        self.friend_name_label.setText("Friend name")
        self.friend_name_label.setFont(font16)
        self.textBrowser.setFont(font10)
        self.textEdit.setFont(font12)
        self.send_button.setText("Send")
        self.send_button.setFont(font12)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource\\chat.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)


class chatwin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.map_ui = Ui_MainWindow()  # The name of my top level object is MainWindow
        self.map_ui.setupUi(self)
        self.add_win = add_contact_win()
        self.messgae_handler = None
        self.contacts_log = {}

    def set_message_handler(self, handler):
        self.messgae_handler = handler
        self.messgae_handler.send_message(['pengym_111@163.com'], 'hello2', ['..\\Email\\lenna.jpeg'])
        re = self.messgae_handler.get_unseen_message('INBOX')
        print(re)
        print(self.messgae_handler.get_all_conversion(['pengym_111@163.com']))

    def new_contact(self):
        if self.add_win.exec_():
            user = self.add_win.get_newcontact()
            self.contacts_log[user] = Chat_log(user)
            print("add new user", user)
            new_user = QListWidgetItem(user)
            self.map_ui.listWidget.insertItem(0, new_user)
            self.map_ui.listWidget.setCurrentItem(new_user)

    def switch_contact(self):
        contact = self.map_ui.listWidget.currentItem().text()
        print(contact, self.contacts_log[contact].log_toString())
        self.map_ui.textBrowser.setText(self.contacts_log[contact].log_toString())

    def send_mess(self):
        text = self.map_ui.textEdit.toPlainText()
        now = time.localtime()
        dt = time.strftime("%Y-%m-%d %H:%M:%S", now)
        self.map_ui.textBrowser.append(dt)
        self.map_ui.textBrowser.append(text)

        contact = self.map_ui.listWidget.currentItem().text()
        self.contacts_log[contact].add_log(text, dt)

        print(dt)
        print(text)
        self.map_ui.textEdit.clear()

    def send_pic(self):
        pic_path = QFileDialog.getOpenFileName(self, 'Open Image', 'C:\\Users', "Image Files (*.png *.jpg *.bmp)")
        print(pic_path)
        return pic_path[0]

    def send_file(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open File', 'C:\\Users')
        print(file_path)
        return file_path[0]

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return and (event.modifiers() == QtCore.Qt.ControlModifier):
            self.send_mess()
        else:
            super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = chatwin()
    # ex.set_message_handler(MessageService(user_config))
    ex.show()
    sys.exit(app.exec_())
