class Group(object):
    def __init__(self, name, members):
        self.name = name
        self.members = members[:]

    def __str__(self):
        return '{"name": %s, "member": %s}' % (self.name, [str(m) for m in self.members])
