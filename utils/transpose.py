from typing import List


"""
Переворачивает таблицу

before = [b'0x010203', 
          b'0x040506']
     
after = [[1, 4],
         [2, 5],
         [3, 6]]
"""


def transpose(array: List[bytes]) -> List[List]:
    res = []

    length = len(array[0])

    for i in range(0, length):
        res.append([])

    for block in array:
        for index in range(0, len(block)):
            res[index].append(block[index])

    return res