from cryptography.hazmat.primitives import padding

"""
PKCS7 Padding
"""


def padding_pkcs7(data, bit_length=128):
    padder = padding.PKCS7(bit_length).padder()
    data = padder.update(data)
    return data + padder.finalize()


def unpadding_pkcs7(data, bit_length=128):
    unpadder = padding.PKCS7(bit_length).unpadder()
    data = unpadder.update(data)
    return data + unpadder.finalize()