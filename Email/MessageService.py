from Security.EncryptionDecryptionService import EncryptionDecryption
from Email.MailService import MailService
import rsa
import Main
import threading
import time
from Main.model.message import Message
from Security.KeyService import KeyService
from Main import utils

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

    def __init__(self, user, listener, userdao):

        self.user = user
        self.user_config = {
            "account": user.account,
            # mail password
            "password": user.password,
            "imap_server": user.imap_server,
            "imap_port": user.imap_port,
            "smtp_server": user.smtp_server,
            "smtp_port": user.smtp_port
        }

        self.mailservice = MailService(self.user_config)
        self.userdao = userdao
        self.listener = listener
        self.load_privkey()
        listen = threading.Thread(target=self._listen_message, args=())
        listen.start()

        # need to change just return the private key object of this user

    def load_privkey(self):
        # TODO self.privkey = KeyService.getPrivateKey(self.user.account,self.user.lock_password)　这里的锁屏密码用来加密私钥，锁屏密码现在默认都是123456 这个字端在UI端还无法设置，请完善 并且利用这个进行登陆验证
        self.privkey = KeyService.getPrivateKey(self.user_config["account"], "123456")

    # 检查可以解密的未读消息，并且返回给chat
    def _listen_message(self):
        while True:
            new_messages = self._get_unseen_message()
            # 每过这段时间检查一下邮箱
            time.sleep(3)
            if len(new_messages) != 0:
                self.notify(listener=self.listener, messages=new_messages)

    def _get_unseen_message(self):
        mails = self.mailservice.get_unseen_mails_in_folder('INBOX')
        messages = []
        for mail in mails:
            mail = self._decrypt_mail(mail)
            if mail is not None:
                # if has attachment, the first 2 are keys
                attachments = list()
                if len(mail['attachments']) > 2:
                    attachments = [
                        {
                            'filename': f['filename'],
                            'data': f['data']
                        } for f in mail['attachments'][2:]
                    ]
                message = Message(mail['subject'],
                                  mail['text'][0]['text'], mail['date'], mail['from_email'], attachments)
                # 这里不加mail['send_from']的原因是如果对方也遵守协议，他会给自己发邮件，所以这一栏就是群聊当中的所有人
                messages.append((message, mail['to']))
                # messages.append(message)
        return messages

    def get_all_messages(self, uuid):
        # get all message from data base dao
        return self.userdao.get_group_messages(uuid)

    def notify(self, listener, messages):
        listener.update_messages(messages)

    # receiver : send to
    # receivers: 收件人
    def _send_message_single(self, receiver, receivers, message, binary_attachments, uuid):
        pubkey = KeyService.getPublicKey(receiver)
        encrypted_binary_files = EncryptionDecryption.encrypt_attachments(binary_attachments, public_key=pubkey)
        ct_message = EncryptionDecryption.encrypt_mail(message, pubkey)
        self.mailservice.send_mail(receiver, receivers, subject=uuid, content=ct_message,
                                   attachments=encrypted_binary_files)

    def send_message(self, accounts, message):
        import uuid
        # just send content
        content = message.content
        # uid = self._getuuid(accounts)
        uid = utils.get_uuid(accounts)
        for receiver in accounts:
            self._send_message_single(receiver, accounts, content, message.attachments, uid)

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

    # userdao = UserDao('penym_111@163.com', '../Main/test.db')
    # messageserver = MessageService(user_config, None, userdao)
    #
    # uid = messageserver.getuuid(['pengym_111@163.com'])
    #
    # # please use your e-mail to try this :)
    # message = Main.model.message.Message(str(uid), 'hello', "", "pengym_111@163.com")
    # messageserver.send_message(['pengym_111@163.com'], message)
    # # messageserver.send_message(['pengym_111@163.com'], 'hello2', ['lenna.jpeg'])
    #
    # # messageserver.get_unseen_message('INBOX')
    #
    # time.sleep(3)
    # print(messageserver.get_unseen_message(uid))
    # print(messageserver.get_all_messages(uid))
    #
    # # print(messageserver.get_all_conversion(['pengym_111@163.com']))
    # # messageserver.send_message(['11510050@mail.sustc.edu.cn'], 'hello', None)

    # 1048217874@qq.com
    # pengym_111@163.com
    # hvwoTxJndBEi8B4G
