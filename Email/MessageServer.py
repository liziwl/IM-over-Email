from Security.KeyService import KeyService
from Security.EncryptionDecryptionService import EncryptionDecryption
from Email.MailService import MailService
import uuid
import copy
# for testing
import rsa


class MessageServerInterface:
    privkey = None
    user_config = None
    mailservice = None

    # send a message to a single account.
    def send_message(self, accounts, message, attachments_path):
        raise NotImplementedError

    # check the subject to decide whether to decrypt the message
    def get_message(self, folder):
        raise NotImplementedError

    def get_unread_message(self, folder):
        raise NotImplementedError

    def get_unanswered_message(self, folder):
        raise NotImplementedError


class MessageServer(MessageServerInterface):

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
        (pubkey, privkey) = rsa.newkeys(512)
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

    def _send_message_single(self, account, message, attachments_path, uuid):
        # pubkey = KeyService.getPublicKey(account)
        (pubkey, privkey) = rsa.newkeys(512)
        ct_message = EncryptionDecryption.encrypt_mail(message, pubkey)
        self.mailservice.send_mail(account, subject=uuid, content=ct_message, attachments=attachments_path)

    def send_message(self, accounts, message, attachments_path):
        uid = self._getuuid(accounts)
        for account in accounts:
            self._send_message_single(account, message, attachments_path, uid)

    def get_message(self, folder):
        mails = self.mailservice.get_mails_in_folder(folder)
        for mail in mails:
            mail['text'][0]['text'] = EncryptionDecryption.decrypt_mail(mail['text'][0]['text'], self.privkey)
        return mails

    def get_unseen_message(self, folder):
        mails = self.mailservice.get_unseen_mails_in_folder(folder)
        for mail in mails:
            mail['text'][0]['text'] = EncryptionDecryption.decrypt_mail(mail['text'][0]['text'], self.privkey)
        return mails

    def get_unanswered_message(self, folder):
        mails = self.mailservice.get_unanswered_mails_in_folder(folder)
        for mail in mails:
            mail['text'][0]['text'] = EncryptionDecryption.decrypt_mail(mail['text'][0]['text'], self.privkey)
        return mails


if __name__ == '__main__':
    user_config = {
        "account": "pengym_111@163.com",
        "password": "hvwoTxJndBEi8B4G",
        "imap_server": "imap.163.com",
        "imap_port": 993,
        "smtp_server": "smtp.163.com",
        "smtp_port": 25
    }

    messageserver = MessageServer(user_config)

    messageserver.send_message(['wanggy97@gmail.com'], 'hello', None)
