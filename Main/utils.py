import configparser
def get_current_user():
    parser = configparser.ConfigParser()
    parser.read("../Main/conf.ini")
    current_user = parser.get("user", "current_user")
    return current_user


def set_current_user(account):
    parser = configparser.ConfigParser()
    parser.read("../Main/conf.ini")
    parser.set("user", "current_user", account)
    parser.write(open('../Main/conf.ini', 'w'))