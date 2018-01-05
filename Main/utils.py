import configparser
import os.path
from Main.dao.main_dao import MainDao

CURRENT_DIR = os.path.dirname(__file__)


def get_current_user():
    mainDao = MainDao()
    parser = configparser.ConfigParser()
    parser.read(os.path.join(CURRENT_DIR, 'conf.ini'))
    account = parser.get("user", "current_user")
    current_user = mainDao.get_user_info(account)
    return current_user


def set_current_user(account):
    parser = configparser.ConfigParser()
    parser.read(os.path.join(CURRENT_DIR, 'conf.ini'))
    parser.set("user", "current_user", account)
    parser.write(open(os.path.join(CURRENT_DIR, 'conf.ini'), 'w'))


def make_user_dir(account):
    path = os.path.join(CURRENT_DIR, account)
    os.mkdir(path)
    return os.path.abspath(path)


def get_user_dir(account):
    path = os.path.join(CURRENT_DIR, account)
    return os.path.abspath(path)


def test_connection(account, password, imap_server):
    import imaplib
    mailbox = imaplib.IMAP4_SSL(imap_server)
    try:
        mailbox.login(account, password)
        return True
    except imaplib.IMAP4.error as e:
        return False

if __name__ == '__main__':
    print(get_current_user())
    print(get_user_dir("1048217874@qq.com"))
    print(test_connection("pengym_111@163.com", "hvwoTxJndBEi8B4G", "imap.163.com"))