from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac


class Hash:
    @staticmethod
    def sha1(msg):
        digest = hashes.Hash(hashes.SHA1(), backend=default_backend())
        digest.update(msg.encode())
        return digest.finalize()

    @staticmethod
    def sha256(msg):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(msg)
        return digest.finalize()

    @staticmethod
    def md5(msg):
        md5 = hashes.Hash(hashes.MD5(), backend=default_backend())
        md5.update(msg)
        return md5.finalize()
