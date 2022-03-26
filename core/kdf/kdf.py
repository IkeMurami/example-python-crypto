from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


class KDF:
    # bcrypt in bcrypt.py
    @staticmethod
    def scrypt(password, salt, power, hash_len):
        kdf = Scrypt(salt=salt, length=hash_len, n=2 ** power, r=8, p=1, backend=default_backend())
        key = kdf.derive(password)
        return key

    @staticmethod
    def pbkdf2_hmac_sha1(password, salt, length, iter):
        kdf = PBKDF2HMAC(algorithm=hashes.SHA1, length=length, salt=salt, iterations=iter, backend=default_backend())
        key = kdf.derive(password)
        return key

    @staticmethod
    def hmac_sha256(key, data):
        h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
        h.update(data)
        return h.finalize()

    @staticmethod
    def hmac_sha1(key, data):
        h = hmac.HMAC(key, hashes.SHA1(), backend=default_backend())
        h.update(data)
        return h.finalize()

    @staticmethod
    def PBE_S1(password, salt, length):
        res = ''
        buf = ''
        while len(res) < length:
            buf = KDF.md5(buf + password + salt)
            res += buf
        key = res[:length]
        return key

    # PBE2WithSHA256
    @staticmethod
    def PKCS12v1_KDF_SHA256(password, salt, iterations, keylen, mode=1):
        def PBKDF_Adjust(a, aOffset, b):
            x = (b[len(b) - 1] & 0xff) + (a[aOffset + len(b) - 1] & 0xff) + 1
            a[aOffset + len(b) - 1] = x & 0xff

            x = x >> 8

            for i in range(len(b) - 2, -1, -1):
                x = x + (b[i] & 0xff) + (a[aOffset + i] & 0xff)
                a[aOffset + i] = x & 0xff
                x = x >> 8
        # rfc7292#appendix-B
        import hashlib
        hash_alg = hashlib.sha256
        v = 64
        u = 32
        r = iterations
        c = 0
        digest = bytearray(u)
        B = bytearray(v)
        key = bytearray(keylen)

        # Step 1
        Dlen = v
        D = bytearray(Dlen)

        for i in range(0, 64):
            D[i] = mode

        # Step 2
        Slen = v * ((len(salt) + v - 1) / v)
        S = bytearray(Slen)

        i = 0
        while (i != v * ((len(salt) + v - 1) / v)):
            S[i] = salt[i % len(salt)]
            i = i + 1

        # Step 3
        Plen = v * ((len(password) + v - 1) / v)
        P = bytearray(Plen)

        i = 0
        while (i != v * ((len(salt) + v - 1) / v)):
            P[i] = password[i % len(password)]
            i = i + 1

        # Step 4
        Ilen = Slen + Plen
        I = S + P

        # Step 5
        c = (keylen + u - 1) / u

        # Step 6
        for i in range(1, c + 1):
            # Step 6 - a
            hash_obj = hash_alg()
            hash_obj.update(D)
            hash_obj.update(I)
            digest = hash_obj.digest()

            for j in range(0, r - 1):
                hash_obj = hash_alg()
                hash_obj.update(digest)
                digest = hash_obj.digest()

            # Step 6 - b
            for k in range(0, v):
                B[k] = digest[k % u]

            # Strp 6 - c
            for j in range(0, Ilen / v):
                PBKDF_Adjust(I, j * v, B)

            if (i == c):
                for j in range(0, keylen - ((i - 1) * u)):
                    key[(i - 1) * u + j] = digest[j]
            else:
                for j in range(0, u):
                    key[(i - 1) * u + j] = digest[j]

        # print binascii.hexlify(key)
        keystr = []
        for ch in key:
            keystr.append(chr(ch))
        return "".join(keystr)

    # PBE2WithSHA1
    @staticmethod
    def PKCS12v1_KDF_SHA1(password, salt, iterations, keylen, mode=1):
        def PBKDF_Adjust(a, aOffset, b):
            x = (b[len(b) - 1] & 0xff) + (a[aOffset + len(b) - 1] & 0xff) + 1
            a[aOffset + len(b) - 1] = x & 0xff

            x = x >> 8

            for i in range(len(b) - 2, -1, -1):
                x = x + (b[i] & 0xff) + (a[aOffset + i] & 0xff)
                a[aOffset + i] = x & 0xff
                x = x >> 8
        # rfc7292#appendix-B
        import hashlib
        hash_alg = hashlib.sha1
        u = 20
        v = 64
        r = iterations
        c = 0
        digest = bytearray(u)
        B = bytearray(v)
        key = bytearray(keylen)

        # Step 1
        Dlen = v
        D = bytearray(Dlen)

        for i in range(0, v):
            D[i] = mode

        # Step 2
        Slen = v * ((len(salt) + v - 1) / v)
        S = bytearray(Slen)

        i = 0
        while (i != v * ((len(salt) + v - 1) / v)):
            S[i] = salt[i % len(salt)]
            i = i + 1

        # Step 3
        Plen = v * ((len(password) + v - 1) / v)
        P = bytearray(Plen)

        i = 0
        while (i != v * ((len(salt) + v - 1) / v)):
            P[i] = password[i % len(password)]
            i = i + 1

        # Step 4
        Ilen = Slen + Plen
        I = S + P

        # Step 5
        c = (keylen + u - 1) / u

        # Step 6
        for i in range(1, c + 1):
            # Step 6 - a
            hash_obj = hash_alg()
            hash_obj.update(D)
            hash_obj.update(I)
            digest = hash_obj.digest()

            for j in range(0, r - 1):
                hash_obj = hash_alg()
                hash_obj.update(digest)
                digest = hash_obj.digest()

            # Step 6 - b
            for k in range(0, v):
                B[k] = digest[k % u]

            # Strp 6 - c
            for j in range(0, Ilen / v):
                PBKDF_Adjust(I, j * v, B)

            if (i == c):
                for j in range(0, keylen - ((i - 1) * u)):
                    key[(i - 1) * u + j] = digest[j]
            else:
                for j in range(0, u):
                    key[(i - 1) * u + j] = digest[j]

        # print binascii.hexlify(key)
        keystr = []
        for ch in key:
            keystr.append(chr(ch))
        return "".join(keystr)

    # for PBE_S1
    @staticmethod
    def md5(msg):
        md5 = hashes.Hash(hashes.MD5(), backend=default_backend())
        md5.update(msg)
        return md5.finalize()
