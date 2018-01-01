# -*- coding: utf-8 -*-
from Main.model.user import User
from UI.login import *
from UI.chat import *
from UI.config import *
from Email.MessageService import *
from Main.dao.main_dao import MainDao
import configparser

class Login_win(QtWidgets.QWidget, Ui_Login):
    def __init__(self):
        super(Login_win, self).__init__()
        self.setupUi(self)
        self.chat_win = chatwin()
        self.conf = config_win()
        self.alert = alert_win("Wrong Account or password.")

        self.user_config = {}
        self.message_handler = None
        self.mainDao = MainDao('../Main/main.db')

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
            # 判断用户是否存在
            if not self.mainDao.is_account_exists(account):
                self.user_config = self.conf.user_config
                if not self.user_config:
                    self.try_setting()
                    return
                self.user_config["account"] = account
                self.user_config["password"] = pwd
                # TODO: get lock password
                self.user_config['lock_password'] = '123456'
                # 保存用户
                new_user = User(
                    self.user_config['account'],
                    self.user_config['lock_password'],
                    self.user_config['smtp_server'],
                    self.user_config['smtp_port'],
                    self.user_config['imap_server'],
                    self.user_config['imap_port']
                )
                self.mainDao.insert_user(new_user)
            self.set_current_user(account)
            print(self.get_current_user())
            # 这里已经获取了所有需要的信息，尝试登录
            # self.message_handler = MessageService(self.user_config)
            if not self.chat_win.isVisible():
                # self.chat_win.set_message_handler(self.message_handler)
                self.chat_win.show()
                self.close()

    def try_setting(self):
        self.conf.show()

    def get_current_user(self):
        parser = configparser.ConfigParser()
        parser.read("../Main/conf.ini")
        current_user = parser.get("user", "current_user")
        return current_user

    def set_current_user(self, account):
        parser = configparser.ConfigParser()
        parser.read("../Main/conf.ini")
        parser.set("user", "current_user", account)
        parser.write(open('../Main/conf.ini', 'w'))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Login_win()
    ex.show()
    sys.exit(app.exec_())
