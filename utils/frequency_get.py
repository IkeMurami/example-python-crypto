"""
Выводит частоту символов для массива байтов

convertToAscii — при выводе символов в кконсоль, пробовать их перевести в ascii-символы
toPrint - выводить в консоль

Возвращает список пар: символы и частота появления в массиве байт.
Элементы расположены в порядке от самого встречаемого до самого редкого
"""
from typing import List, Tuple


def frequency(array: bytes, convertToAscii=False, toPrint=False) -> List[Tuple]:
    freq_dict = dict()

    for a in array:
        if a not in freq_dict:
            freq_dict[a] = 0

        freq_dict[a] += 1

    res = list()

    # Сортируем словарь по значению в обратном порядке
    for value in sorted(freq_dict, key=freq_dict.get, reverse=True):

        if toPrint:
            print(
                chr(value)
                if convertToAscii else value,

                freq_dict[value] / len(array)
            )

        res.append((value, freq_dict[value] / len(array)))

    return res