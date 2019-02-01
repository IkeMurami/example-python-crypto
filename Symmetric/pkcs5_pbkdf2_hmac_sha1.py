import binascii
from aes import AES
from pbkdf2 import pbkdf2

salt = b'saltysalt'
password = b'peanuts' # v10
version = '763130'

iv = binascii.unhexlify('20202020202020202020202020202020')
ct = binascii.unhexlify('EEC0C69AB3D6265508153B6ED7AE325CBBA873317A5EC9EF084BDAEE781446B7')

key = pbkdf2().deriverKey(password, salt)
aes = AES()
pt = aes.decrypt(key, iv, 'CBC', ct)
print (binascii.hexlify(pt))