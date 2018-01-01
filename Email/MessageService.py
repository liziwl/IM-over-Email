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

    # send a message to several accounts.
    def send_message(self, accounts, message):
        raise NotImplementedError

    # get all mails in 'INBOX' with subject as uuid
    def get_all_messages(self, uuid):
        raise NotImplementedError

    # get all unseen message in 'INBOX' with subject as uuid
    def get_unseen_message(self, uuid):
        raise NotImplementedError

    def notify(self, listener):
        raise NotImplementedError


class MessageService(MessageServiceInterface):

    def get_all_messages(self, uuid):

        pass

    def notify(self, listener):
        pass

    def __init__(self, user_config, listener):
        self.user_config = user_config
        self.load_privkey(None)
        self.mailservice = MailService(user_config)

    # need to change just return the private key object of this user
    def load_privkey(self, key_path):

        '''
        with open(key_path, 'rb') as f:
            key = f.read()
            f.close()
        self.privkey = KeyService.load_privkey(key)
        '''

        # (pubkey, privkey) = rsa.newkeys(512)
        self.privkey = privkey

    # hash function

    def _getuuid(self, accounts):
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

    def _decrypt_mail(self, mail):
        try:
            mail['text'][0]['text'] = EncryptionDecryption.decrypt_mail(mail['text'][0]['text'], self.privkey)
            mail['attachments'] = EncryptionDecryption.decrypt_attachments(mail['attachments'], self.privkey)
            print('decrypted!\n')
            print(mail['text'][0]['text'])
            return mail
        except:
            return None

    def get_message(self, folder):
        msg = []
        mails = self.mailservice.get_mails_in_folder(folder)
        for mail in mails:
            de_mail = self._decrypt_mail(mail)
            if de_mail is not None:
                msg.append(de_mail)
        return msg

    def get_unseen_message(self, folder):
        msg = []
        mails = self.mailservice.get_unseen_mails_in_folder(folder)
        for mail in mails:
            de_mail = self._decrypt_mail(mail)
            if de_mail is not None:
                msg.append(de_mail)
        return msg

    def get_unanswered_message(self, folder):
        msg = []
        mails = self.mailservice.get_unanswered_mails_in_folder(folder)
        for mail in mails:
            de_mail = self._decrypt_mail(mail)
            if de_mail is not None:
                msg.append(de_mail)
        return msg

    # # we should make a new folder for this
    # # new message will show first
    def get_all_conversion(self, accounts):
        msg_in = self.get_message('INBOX')
        msg_out = self.get_message('已发送')
        msg = []
        if msg_in is not None:
            msg.extend(msg_in)
        if msg_out is not None:
            msg.extend(msg_out)
        return self._get_mail_by_account(accounts, msg)

    # accounts['mail address','mail address']
    def get_mails_by_accounts(self, accounts):
        uuid = self._getuuid(accounts)
        return self.get_mails_by_uuid(uuid)

    def get_mails_by_uuid(self, uuid):
        msg = self.mailservice.get_mails_in_folder_with_subject('INBOX', str(uuid))
        if msg is None:
            return []
        else:
            return sorted(msg, key=lambda m: m['date'])

    # look for unseen message send by this accounts
    def get_unseen(self, accounts):
        msg_in = self.get_unseen_message('INBOX')
        return self._get_mail_by_account(accounts, msg_in)

    # may be useless
    def get_sent(self, accounts):
        msg_out = self.get_message('已发送')
        return self._get_mail_by_account(accounts, msg_out)

    def _get_mail_by_account(self, accounts, msg):
        results = []
        if msg is not None:
            for m in msg:
                if m['subject'] == self._getuuid(accounts):
                    results.append(m)
            sorted(results, key=lambda m: m['date'])
        return results


if __name__ == '__main__':
    user_config = {
        "account": "pengym_111@163.com",
        "password": "hvwoTxJndBEi8B4G",
        "imap_server": "imap.163.com",
        "imap_port": 993,
        "smtp_server": "smtp.163.com",
        "smtp_port": 25
    }

    messageserver = MessageService(user_config)

    # please use your e-mail to try this :)
    messageserver.send_message(['pengym_111@163.com'], 'hello2', ['lenna.jpeg'])

    messageserver.get_unseen_message('INBOX')

    print(messageserver.get_all_conversion(['pengym_111@163.com']))
    # messageserver.send_message(['11510050@mail.sustc.edu.cn'], 'hello', None)
