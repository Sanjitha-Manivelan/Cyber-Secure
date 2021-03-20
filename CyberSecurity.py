from Crypto import Random
from Crypto.Cipher import AES
import pyaes, pbkdf2, binascii, secrets
import os

class cyberSecurity:
    def __init__(self, pword):
        pw = pword
        pwsalt = os.urandom(16)
        self.key = pbkdf2.PBKDF2(pw, pwsalt).read(32)

    def padding(self, msg):
        return msg + b"\0" * (AES.block_size - len(msg) % AES.block_size)

    def encrypt(self, msg, key, key_size=256):
        msg = self.padding(msg)
        randomvalue = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, randomvalue)
        return randomvalue + cipher.encrypt(msg)

    def encryptFile(self, fileName):
        with open(fileName, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(fileName + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(fileName)

    def decrypt(self, ciphertext, key):
        cyphervalue = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, cyphervalue)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decryptFile(self, fileName):
        with open(fileName, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(fileName[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(fileName)
