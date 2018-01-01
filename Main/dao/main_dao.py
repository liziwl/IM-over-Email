import sqlite3
import os.path
from Main.model.user import User


class MainDao(object):
    def __init__(self, path):
        # If main database not exists, create it with sql
        has_main_db = os.path.isfile(path)
        try:
            self.conn = sqlite3.connect(path)
            if not has_main_db:
                c = self.conn.cursor()
                c.executescript('database/user.sql')
        except Exception as e:
            print("Unable to connect to main database")
            exit(1)

    def __del__(self):
        self.conn.close()

    def is_account_exists(self, account):
        c = self.conn.cursor()
        c.execute(
            "SELECT * FROM users "
            "WHERE account = ?", [account]
        )
        return c.fetchone() is not None

    def insert_user(self, user):
        if not self.is_account_exists(user.account):
            c = self.conn.cursor()
            c.execute(
                "INSERT INTO users(account, lock_password, "
                "smtp_server, smtp_port, imap_server, imap_port) "
                "VALUES(?, ?, ?, ?, ?, ?);",
                [
                    user.account, user.lock_password,
                    user.smtp_server, user.smtp_port, user.imap_server, user.imap_port
                ]
            )
            self.conn.commit()

    def get_user_info(self, account):
        c = self.conn.cursor()
        c.execute(
            "SELECT account, lock_password, smtp_server, smtp_port, imap_server, imap_port "
            "FROM users "
            "WHERE account = ?", [account]
        )
        result = c.fetchone()
        return User(result[0], result[1], result[2], result[3], result[4], result[5])

    def verify_user(self, account, lock_password):
        c = self.conn.cursor()
        c.execute(
            "SELECT lock_password FROM users "
            "WHERE account = ?", [account]
        )
        result = c.fetchone()[0]
        return result is not None and lock_password == result


if __name__ == '__main__':
    mainDao = MainDao('../main.db')
    mainDao.insert_user(
        User('1048217874@qq.com', '123456', 'smtp.163.com', 25, 'imap.163.com', 993)
    )
    result = mainDao.get_user_info("pengym_111@163.com")
    print(result.account)
    print(mainDao.verify_user('pengym_111@163.com', '123456'))