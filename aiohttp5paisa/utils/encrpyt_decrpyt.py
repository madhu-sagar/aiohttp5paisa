"""

"""

import base64
from Crypto.Cipher import AES
from pbkdf2 import PBKDF2


RAWSALT = [83, 71, 26, 58, 54, 35, 22, 11, 83, 71, 26, 58, 54, 35, 22, 11]
salt = str(bytes(RAWSALT).decode()).encode()
BS = 16

pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


def encrpyt(raw_value,encryption_key):

    
    raw_value = pad(raw_value)
    generator = PBKDF2(encryption_key,salt)
    aes_iv = generator.read(16)
    aes_key = generator.read(32)
   
    mode = AES.MODE_CBC
    cipher = AES.new(aes_key, mode, IV=aes_iv)
    return base64.b64encode(cipher.encrypt(raw_value)).decode()

def decrpyt(encrypted_value,encryption_key) :

    encrypted_value = base64.b64decode(encrypted_value)
    generator = PBKDF2(encryption_key, salt)
    aes_iv = generator.read(16)
    aes_key = generator.read(32)
    mode = AES.MODE_CBC
    cipher = AES.new(aes_key, mode, IV=aes_iv)
    return unpad(cipher.decrypt(encrypted_value))


