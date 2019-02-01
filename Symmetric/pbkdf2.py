import binascii
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# pbkdf2 hmac sha1 (pkcs5)
class pbkdf2:
    def deriverKey(self, password, salt):
        kdf = PBKDF2HMAC(algorithm=hashes.SHA1, length=16, salt=salt, iterations=1, backend=default_backend())
        key = kdf.derive(password)
        return key

"""
TEST
----

print(binascii.hexlify(pbkdf2().deriverKey(b'test', b'salt')))

--------
END TEST
"""