from core.theory_of_coding.hamming_distance import hamming_distance
from utils.transpose import transpose
from utils.xor import xor_byte


def challenge6(enc=b'blablalb blalba blssv'):
    """
    Break repeating XOR
    1. Надо вычислить длину ключа KEYSIZE
        1.1 Для KEYSIZE от 2 до 40
        1.2 Берем у зашифрованного текста первый блок длины KEYSIZE и второй блок длины KEYSIZE.
        1.3 Считаем расстояние Хемминга и делим на значение KEYSIZE для нормализации результата
        1.4 Значения с наименьшими показателями нормализованного расстояния Хемминга вероятно будут ключами (можно рассмотрет 2-3 значения).
        1.4* Или можно в пункте 1.2 просчитывать не для 2-х блоков, а для 4-х, например
    2.  Теперь разбиваем зашифрованный текст на блоки длины KEYSIZE
    3. Составляем новую таблицу блоков методом транспозиции: 1-й блок — все первые байты блоков из п.2, 2-й блок — все 2-е байты и тд
    4. Для каждого блока решаем задачу поиска ключа (Single Byte XOR): выбираем те значения, гистограмма для которых лучше (частотность близка к реальной)
    5.
    """

    assert hamming_distance(b'this is a test',
                            b'wokka wokka!!!') == 37, 'Error in calculation Hamming distace function'

    enc_data = enc

    res = dict()

    for KEYSIZE in range(1, 40):
        res[KEYSIZE] = hamming_distance(enc_data[:KEYSIZE], enc_data[KEYSIZE: KEYSIZE * 2])

    KEYSIZE = 5

    blocks = [enc_data[i:i + KEYSIZE] for i in range(0, len(enc_data), KEYSIZE)]

    transpose_blocks = transpose(blocks)

    enc = bytes(transpose_blocks[0])
    for i in range(0, 255):
        print(xor_byte(enc, i)[:20])

    # print(transpose_blocks)
    print(res)
    # print(enc_data)