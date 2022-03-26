"""
Расстояние Хемминга — количество отличющихся бит в двух строках
"""
from utils.xor import xor_array


def hamming_distance(first: bytes, second: bytes) -> int:

    assert len(first) == len(second), 'Массивы разной длины'

    # XOR
    res = xor_array(first, second)
    
    hammingDistace = 0

    # Считаем 1
    for val in res:
        hammingDistace += len(
            bin(val)
            .replace('0b', '')
            .replace('0', '')
        )

    return hammingDistace


def _test():
    assert hamming_distance(b'this is a test', b'wokka wokka!!!') == 37, 'A calculation error in Hamming distance function'