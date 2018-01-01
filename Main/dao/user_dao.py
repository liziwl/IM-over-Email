# coding: utf-8
import sqlite3

from Main.model.contact import Contact
from Main.model.group import Group
from Main.model.message import Message


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
        if not self.is_contact_exists(contact.account):
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

    def is_contact_exists(self, account):
        c = self.conn.cursor()
        c.execute(
            "SELECT * FROM contacts "
            "WHERE account = ?", [account]
        )
        return c.fetchone() is not None

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
        if not self.is_group_exists(group_uuid):
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

    def is_group_exists(self, group_uuid):
        c = self.conn.cursor()
        c.execute(
            "SELECT * FROM groups "
            "WHERE uuid = ?", [group_uuid]
        )
        return c.fetchone() is not None

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
        return Group(group_name, members, uuid)

    def add_messages(self, message):
        c = self.conn.cursor()
        c.execute(
            "INSERT INTO messages(group_, content, date_, sender) "
            "VALUES (?, ?, ?, ?)", [(message.group, message.content, message.date, message.sender)]
        )

    def get_group_messages(self, group_uuid):
        messages = list()
        c = self.conn.cursor()
        c.execute(
            "SELECT group_, content, date_, sender FROM messages "
            "WHERE group_ = ?", [group_uuid]
        )
        for m in c.fetchall():
            messages.append(Message(m[0], m[1], [2], m[3]))
        return messages


if __name__ == '__main__':
    userDao = UserDao('pengym_111@163.com', '../test.db')
    userDao.add_group('面向对象', ('12@qq.com', '1@qq.com'))
    for group in userDao.get_groups():
        for member in group.members:
            print(member.account)

        for message in userDao.get_group_messages(group.group_uuid):
            print(message)
