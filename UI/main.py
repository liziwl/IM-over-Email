# -*- coding: utf-8 -*-
from Main.model.user import User
from UI.login import *
from UI.chat import *
from UI.config import *
from Email.MessageService import *
from Main.dao.main_dao import MainDao
from Main.utils import set_current_user, get_user_dir, make_user_dir, test_connection
from Main.dao.user_dao import UserDao

from Security.KeyService import KeyService
import os.path

CURRENT_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))


class Login_win(QtWidgets.QWidget, Ui_Login):
    def __init__(self):
        super(Login_win, self).__init__()
        self.setupUi(self)
        self.chat_win = chatwin()
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
            # TODO  UI 添加输入锁屏密码，然后生成uuid与数据库中uuid比对验证登陆
            # 如果帐号密码还未输入提示
            if not (account and pwd):
                if self.alert.exec_() == 0:
                    self.close()
                    return
                else:
                    return
            set_current_user(account)
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
                # 生成用户数据库
                userDao = UserDao(account, new=True)

                # 生成钥匙
                KeyService.generate_keys(account, self.user_config['lock_password'])
                # 保存用户
                # 找到lock_password的哈希值并保存，用于验证登陆
                check_lock_password = str(uuid.uuid3(uuid.NAMESPACE_DNS, self.user_config['lock_password']))
                new_user = User(
                    self.user_config['account'],
                    self.user_config['password'],
                    # self.user_config['lock_password'],
                    check_lock_password,
                    self.user_config['smtp_server'],
                    self.user_config['smtp_port'],
                    self.user_config['imap_server'],
                    self.user_config['imap_port']
                )
                if test_connection(self.user_config['account'], self.user_config['password'],
                                   self.user_config['iamp_server']):
                    self.mainDao.insert_user(new_user)
                else:
                    # TODO: show alert window here
                    pass
                # TODO add this user to contact table but not show

            # 这里已经获取了所有需要的信息，尝试登录
            # self.message_handler = MessageService(self.user_config)
            if not self.chat_win.isVisible():
                # self.chat_win.set_message_handler(self.message_handler)
                self.chat_win.set_user()
                self.chat_win.show()
                self.close()

    def init_login(self):
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
