# -*- coding: utf-8 -*-
from UI.login import *
from UI.chat import *
from UI.config import *


class loginwin(QtWidgets.QWidget, Ui_Login):
    def __init__(self):
        super(loginwin, self).__init__()
        self.setupUi(self)
        self.chat_win = chatwin()
        self.conf = config_win()

    def try_login(self):
        # 这里写授权登陆的函数
        account = self.account_lineEdit.text()
        pwd = self.pwd_lineEdit.text()
        print(account, pwd)
        if not self.chat_win.isVisible():
            self.chat_win.show()
            self.close()

    def try_setting(self):
        print(self.conf.exec_())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = loginwin()
    ex.show()
    sys.exit(app.exec_())
