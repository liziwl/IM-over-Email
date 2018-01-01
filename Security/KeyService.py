import rsa
import gnupg



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
        compare_uid = "<"+account+">"
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
    def generate_keys(name, email_address, password):
        gpg = gnupg.GPG(homedir='~/.gnupg')
        user_input = gpg.gen_key_input(name_real=name, name_email=email_address, passphrase=password)
        user_key = gpg.gen_key(user_input)
        # send public key to server
        gpg.send_keys('hkp://pgp.mit.edu', user_key.key_id)
        return user_key

    @staticmethod
    def getPublicKey(account):
        gpg = gnupg.GPG()
        key_information = gpg.search_keys(account, 'hkp://pgp.mit.edu')
        public_key = gpg.export_keys(key_information[0]["keyid"])
        return public_key

    @staticmethod
    def getPrivateKey(account):
        compare_uid = "<" + account + ">"
        gpg = gnupg.GPG()
        user_keys = gpg.list_keys()
        for key_array in user_keys:
            uid = key_array["uids"][0].split(' ', 1)[1]
            if compare_uid == uid:
                private_key_fingerprint=key_array["fingerprint"]
                private_key=gpg.export_keys(private_key_fingerprint,True)
        return private_key

    @staticmethod
    def save_privkey(account, format='PEM'):
        private_key=KeyService.getPrivateKey(account)
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

    print(KeyService.generate_keys())
    # from the public key object to binary file
    # pem_pubkey = KeyService.save_pubkey(pubkey)
    # from the binary file to public key object
    # red_pubkey = KeyService.load_pubkey(pem_pubkey)
    # print(red_pubkey)
    # print(pem_pubkey)
