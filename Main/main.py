from Main.dao.main_dao import MainDao


class Application(object):
    def __init__(self):
        self.mainDao = MainDao()


def create_user(user):
    import os
    import uuid
    user_id = uuid.uuid4()
    directory = str(user_id)
    # create folder
    os.mkdir(directory)
    # create keys
    public_key, private_key = create_keys()
    # TODO: encrypt private key
    # TODO: encrypt lock password
    # create user database
    create_db(directory, "database/user.sql")
    # insert record to main database


def create_db(path, script):
    import sqlite3
    try:
        # create user database
        conn = sqlite3.connect(path)
        c = conn.cursor()
        # create tables
        c.executescript(script)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        exit(1)


def create_keys():
    # TODO: Generate key
    public_key = ""
    private_key = ""
    # TODO: Upload public to server
    return public_key, private_key


if __name__ == '__main__':
    create_user()