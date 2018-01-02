# -*- coding: utf-8 -*-
from Main.model.user import User
from UI.login import *
from UI.chat import *
from UI.config import *
from Email.MessageService import *
from Main.dao.main_dao import MainDao
from Main.utils import set_current_user, get_user_dir, make_user_dir
from Main.dao.user_dao import UserDao

from Security.KeyService import KeyService
import os.path

CURRENT_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))


class Login_win(QtWidgets.QWidget, Ui_Login):
    def __init__(self):
        super(Login_win, self).__init__()
        self.setupUi(self)
        self.chat_win = None
        self.conf = config_win()
        self.alert = alert_win("Wrong Account or password.")

        self.user_config = {}
        self.message_handler = None
        self.mainDao = MainDao()

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
                # TODO: set lock password
                self.user_config['lock_password'] = '123456'
                # 生成用户目录
                make_user_dir(account)
                # 生成钥匙
                KeyService.generate_keys(account, self.user_config['lock_password'])
                # 生成用户数据库
                userDao = UserDao(new=True)
                # 保存用户
                new_user = User(
                    self.user_config['account'],
                    self.user_config['password'],
                    self.user_config['lock_password'],
                    self.user_config['smtp_server'],
                    self.user_config['smtp_port'],
                    self.user_config['imap_server'],
                    self.user_config['imap_port']
                )
                self.mainDao.insert_user(new_user)
            set_current_user(account)
            # 这里已经获取了所有需要的信息，尝试登录
            # self.message_handler = MessageService(self.user_config)
            self.init_login()

    def init_login(self):
        self.chat_win = chatwin()
        if not self.chat_win.isVisible():
            # self.chat_win.set_message_handler(self.message_handler)
            self.chat_win.show()
            self.close()

    def try_setting(self):
        self.conf.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Login_win()
    ex.show()
    sys.exit(app.exec_())
