from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class AES:
    @staticmethod
    def decrypt(key, data, iv=None, nonce=None, tag=None, aad=None):
        algorithm = algorithms.AES(key)

        if not iv:
            if not nonce:
                mode = modes.ECB()
            else:
                mode = modes.CTR(nonce)
        elif tag:
            mode = modes.GCM(iv, tag)
        else:
            mode = modes.CBC(iv)
        cipher = Cipher(algorithm, mode, backend=default_backend()).decryptor()
        if aad:
            cipher.authenticate_additional_data(aad)
        plaintext = cipher.update(data) + cipher.finalize()
        return plaintext

    @staticmethod
    def encrypt(key, data, iv=None, nonce=None, aad=None):
        algorithm = algorithms.AES(key)

        if not iv:
            if not nonce:
                mode = modes.ECB()
            else:
                mode = modes.CTR(nonce)
        elif aad:
            mode = modes.GCM(iv)
        else:
            mode = modes.CBC(iv)
        cipher = Cipher(algorithm, mode, backend=default_backend()).encryptor()
        if aad:
            cipher.authenticate_additional_data(aad)
        ciphertext = cipher.update(data) + cipher.finalize()
        if aad:
            return ciphertext, cipher.tag
        else:
            return ciphertext

    # aes-ige in apk/Telegram/* (mb wrong)

    # OCB-AES
    """
    from ocb.aes import AES as AESOCB
    from ocb import OCB
    aes = AESOCB(256)
    ocb = OCB(aes)
    ocb.setKey(bytearray().fromhex('aaaaaaaa..aaa'))
    ocb.setNonce(bytearray().fromhex('aaaaaaaa..aaa'))
    (tag, ciphertext) = ocb.encrypt(bytearray('plaintext'), bytearray('aad'))
    (is_authentic, plaintext) = ocb.decrypt(b'aad', ciphertext, tag)
    """
