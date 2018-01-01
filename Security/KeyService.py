import rsa
import gnupg
import requests
from Security.EncryptionDecryptionService import EncryptionDecryption
import os
import random
import sys


class KeyServiceInterface:
    # get the AES public key of a account
    @staticmethod
    def getPublickey(account):
        raise NotImplementedError

    @staticmethod
    # generate public key and private key for a new account
    # user is a dictionary
    def generate_keys(path, user):
        raise NotImplementedError

    @staticmethod
    # check whether the public key belongs to the account.
    def check_publickey(account, public_key):
        raise NotImplementedError

    # encode the pubkey to binary format and return
    @staticmethod
    def save_pubkey(key, format):
        raise NotImplementedError

    # encode the private key to binary format and return
    @staticmethod
    def save_privkey(key, format):
        raise NotImplementedError

    # load the pubkey from standard binary format and return
    @staticmethod
    def load_pubkey(key, format):
        raise NotImplementedError

    # load the private key from standard binary format and return
    @staticmethod
    def load_privkey(ket, format):
        raise NotImplementedError


class KeyService(KeyServiceInterface):
    @staticmethod
    def check_publickey(account, public_key):
        compare_uid = "<" + account + ">"
        gpg = gnupg.GPG()
        user_keys = gpg.list_keys()
        for key_array in user_keys:
            uid = key_array["uids"][0].split(' ', 1)[1]
            if compare_uid == uid:
                pub_key = KeyService.getPublicKey(account)
                if pub_key == public_key:
                    return True
                else:
                    return False

    @staticmethod
    def generate_keys(email_address, password):
        pubkey,privkey = rsa.newkeys(512)

        KeyService._post_keys(email_address,pubkey)

        privkey_pem = privkey.save_pkcs1('PEM')
        random.seed(password)
        chacha20_key = random.getrandbits(32 * 8).to_bytes(32, sys.byteorder)
        nonce = random.getrandbits(16 * 8).to_bytes(16, sys.byteorder)

        ct_private_key = EncryptionDecryption.chacha20_encrypt(privkey_pem,chacha20_key,nonce)

        with open("private_key"+email_address,'wb') as f:
            f.write(ct_private_key)
            f.close()
        return privkey

    # post public key to server
    @staticmethod
    def _post_keys(email_address,pubkey):
        pubkey_pem = pubkey.save_pkcs1("PEM")
        # base64.b64encode(ct_mail).decode('ascii')
        # post the key to server
        payload = {"email": email_address, "public_key": pubkey_pem.decode('ascii')}
        r = requests.post("http://csyllabus.org:9999/api/key", json=payload)

    @staticmethod
    def getPublicKey(account):
        # get binary key from server as string
        payload = {"email":account}
        r = requests.post("http://csyllabus.org:9999/api/key/public_key",json=payload)
        r.encoding = 'ascii'
        str_pk = r.text
        pk = str_pk.encode('ascii')
        return rsa.PublicKey.load_pkcs1(pk,format="PEM")


    @staticmethod
    def getPrivateKey(account,password):
        try:
            with open("private_key"+account,'rb') as f:
                pk = f.read()
                f.close()
            random.seed(password)
            chacha20_key = random.getrandbits(32 * 8).to_bytes(32,sys.byteorder)
            nonce = random.getrandbits(16 * 8).to_bytes(16,sys.byteorder)

            de_pk = EncryptionDecryption.chacha20_decrypt(pk,chacha20_key,nonce)
            return rsa.PrivateKey.load_pkcs1(de_pk,format="PEM")
        except FileNotFoundError:
            print("this user has not generate private key!")

    @staticmethod
    def save_privkey(account, format='PEM'):
        private_key = KeyService.getPrivateKey(account)
        return private_key.save_pkcs1(format=format)

    @staticmethod
    def save_pubkey(account, format='PEM'):
        pubkey = KeyService.getPublicKey(account)
        return pubkey.save_pkcs1(format=format)

    @staticmethod
    def load_privkey(key, format='PEM'):
        return rsa.PrivateKey.load_pkcs1(key, format='PEM')

    @staticmethod
    def load_pubkey(key, format='PEM'):
        return rsa.PublicKey.load_pkcs1(key, format=format)


if __name__ == '__main__':
    import random
    random.seed('hhhh')


    print(KeyService.getPublicKey("pengym_111@163.com"))
    # print(KeyService.getPublicKey("1048217874@qq.com"))
    # print(KeyService.generate_keys("pengym_111@163.com","123456"))

    print(KeyService.getPrivateKey("pengym_111@163.com","123456"))




    #print(KeyService.generate_keys())
    # from the public key object to binary file
    # pem_pubkey = KeyService.save_pubkey(pubkey)
    # from the binary file to public key object
    # red_pubkey = KeyService.load_pubkey(pem_pubkey)
    # print(red_pubkey)
    # print(pem_pubkey)

