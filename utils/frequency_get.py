"""
Выводит частоту символов для массива байтов

convertToAscii — при выводе символов в кконсоль, пробовать их перевести в ascii-символы
toPrint - выводить в консоль

Возвращает словарь: ключи — символы, значения — сколько раз встретились в массиве байтов
"""


def frequency(array: bytes, convertToAscii=False, toPrint=False):
    freq_dict = dict()

    for a in array:
        if a not in freq_dict:
            freq_dict[a] = 0

        freq_dict[a] += 1

    res = dict()

    # Сортируем словарь по значению в обратном порядке
    for value in sorted(freq_dict, key=freq_dict.get, reverse=True):

        if toPrint:
            print(
                chr(value)
                if convertToAscii else value,

                freq_dict[value]
            )

        res[value] = freq_dict[value]

    return res