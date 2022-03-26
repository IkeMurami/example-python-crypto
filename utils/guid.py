import os
from binascii import hexlify


"""
Generate correct GUID/UUID
"""


def guid():
    string = bytearray(os.urandom(16))

    string = string[:6] + bytearray([string[6] & 0xf | 0x40]) + \
             bytearray([string[7]]) + bytearray([string[8] & 0x3f | 0x80]) + \
             string[9:]

    string = hexlify(string).decode()
    string = f'{string[:8]}-{string[8:12]}-{string[12:16]}-{string[16:20]}-{string[20:]}'
    return string