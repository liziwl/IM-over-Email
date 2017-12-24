# coding: utf-8
from Security.KeyService import KeyService
from Security.EncryptionDecryptionService import EncryptionDecryption
import imapy
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE, formatdate
import os.path
from imapy.query_builder import Q


class MailServiceInterface:
    user_config = None
    mailbox = None

    query_builder = None

    def _login(self):
        raise NotImplementedError

    def show_mails(self, mails):
        raise NotImplementedError

    # ex. get all mails in '已发送'
    def get_mails_in_folder(self, folder):
        raise NotImplementedError

    # get all unseen emails in folder
    def get_unseen_mails_in_folder(self, folder):
        raise NotImplementedError

    # send an e-mail to receiver attachments is a list of file paths. not binary stream.
    #  ['1048217874@qq.com'], '辣鸡，Project 做完了吗?', 'hhhhh', ['lenna.jpeg']
    def send_mail(self, receiver, receivers, subject, content, attachments=None):
        raise NotImplementedError


class MailService(MailServiceInterface):

    def __init__(self, user_config):
        self.user_config = user_config
        self.query_builder = Q()
        self._login()

    def _login(self):
        self.mailbox = imapy.connect(
            host=self.user_config['imap_server'],
            username=self.user_config['account'],
            password=self.user_config['password'],
            ssl=True
        )

    # show a single mail
    def _show_mail(self, mail):
        print('-' * 100)
        print('Subject: ', mail['subject'])
        print('From: ', mail['from_email'])
        print('To: ', mail['to'])
        print('Date: ', mail['date'])
        print('*' * 100)
        print('Content: ')
        content = mail['text'][0]['text']
        print(content)
        print('Attachments: ', mail['attachments'])
        print('*' * 100)

    # show all mails
    def show_mails(self, mails):
        for mail in mails:
            self._show_mail(mail)

    def get_mails_in_folder(self, folder):
        mails = self.mailbox.folder(folder).emails()
        if mails is False:
            return None
        return mails

    def get_unseen_mails_in_folder(self, folder):
        mails = self.mailbox.folder(folder).emails(self.query_builder.unanswered().unseen())
        if mails is False:
            return None
        return mails

    def get_unanswered_mails_in_folder(self, folder):
        mails = self.mailbox.folder(folder).emails(self.query_builder.unanswered().unanswered())
        if mails is False:
            return None
        return mails

    def send_mail(self, receiver, receivers, subject, content, attachments=None):
        account = self.user_config['account']
        password = self.user_config['password']

        message = MIMEMultipart()
        message['From'] = account
        message['To'] = ';'.join(receivers)
        # message['To'] = receivers
        message['Subject'] = subject
        message['Date'] = formatdate(localtime=True)
        message.attach(MIMEText(content))

        for f in attachments or []:
            with open(f, 'rb') as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=os.path.basename(f)
                )
            part['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(f)
            message.attach(part)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.user_config['smtp_server'], self.user_config['smtp_port'])
            smtpObj.login(account, password)
            smtpObj.sendmail(account.format(account), receiver, message.as_string())
            smtpObj.close()
        except smtplib.SMTPException as e:
            print("Error: Unable to send email!")
