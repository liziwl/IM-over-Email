class User(object):
    def __init__(self, account, lock_password,
                 smtp_server, smtp_port, imap_server, imap_port):
        self.account = account
        self.lock_password = lock_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.imap_server = imap_server
        self.imap_port = imap_port
