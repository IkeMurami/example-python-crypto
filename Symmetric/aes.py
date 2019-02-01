from binascii import hexlify, unhexlify
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import binascii


class AES:


    def decryptCBC(self, key, iv, db):
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(db) + decryptor.finalize()
        return plaintext

    def decryptECB(self, key, ciphertext):
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext


from cryptography.hazmat.primitives import serialization
e = 65537
n = 71521286555472299312252291246589709247849481750774732993492805730954699131789
p = 273130256889334854338089243490350662083
q = 261857794043121448213410325750790838383
d = 66043993770909144601963534517312602411294055720082623568097196488923525348009
c = 49261759487956473329685313812271645883131850171569790962655880778772489980709
def testKey(key):
    if len(hex(key)[2:]) == 64:
        return True
    return False

key = pow(c, d, n)
mbKeys = []
if testKey(key):
    mbKeys.append(key)
key += n
if testKey(key):
    mbKeys.append(key)
key += n
if testKey(key):
    mbKeys.append(key)
key += n
if testKey(key):
    mbKeys.append(key)
key += n
if testKey(key):
    mbKeys.append(key)
key += n


aes = AES()
key = binascii.unhexlify(hex(mbKeys[0])[2:])
msg = binascii.unhexlify('10DECE6C28C5722F42A2FD966663AF6EF38838B2F07E748B049C8C852CD6B344')
res = aes.decryptECB(key, msg)
pass

