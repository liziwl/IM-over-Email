# -*- coding: utf-8 -*-
import time as ti


class Chat_log(object):
    def __init__(self, email, uid=None):
        self.email = email
        self.uid = uid
        self.log = []

    def add_log(self, content, time=None):
        self.log.append(Log(content, time))

    def log_toString(self):
        out = ""
        for it in self.log:
            out += "{}\n{}\n".format(it.time_stmp, it.content)
        return out


class Log(object):
    def __init__(self, content, time=None):
        if time is None:
            now = ti.localtime()
            dt = ti.strftime("%Y-%m-%d %H:%M:%S", now)
            self.time_stmp = dt
        else:
            self.time_stmp = time
        self.content = content
