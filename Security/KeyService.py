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

    # encode the key to some format
    @staticmethod
    def encode_key(key):
        raise NotImplementedError

    # decode the key to some format
    @staticmethod
    def decode_key(key):
        raise NotImplementedError

    # get the rsa key object from input key format
    @staticmethod
    def get_key_object(key):
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
