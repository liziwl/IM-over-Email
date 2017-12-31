# -*- coding: utf-8 -*-
from UI.login import *
from UI.chat import *
from UI.config import *
from Email.MessageService import *


class LoginUI(QtWidgets.QWidget, LoginUI):
    def __init__(self):
        super(LoginUI, self).__init__()
        self.setupUi(self)
        self.chat_win = chatwin()
        self.conf = config_win()
        self.alert = alert_win("Wrong Account or password.")

        self.user_config = {}
        self.message_handler = None

    def try_login(self):
        # 这里写授权登陆的函数
        if not self.conf.isVisible():
            account = self.account_lineEdit.text().strip()
            pwd = self.pwd_lineEdit.text().strip()
            # 如果帐号密码还未输入提示
            if not (account and pwd):
                if self.alert.exec_() == 0:
                    self.close()
                    return
                else:
                    return
            self.user_config = self.conf.user_config
            # 如果user_config服务器配置不存在，尝试配置
            if not self.user_config:
                self.try_setting()
            else:
                self.user_config["account"] = account
                self.user_config["password"] = pwd
                print(self.conf.user_config)
                # 这里已经获取了所有需要的信息，尝试登录
                # self.message_handler = MessageService(self.user_config)
                if not self.chat_win.isVisible():
                    # self.chat_win.set_message_handler(self.message_handler)
                    self.chat_win.show()
                    self.close()

    def try_setting(self):
        self.conf.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = LoginUI()
    ex.show()
    sys.exit(app.exec_())
