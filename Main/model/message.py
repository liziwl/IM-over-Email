class Message(object):
    # TODO 解决附件的问题， 多个附件， 文本+附件等 底层可以对一封既有正文又有附件的邮件进行加密
    def __init__(self, group, content, date, sender, attachments=[]):
        self.group = group
        self.content = content
        self.date = date
        self.sender = sender
        self.attachments = attachments
    
    def __str__(self):
        return self.content
