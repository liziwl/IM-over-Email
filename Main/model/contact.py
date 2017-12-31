class Contact(object):
    def __init__(self, name, account, public_key, trusted):
        self.name = name
        self.account = account
        self.public_key = public_key
        self.trusted = trusted

    def __str__(self):
        return '{"name": %s, "account": %s, "public_key": %s, "trusted": %s}'\
            % (self.name, self.account, self.public_key, self.trusted)
