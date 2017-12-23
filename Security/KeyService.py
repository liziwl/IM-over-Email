import rsa


class KeyServiceInterface:
    # get the AES public key of a account
    @staticmethod
    def getPublicKey(account):
        raise NotImplementedError

    @staticmethod
    # generate public key and private key for a new account
    def generate_keys():
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
        pass

    @staticmethod
    def generate_keys():
        (pubkey, privkey) = rsa.newkeys(512)
        return pubkey, privkey

    @staticmethod
    def getPublicKey(account):
        pass

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
    pubkey, privkey = KeyService.generate_keys()
    print(pubkey)
    # from the public key object to binary file
    pem_pubkey = KeyService.save_pubkey(pubkey)
    # from the binary file to public key object
    red_pubkey = KeyService.load_pubkey(pem_pubkey)
    print(red_pubkey)
