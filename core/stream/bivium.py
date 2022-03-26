import numpy as np

"""
Bivium - алгоритм - небольшое упрощение trivium
"""

class Bivium:


    """
    Циклический сдвиг
    """
    @staticmethod
    def _shift(arr, b):
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = b
        return arr


    """
    Функция обратной связи для регистра X
    """
    @staticmethod
    def _bx(arr_x, arr_y):
        return arr_x[65] ^ arr_x[92] ^ arr_x[90] ^ arr_x[91] ^ arr_y[77]

    """
    Функция обратной связи для регистра Y
    """
    @staticmethod
    def _by(arr_x, arr_y):
        return arr_x[68] ^ arr_y[83] ^ arr_y[81] ^ arr_y[82] ^ arr_y[68]

    """
    Функция выхода
    """
    @staticmethod
    def _z(arr_x, arr_y):
        return arr_x[27] ^ arr_x[0] ^ arr_y[0] ^ arr_y[15]

    @staticmethod
    def keystream(X, Y, l):
        res = [0 for i in range(0, l)]
        for i in range(0, l):
            res[i] = Bivium._z(X, Y)
            Xt = Bivium._shift(X, Bivium._bx(X, Y))
            Yt = Bivium._shift(Y, Bivium._by(X, Y))
            X = Xt
            Y = Yt
        return res

    @staticmethod
    def encrypt(text, key):
        X = key[0]
        Y = key[1]
        gamma = Bivium.keystream(X, Y, len(text))
        return [text[i] ^ gamma[i] for i in range(0, len(text))]

    @staticmethod
    def decrypt(gamma):
        l = len(gamma)
        x = [0 for i in range(0, 4*l + 177)]
        y = [0 for i in range(0, 4 * l + 177)]
        z = [0 for i in range(0, 4 * l + 177)]
        r = []
        rb = []
        for i in range(0, l):
            x[i + 0] = 1
            x[i + 27] = 1
            x[2*l + 177 + i] = 1
            x[l + 92 + i + 6] = 1

            y[i + 24] = 1
            y[l + 92 + i + 0] = 1
            y[l + 92 + i + 15] = 1
            y[3*l + 177 + i] = 1

            z[i + 27] = 1
            z[i + 0] = 1
            z[l + 92 + i + 15] = 1
            z[l + 92 + i + 0] = 1

            r.append(x)
            r.append(y)
            r.append(z)
            rb.append(0)
            rb.append(0)
            rb.append(gamma[i])

        a = np.array(r)
        b = np.array(rb)
        x = np.linalg.solve(a, b)
        return x[0:l + 92], x[l + 92:2*l + 177]


if __name__ == '__main__':

    X = [1 for i in range(0, 93)]
    Y = [0 for i in range(0, 84)]
    Xc, Yc = Bivium.decrypt(Bivium.keystream(X, Y, 177))
    print(Xc)
    print(Yc)
