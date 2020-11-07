from Crypto.Cipher import AES


class AesWrap:
    def __init__(self, encryption_method, key, iv):
        self.cipher = AES.new(key, AES.MODE_ECB, iv) if encryption_method == "ecb" else AES.new(key, AES.MODE_CFB,
                                                                                          iv) if encryption_method == "cfb" else "none"

    def encrypt(self, plain):
        if self.cipher != "none":
            return self.cipher.encrypt(plain)
        return 'error'

    def decrypt(self, ciphertext):
        if self.cipher != "none":
            return self.cipher.decrypt(ciphertext)