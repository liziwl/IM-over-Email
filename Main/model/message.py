class Message(object):
    def __init__(self, group, content, date, sender):
        self.group = group
        self.content = content
        self.date = date
        self.sender = sender
    
    def __str__(self):
        return self.content
