import os
import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import base64

class EncryptionDecryptionServiceInterface:
    # encrypt an e-mail using chacah20
    # input: content of the mail RSA public key (rsa public key object)
    # encrypt the chacha20 key using public key with AES
    # encrypt the mail with the chacha20 key
    # return encrypted chacha20 key,encrypted mail
    @staticmethod
    def encrypt_mail(mail, public_key):
        raise NotImplementedError

    # decrypt an e-mail
    # imput: mail rsa private_key object
    @staticmethod
    def decrypt_mail(mail, private_key):
        raise NotImplementedError


class EncryptionDecryption(EncryptionDecryptionServiceInterface):
    @staticmethod
    def encrypt_mail(mail, public_key, encode_type='utf8'):
        # from str to binary
        mail_bin = mail.encode(encode_type)
        chacha20_key, nonce = EncryptionDecryption._generate_chanchan20_key()
        # encrypt mail using chacha20 with new generated chacha20key
        ct_mail = EncryptionDecryption._chacha20_encrypt(mail_bin, chacha20_key, nonce)
        # encrypt chacha20 key
        encrypted_chacha20_key = EncryptionDecryption._rsa_encrypt(chacha20_key, public_key)
        # return encrypted mail with encrypted  chacha20key as header
        return base64.b64encode(encrypted_chacha20_key).decode('ascii') + '\n' + base64.b64encode(nonce).decode(
            'ascii') + '\n' + base64.b64encode(ct_mail).decode('ascii')

    @staticmethod
    def _generate_chanchan20_key():
        chacha20_key = os.urandom(32)  # must be 32 bytes
        nonce = os.urandom(16)  # nonce
        return chacha20_key, nonce

    @staticmethod
    def _rsa_encrypt(message, publickey):
        return rsa.encrypt(message, publickey)

    @staticmethod
    def _rsa_decrypt(ct_message, privatekey):
        return rsa.decrypt(ct_message, privatekey)

    @staticmethod
    def _chacha20_encrypt(message, key, nonce):
        cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
        encryptor = cipher.encryptor()
        ct_mail = encryptor.update(message)
        return ct_mail

    @staticmethod
    def _chacha20_decrypt(ct_message, key, nonce):
        cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
        decryptor = cipher.decryptor()
        message = decryptor.update(ct_message)
        return message

    # decrypt an e-mail
    @staticmethod
    def decrypt_mail(mail, private_key, encode_type='utf8'):
        # mail = str(base64.b64decode(mail))
        split_mail = mail.split('\n', 2)
        ct_chacha20_key = base64.b64decode(split_mail[0].encode('ascii'))
        # non encrypted
        ct_nonce = base64.b64decode(split_mail[1].encode('ascii'))
        ct_mail = base64.b64decode(split_mail[2].encode('ascii'))

        chacha20_key = EncryptionDecryption._rsa_decrypt(ct_chacha20_key, private_key)

        mail_bin = EncryptionDecryption._chacha20_decrypt(ct_mail, chacha20_key, ct_nonce)
        return mail_bin.decode(encode_type)


if __name__ == '__main__':
    # test
    (pubkey, privkey) = rsa.newkeys(512)
    data = '''The Witcher 3: Wild Hunt[a] is a 2015 action role-playing video game developed and published by CD Projekt. 
Based on The Witcher series of fantasy novels by Polish author Andrzej Sapkowski, 
it is the sequel to the 2011 video game The Witcher 2: Assassins of Kings and the third installment in The Witcher video game series. 
Played in an open world with a third-person perspective, players control protagonist Geralt of Rivia. 
Geralt, a monster hunter known as a Witcher, is looking for his missing adopted daughter, 
who is on the run from the Wild Hunt: an otherworldly force determined to capture and use her powers. 
Players battle the game's many dangers with weapons and magic, interact with non-player characters, 
and complete main-story and side quests to acquire experience points and gold, 
which are used to increase Geralt's abilities and purchase equipment. Its central story has several endings, 
determined by the player's choices at certain points in the game.'''

    send_mail = EncryptionDecryption.encrypt_mail(data, pubkey)
    print(send_mail)

    rcv_mail = EncryptionDecryption.decrypt_mail(send_mail, privkey)
    print(rcv_mail)
