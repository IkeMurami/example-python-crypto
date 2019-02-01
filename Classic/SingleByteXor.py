import binascii
from misc.tools.operations import xor, score

def singleByteXor(hexString):
    for ch in range(0, 255):
        key = [ch for i in range(0, len(hexString))]
        res = xor(key, hexString)
        print(res)
    return None

print(singleByteXor(binascii.unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')))