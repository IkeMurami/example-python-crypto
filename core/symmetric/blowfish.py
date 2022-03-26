from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

"""
Blowfish — криптографический алгоритм, реализующий блочное симметричное шифрование с переменной длиной ключа. 
Разработан Брюсом Шнайером в 1993 году. 
Представляет собой сеть Фейстеля. 
"""
class BlowFish:
    @staticmethod
    def encrypt(key, plaintext):
        cipher = Cipher(algorithms.Blowfish(key), mode=None, backend=default_backend())
        encryptor = cipher.encryptor()
        return encryptor.update(plaintext)

    @staticmethod
    def decrypt(key, ciphertext):
        cipher = Cipher(algorithms.Blowfish(key), mode=None, backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext)
