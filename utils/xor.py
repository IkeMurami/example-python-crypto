"""
Операции сложения массивов
"""


def xor_array(first: bytes, second: bytes) -> bytes:
    """
    xor двух масссивов одной длины
    """
    assert len(first) == len(second), 'Массивы разной длины'

    return bytes([a ^ b for a, b in zip(first, second)])


def xor_byte(array: bytes, key: int) -> bytes:
    """
    xor массива с одним байтом
    """
    return bytes([a ^ key for a in array])


def xor_repeat(array: bytes, key: bytes) -> bytes:
    """
    xor массива с ключом (ключ добивается методом повторения до длины массива)
    """

    # Добиваем ключ до длины массива

    m = int(len(array) / len(key) + 1)
    key = (key * m)[:len(array)]

    return xor_array(array, key)