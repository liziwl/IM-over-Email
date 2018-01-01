class Group(object):
    def __init__(self, name, members, group_uuid):
        self.name = name
        self.members = members[:]
        self.group_uuid = group_uuid

    def __str__(self):
        return '{"name": %s, "member": %s}' % (self.name, [str(m) for m in self.members])
