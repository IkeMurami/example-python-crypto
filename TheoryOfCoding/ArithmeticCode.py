# Арифметический код
# https://neerc.ifmo.ru/wiki/index.php?title=Арифметическое_кодирование
from decimal import *
# Точность чисел
getcontext().prec = 150
# Частота встречаемости букв в алфавите
letters = [7, 7, 6, 5, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1 ,1, 1, 1, 1]
count = sum(letters)
# Наш отрезок [0, 1)
otrezok = [0]
for i in range(0, len(letters)):
    otrezok.append(Decimal(otrezok[-1]) + Decimal(letters[i]) / Decimal(sum(letters)))
# Закодированное арифметическим кодом сообщение
code = Decimal('0.868516383793554551020788061040565942198772113518651056879523592604008266287258119575459211858508598089343165930071849266364704413601432779618568252927')

# Декодирует один символ и нормирует отрезок
def decode(otr, num):
    gran = 0
    for i in range(0, len(otr)):
        if otr[i + 1] >= num:
            gran =  i
            break
    diapazon = otr[gran + 1] - otr[gran]
    start = otr[gran]
    for i in range(0, len(otr)):
        otr[i] = Decimal(start) + Decimal(diapazon) * Decimal(otrezok[i])
    return otr, gran

# Запускаем декодинг на щаданную глубину count (количество символов в сообщении закодированном)
otr = otrezok.copy()
res = []
for i in range(0, count):
    otr, pos = decode(otr, code)
    res.append(pos)

print(res)
