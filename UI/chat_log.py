# -*- coding: utf-8 -*-
import time as ti


class Chat_log(object):
    GROUP = 1
    SINGLE = 0

    def __init__(self, email, type, name=None, uid=None):
        self.name = name
        self.email = email
        self.uid = uid
        self.log = []
        self.isblocked = False
        self.type = type

    def set_blocked(self):
        self.isblocked = True

    def reset_blocked(self):
        self.isblocked = False

    def add_log(self, content, time=None, sender=None):
        self.log.append(Log(content, time, sender))

    def log_toString(self):
        out = ""
        for it in self.log:
            out += "{} {}\n{}\n".format(it.sender, it.time_stmp, it.content)
        return out[:-1]


# TODO 添加标识，标记这个信息是否是自己发出，如果是的话就显示在文本靠右的位置（与收到的信息区分）
class Log(object):
    def __init__(self, content, time=None, sender=None):
        if time is None:
            now = ti.localtime()
            dt = ti.strftime("%Y-%m-%d %H:%M:%S", now)
            self.time_stmp = dt
        else:
            self.time_stmp = time
        self.content = content
        if sender is None:
            sender = 'None'
        self.sender = sender
