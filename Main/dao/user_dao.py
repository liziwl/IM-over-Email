# coding: utf-8
import sqlite3

from Main.model.contact import Contact
from Main.model.group import Group
from Main.model.message import Message
from Main.utils import get_current_user, get_user_dir
import os


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


class UserDao(object):
    def __init__(self, account, new=False):
        self.account = account
        self.conn = None
        database_path = os.path.join(get_user_dir(self.account), 'user.db')
        print(database_path)
        try:
            self.conn = sqlite3.connect(database_path)
            if new:
                current_dir = os.path.dirname(__file__)
                script_path = os.path.join(current_dir, 'user.sql')
                c = self.conn.cursor()
                with open(script_path) as f:
                    c.executescript(f.read())
        except Exception as e:
            print(e)
            print('Unable to connect to user database')
            exit(1)

    def add_contact(self, contact):
        if not self.is_contact_exists(contact.account):
            c = self.conn.cursor()
            c.execute(
                "INSERT INTO contacts(name, account, public_key, trusted, is_blocked) "
                "VALUES(?, ?, ?, ?, ?)",
                [
                    contact.name,
                    contact.account,
                    contact.public_key,
                    contact.trusted,
                    contact.is_blocked
                ])
            self.conn.commit()

    def remove_contact(self, account):
        if self.is_contact_exists(account):
            c = self.conn.cursor()
            c.execute(
                "DELETE FROM contacts "
                "WHERE account = ?", [account]
            )
            self.conn.commit()

    def change_contact_block_state(self, account):
        if self.is_contact_exists(account):
            c = self.conn.cursor()
            c.execute(
                "UPDATE contacts "
                "SET is_blocked = (CASE is_blocked WHEN 1 THEN 0 WHEN 0 THEN 1 END) "
                "WHERE account = ?", [account]
            )
            self.conn.commit()

    def get_contacts(self):
        c = self.conn.cursor()
        c.execute(
            "SELECT name, account, public_key, trusted, is_blocked FROM contacts"
        )
        return [
            Contact(r[0], r[1], r[2], r[3] == 1, r[4] == 1) for r in c.fetchall()
        ]

    def is_contact_exists(self, account):
        c = self.conn.cursor()
        c.execute(
            "SELECT * FROM contacts "
            "WHERE account = ?", [account]
        )
        return c.fetchone() is not None

    # TODO group: let group represent dialog message.group :=uuid
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
            if len(accounts) > 1:
                accounts_str = '(' + ','.join(['"' + s + '"' for s in accounts]) + ')'
                c.execute(
                    "INSERT INTO member_in_group(member_id, group_id) "
                    "SELECT id, ? FROM contacts "
                    "WHERE account IN %s" % accounts_str, [group_uuid]
                )
            elif len(accounts) == 1:
                new_member_account = accounts[0]
                print(new_member_account)
                c.execute(
                    "INSERT INTO member_in_group(member_id, group_id) "
                    "SELECT id, ? FROM contacts "
                    "WHERE account = ?", [group_uuid, new_member_account]
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
            "WHERE uuid = ? ", [uuid]
        )
        group_name = c.fetchone()[0]
        c = self.conn.cursor()
        c.execute(
            "SELECT name, account, public_key, trusted, is_blocked FROM contacts "
            "INNER JOIN "
            "(SELECT member_id FROM member_in_group "
            "WHERE group_id = ?) AS member_ids "
            "ON contacts.id = member_ids.member_id", [uuid]
        )
        members = [
            Contact(r[0], r[1], r[2], r[3] == 1, r[4] == 1) for r in c.fetchall()
        ]
        return Group(group_name, members, uuid)

    def add_messages(self, message):
        c = self.conn.cursor()
        c.execute(
            "INSERT INTO messages(group_, content, date_, sender) "
            "VALUES (?, ?, ?, ?)", [message.group, message.content, message.date, message.sender]
        )
        self.conn.commit()

    def get_group_messages(self, group_uuid):
        messages = list()
        c = self.conn.cursor()
        c.execute(
            "SELECT group_, content, date_, sender FROM messages "
            "WHERE group_ = ? "
            "ORDER BY date_"
            , [group_uuid]
        )
        for m in c.fetchall():
            messages.append(Message(m[0], m[1], m[2], m[3]))
        return messages


if __name__ == '__main__':
    userDao = UserDao()
    userDao.add_group('面向对象', ('12@qq.com', '1@qq.com'))
    # userDao.add_contact(Contact("John", "John@outlook.com", "123456", True, True))
    # for group in userDao.get_groups():
    #     for member in group.members:
    #         print(member.account)
    #
    #     for message in userDao.get_group_messages(group.group_uuid):
    #         print(message)
    userDao.change_contact_block_state("John@outlook.com")
    userDao.remove_contact('John@outlook.com')
