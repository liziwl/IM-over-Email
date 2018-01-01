from Security.EncryptionDecryptionService import EncryptionDecryption
from Email.MailService import MailService
import uuid
import copy
# for testing
import rsa
import os
import Main
import threading
import time
from Main.model.message import Message
import threading
from Main.dao.user_dao import UserDao

# !! just fot test
# we need this from KeyService
(pubkey, privkey) = rsa.newkeys(512)


# folder: 'INBOX'
# message [mail]

class MessageServiceInterface:
    privkey = None
    user_config = None
    mailservice = None
    listener = None
    UserDao = None

    # send a message to several accounts.
    def send_message(self, accounts, message):
        raise NotImplementedError

    # get all mails in 'INBOX' with subject as uuid
    def get_all_messages(self, uuid):
        raise NotImplementedError

    # get all unseen message in 'INBOX' with subject as uuid
    def get_unseen_message(self, uuid):
        raise NotImplementedError

    def notify(self, listener, messages):
        raise NotImplementedError


class MessageService(MessageServiceInterface):

    def __init__(self, user_config, listener, userdao):
        self.user_config = user_config
        self.load_privkey(None)
        self.mailservice = MailService(user_config)
        self.userdao = userdao

        listen = threading.Thread(target=self._listen_message, args=())
        listen.start()

        # need to change just return the private key object of this user

    def load_privkey(self, key_path):
        '''
        with open(key_path, 'rb') as f:
            key = f.read()
            f.close()
        self.privkey = KeyService.load_privkey(key)
        '''
        self.privkey = privkey

    def get_unseen_message(self, uuid):
        mails = self.mailservice.get_unseen_mails_in_folder_with_subject('INBOX', str(uuid))
        messages = []
        for mail in mails:
            mail = self._decrypt_mail(mail)
            if mail is not None:
                message = Main.model.message.Message(uuid, mail['text'][0]['text'], mail['date'], mail['from_email'])
                messages.append(message)
                self.userdao.add_messages(message)
        return messages

    def _listen_message(self):
        while True:
            new_messages = self._get_unseen_message()
            time.sleep(5)
            if len(new_messages) != 0:
                self.notify(listener=self.listener, messages=new_messages)

    def _get_unseen_message(self):
        mails = self.mailservice.get_unseen_mails_in_folder('INBOX')
        messages = []
        for mail in mails:
            mail = self._decrypt_mail(mail)
            if mail is not None:
                message = Message(uuid, mail['text'][0]['text'], mail['date'], mail['from_email'])
                messages.append(message)
        return messages
        pass

    def get_all_messages(self, uuid):
        # get all message from data base dao
        return self.userdao.get_group_messages(uuid)

    def notify(self, listener, messages):
        # to do
        # listener.update(messages)
        print(message.content)
        print('notifyed')
        pass

    # hash function

    def _getuuid(self, accounts):
        accounts_name = copy.deepcopy(list(accounts))
        accounts_name.append(self.user_config['account'])
        accounts_name = sorted(accounts_name)
        names = ''
        for name in accounts_name:
            names = name + names
        return str(uuid.uuid3(uuid.NAMESPACE_DNS, names))

    def getuuid(self, accounts):
        accounts_name = copy.deepcopy(list(accounts))
        accounts_name.append(self.user_config['account'])
        accounts_name = sorted(accounts_name)
        names = ''
        for name in accounts_name:
            names = name + names
        return str(uuid.uuid3(uuid.NAMESPACE_DNS, names))

    # receiver : send to
    # receivers: 收件人
    def _send_message_single(self, receiver, receivers, message, binary_attachments, uuid):
        # pubkey = KeyService.getPublicKey(account)
        encrypted_binary_files = EncryptionDecryption.encrypt_attachments(binary_attachments, public_key=pubkey)
        ct_message = EncryptionDecryption.encrypt_mail(message, pubkey)
        self.mailservice.send_mail(receiver, receivers, subject=uuid, content=ct_message,
                                   attachments=encrypted_binary_files)

    # def send_message(self, receivers, message, attachments_path, uid=None):
    #     binary_attachments = []
    #     for f in attachments_path or []:
    #         with open(f, 'rb') as fil:
    #             binary_attachments.append({'filename': os.path.basename(f), 'data': fil.read()})
    #     if uid is None:
    #         uid = self._getuuid(receivers)
    #     for receiver in receivers:
    #         self._send_message_single(receiver, receivers, message, binary_attachments, uid)

    def send_message(self, accounts, message):
        # just send content
        content = message.content
        uid = self._getuuid(accounts)
        for recevier in accounts:
            self._send_message_single(recevier, accounts, content, [], uid)

        self.userdao.add_messages(message)

    def _decrypt_mail(self, mail):
        try:
            mail['text'][0]['text'] = EncryptionDecryption.decrypt_mail(mail['text'][0]['text'], self.privkey)
            mail['attachments'] = EncryptionDecryption.decrypt_attachments(mail['attachments'], self.privkey)
            return mail
        except:
            return None


if __name__ == '__main__':
    user_config = {
        "account": "pengym_111@163.com",
        "password": "hvwoTxJndBEi8B4G",
        "imap_server": "imap.163.com",
        "imap_port": 993,
        "smtp_server": "smtp.163.com",
        "smtp_port": 25
    }

    userdao = UserDao('penym_111@163.com', '../Main/test.db')
    messageserver = MessageService(user_config, None, userdao)

    uid = messageserver.getuuid(['pengym_111@163.com'])

    # please use your e-mail to try this :)
    message = Main.model.message.Message(str(uid), 'hello', "", "pengym_111@163.com")
    messageserver.send_message(['pengym_111@163.com'], message)
    # messageserver.send_message(['pengym_111@163.com'], 'hello2', ['lenna.jpeg'])

    # messageserver.get_unseen_message('INBOX')

    time.sleep(3)
    print(messageserver.get_unseen_message(uid))
    print(messageserver.get_all_messages(uid))

    # print(messageserver.get_all_conversion(['pengym_111@163.com']))
    # messageserver.send_message(['11510050@mail.sustc.edu.cn'], 'hello', None)
