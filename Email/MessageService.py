from Security.KeyService import KeyService
from Security.EncryptionDecryptionService import EncryptionDecryption
from Email.MailService import MailService
import uuid
import copy
# for testing
import rsa

# !! just fot test
# we need this from KeyService
(pubkey, privkey) = rsa.newkeys(512)


class MessageServiceInterface:
    privkey = None
    user_config = None
    mailservice = None

    # send a message to a single account.
    def send_message(self, accounts, message, attachments_path):
        raise NotImplementedError

    # check the subject to decide whether to decrypt the message
    def get_message(self, folder):
        raise NotImplementedError

    def get_unseen_message(self, folder):
        raise NotImplementedError

    def get_unanswered_message(self, folder):
        raise NotImplementedError

    def get_unseen_conversion(self, accounts):
        raise NotImplementedError

    def get_all_conversion(self, accounts):
        raise NotImplementedError


class MessageService(MessageServiceInterface):

    def __init__(self, user_config):
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
        sorted(accounts_name)
        names = ''
        for name in accounts_name:
            names = name + names
        return str(uuid.uuid3(uuid.NAMESPACE_DNS, names))

    # receiver : send to
    # receivers: 收件人
    def _send_message_single(self, receiver, receivers, message, attachments_path, uuid):
        # pubkey = KeyService.getPublicKey(account)

        ct_message = EncryptionDecryption.encrypt_mail(message, pubkey)
        self.mailservice.send_mail(receiver, receivers, subject=uuid, content=ct_message, attachments=attachments_path)

    def send_message(self, receivers, message, attachments_path):
        uid = self._getuuid(receivers)
        for receiver in receivers:
            self._send_message_single(receiver, receivers, message, attachments_path, uid)

    def get_message(self, folder):
        msg = []
        mails = self.mailservice.get_mails_in_folder(folder)
        for mail in mails:
            try:
                mail['text'][0]['text'] = EncryptionDecryption.decrypt_mail(mail['text'][0]['text'], self.privkey)
                print('decrypted!\n')
                print(mail['text'][0]['text'])
                msg.append(mail)
            except:
                pass
        return msg

    def get_unseen_message(self, folder):
        msg = []
        mails = self.mailservice.get_unseen_mails_in_folder(folder)
        for mail in mails:
            try:
                mail['text'][0]['text'] = EncryptionDecryption.decrypt_mail(mail['text'][0]['text'], self.privkey)
                print('decrypted!\n')
                print(mail['text'][0]['text'])
                msg.append(mail)
            except:
                pass
        return msg

    def get_unanswered_message(self, folder):
        msg = []
        mails = self.mailservice.get_unanswered_mails_in_folder(folder)
        for mail in mails:
            try:
                mail['text'][0]['text'] = EncryptionDecryption.decrypt_mail(mail['text'][0]['text'], self.privkey)
                print('decrypted!\n')
                print(mail['text'][0]['text'])
                msg.append(mail)
            except:
                pass
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

    # look for unseen message send by this accounts
    def get_unseen(self, accounts):
        msg_in = self.get_unseen_message('INBOX')
        return self._get_mail_by_account(accounts, msg_in)

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
    messageserver.send_message(['pengym_111@163.com'], 'hello2', None)

    messageserver.get_unseen_message('INBOX')

    print(messageserver.get_all_conversion(['pengym_111@163.com']))
    # messageserver.send_message(['11510050@mail.sustc.edu.cn'], 'hello', None)
