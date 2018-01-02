import configparser

from Main.dao.main_dao import MainDao


def get_current_user():
    mainDao = MainDao('main.db')
    parser = configparser.ConfigParser()
    parser.read("../Main/conf.ini")
    account = parser.get("user", "current_user")
    current_user = mainDao.get_user_info(account)
    return current_user


def set_current_user(account):
    parser = configparser.ConfigParser()
    parser.read("../Main/conf.ini")
    parser.set("user", "current_user", account)
    parser.write(open('../Main/conf.ini', 'w'))


if __name__ == '__main__':
    print(get_current_user())