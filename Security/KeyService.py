import rsa
import gnupg
import pem


class KeyServiceInterface:
    # get the AES public key of a account
    @staticmethod
    def get_public_key(account):

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
        compare_uid = "<"+account+">"
        print(compare_uid)
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
        pass

    @staticmethod
    def generate_keys():
        gpg = gnupg.GPG()
        user_input = gpg.gen_key_input(name_real=NAME, name_email=NAME_EMAIL, passphrase=PASSPHRASE)
        user_key = gpg.gen_key(user_input)
        return user_key

    @staticmethod
    def getPublicKey(account):
        gpg = gnupg.GPG()
        key_information = gpg.search_keys(account, 'hkp://pgp.mit.edu')
        public_key = gpg.export_keys(key_information[0]["keyid"])
        return public_key


    @staticmethod
    def save_privkey(key, format='PEM'):
        return key.save_pkcs1(format=format)

    @staticmethod
    def save_pubkey(key, format='PEM'):
        return key.save_pkcs1(format=format)

    @staticmethod
    def load_privkey(key, format='PEM'):
        return rsa.PrivateKey.load_pkcs1(key, format='PEM')

    @staticmethod
    def load_pubkey(key, format='PEM'):
        return rsa.PublicKey.load_pkcs1(key, format=format)


if __name__ == '__main__':
    account = 'mintmao@outlook.com'

    NEW_KEY_DIR = './KEY'
    NAME = 'helloworld'
    NAME_COMMENT = None
    NAME_EMAIL = 'helloworld@mail.com'
    EXPIRE_DATE = None
    PASSPHRASE =None
    KEY_TYPE = 'RSA'
    KEY_USAGE = 'cert'
    KEY_LENGTH = 2048
    SUBKEY_TYPE = 'RSA'
    SUBKEY_USAGE = 'SIGN'
    SUBKEY_LEGNT = 4096
    KEYSERVER = 'hkp://pgp.mit.edu'
    print(KeyService.generate_keys())
    # from the public key object to binary file
    # pem_pubkey = KeyService.save_pubkey(pubkey)
    # from the binary file to public key object
    # red_pubkey = KeyService.load_pubkey(pem_pubkey)
    # print(red_pubkey)
    # print(pem_pubkey)
