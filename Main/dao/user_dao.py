# coding: utf-8
import sqlite3

from Main.model.contact import Contact
from Main.model.group import Group


class UserDao(object):
    def __init__(self, account, database_path):
        self.account = account
        try:
            self.conn = sqlite3.connect(database_path)
        except Exception as e:
            print('Unable to connect to user database')
            exit(1)

    def __del__(self):
        self.conn.close()

    def add_contact(self, contact):
        c = self.conn.cursor()
        c.execute(
            "INSERT INTO contacts(name, account, public_key, trusted) "
            "VALUES(?, ?, ?, ?)",
            [
                contact.name,
                contact.account,
                contact.public_key,
                contact.trusted
            ])
        self.conn.commit()

    def get_contacts(self):
        c = self.conn.cursor()
        c.execute(
            "SELECT name, account, public_key, trusted FROM contacts"
        )
        return [
           Contact(r[0], r[1], r[2], r[3] == 1) for r in c.fetchall()
        ]

    def get_groups(self):
        c = self.conn.cursor()
        c.execute(
            "SELECT uuid FROM groups"
        )
        result = list()
        for r in c.fetchall():
            uuid = r[0]
            result.append(self.get_group(uuid))
        return result

    def add_group(self, group_name, accounts):
        import uuid
        c = self.conn.cursor()
        accounts_name = [account for account in accounts]
        accounts_name.append(self.account)
        accounts_name = sorted(accounts_name)
        names = ''
        for name in accounts_name:
            names = name + names
        group_uuid = str(uuid.uuid3(uuid.NAMESPACE_DNS, names))
        c.execute(
            "INSERT INTO groups(name, uuid) "
            "VALUES (?, ?)", [group_name, group_uuid]
        )
        c.execute(
            "INSERT INTO member_in_group(member_id, group_id) "
            "SELECT id, ? FROM contacts "
            "WHERE account IN %s" % str(accounts), [group_uuid]
        )
        self.conn.commit()

    def get_group(self, uuid):
        c = self.conn.cursor()
        c.execute(
            "SELECT name FROM groups "
            "WHERE uuid = ?", [uuid]
        )
        group_name = c.fetchone()[0]
        c = self.conn.cursor()
        c.execute(
            "SELECT name, account, public_key, trusted FROM contacts "
            "INNER JOIN "
            "(SELECT member_id FROM member_in_group "
            "WHERE group_id = ?) AS member_ids "
            "ON contacts.id = member_ids.member_id", [uuid]
        )
        members = [
           Contact(r[0], r[1], r[2], r[3] == 1) for r in c.fetchall()
        ]
        return Group(group_name, members)


if __name__ == '__main__':
    userDao = UserDao('pengym_111@163.com', '../test.db')
    # userDao.add_group('面向对象讨论组', ('12@qq.com', '1@qq.com'))
    for group in userDao.get_groups():
        for member in group.members:
            print(member.account)
