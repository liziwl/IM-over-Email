# coding: utf-8
import sqlite3

from Main.model.contact import Contact
from Main.model.group import Group
from Main.model.message import Message
from Main.utils import get_user_dir
from Main import utils
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
            self.conn = sqlite3.connect(database_path, check_same_thread=False)
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
        c = self.conn.cursor()
        group_uuid = utils.get_uuid(accounts)
        if not self.is_group_exists(group_uuid):
            c.execute(
                "INSERT INTO groups(name, uuid) "
                "VALUES (?, ?)", [group_name, group_uuid]
            )
            c.executemany(
                "INSERT INTO member_in_group(group_id, account) "
                "VALUES (?, ?)", [(group_uuid, account) for account in accounts]
            )
            self.conn.commit()

    def is_group_exists(self, group_uuid):
        c = self.conn.cursor()
        c.execute(
            "SELECT * FROM groups "
            "WHERE uuid = ?", [group_uuid]
        )
        return c.fetchone() is not None

    def get_group(self, group_uuid):
        c = self.conn.cursor()
        c.execute(
            "SELECT name FROM groups "
            "WHERE uuid = ? ", [group_uuid]
        )
        group_name = c.fetchone()[0]
        c = self.conn.cursor()
        c.execute(
            "SELECT account FROM member_in_group "
            "WHERE group_id = ?", [group_uuid]
        )
        members = [
            a[0] for a in c.fetchall()
        ]
        return Group(group_name, members, group_uuid)

    def add_messages(self, message):
        c = self.conn.cursor()
        c.execute(
            "INSERT INTO messages(group_, content, date_, sender) "
            "VALUES (?, ?, ?, ?)", [message.group, message.content, message.date, message.sender]
        )
        for buff in message.attachments:
            c.execute(
                "INSERT INTO attachments(message_id, content) "
                "SELECT id, ? FROM messages "
                "WHERE group_ = ? "
                "AND content = ?", [memoryview(buff), message.group, message.content]
            )
        self.conn.commit()

    def get_group_messages(self, group_uuid):
        from copy import deepcopy
        messages = list()
        # get body
        c = self.conn.cursor()
        c.execute(
            "SELECT id, group_, content, date_, sender FROM messages "
            "WHERE group_ = ? "
            "ORDER BY date_"
            , [group_uuid]
        )
        msg_body = deepcopy(c.fetchall())

        # get attachments
        c = self.conn.cursor()
        c.execute(
            "SELECT message_id, content FROM attachments "
        )
        # message_id 到 attachment buffer list的map
        attachment_map = {}
        for a in c.fetchall():
            message_id = a[0]
            buff = a[1]
            if message_id not in attachment_map:
                attachment_map[message_id] = list()
            attachment_map[message_id].append(buff)

        for m in msg_body:
            message_id = m[0]
            messages.append(Message(m[1], m[2], m[3], m[4], attachments=attachment_map.get(message_id)))
        return messages


if __name__ == '__main__':
    userDao = UserDao("pengym_111@163.com")

    # add user
    userDao.add_contact(Contact("John", "John@outlook.com", "123456", True, True))
    userDao.add_contact(Contact("Jack", "Jack@outlook.com", "123456", True, True))

    # add group
    userDao.add_group('面向对象', ('John@outlook.com', 'Jack@outlook.com'))

    # save message with attachments
    buf1 = open('test.jpg', 'rb').read()
    buf2 = open('user.sql', 'rb').read()
    msg = Message("85934a68-f4f1-38e2-b6e8-cabd3c05bb52", "Happy New Year!", "2018-1-1", "pengym_111@163.com",
                  attachments=[buf1, buf2])
    userDao.add_messages(msg)

    for group in userDao.get_groups():
        print(group.name)
        print(group.members)

        for message in userDao.get_group_messages(group.group_uuid):
            print(message)

            for f in message.attachments:
                print(repr(str(f)))

    userDao.change_contact_block_state("John@outlook.com")
    userDao.remove_contact('John@outlook.com')
