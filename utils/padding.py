from cryptography.hazmat.primitives import padding

"""
PKCS7 Padding
"""


def padding_pkcs7(data):
    padder = padding.PKCS7(128).padder()
    data = padder.update(data)
    return data + padder.finalize()


def unpadding_pkcs7(data):
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(data)
    return data + unpadder.finalize()