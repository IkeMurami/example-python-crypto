# -*- coding: UTF-8 -*-
# common
import os
from binascii import hexlify, unhexlify
from cryptography.hazmat.backends import default_backend
# sym
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
# other
from cryptography.hazmat.primitives import hashes, hmac

from core.kdf.kdf import KDF


"""
SQLCipher база может бытьь зашифрована по паролю, а может по ключу. 
getDBKey получает из пароля ключ
"""
class Crypto:
    def getDBKey(self, dbPassword, first16bytes):
        """
        SQLCipher: derive password
        first16byte - первые 16 байт зашифрованной бд
        """
        dbKey = KDF.pbkdf2_hmac_sha1(dbPassword, first16bytes, 32, 4000)
        return dbKey


# crypto = Crypto()
# crypto.getDBKey('737ac164813527baec9b924989100ebf975b994ca68795ff7c2aeb6f4908a910', unhexlify('C4C6B0090424F8658342A8BBB6D9FCFB'))

