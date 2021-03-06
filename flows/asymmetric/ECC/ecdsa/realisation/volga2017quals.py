# Представлена реализация ECDSA с таска Curved200 с VolgaCTF2017Quals
#!/usr/bin/env python
from __future__ import print_function
import os
import hashlib
from asymmetric.tools import numeric
"""
    Utils
"""


def import_public_key(keys_path):
    key_public = os.path.join(keys_path, 'key.public')
    assert (os.path.exists(key_public))
    with open(key_public, 'r') as f:
        data = f.read()
        d = data.split('\n')
        QAx = int(d[0])
        QAy = int(d[1])
        return QAx, QAy


def import_private_key(keys_path):
    key_private = os.path.join(keys_path, 'key.private')
    assert (os.path.exists(key_private))
    with open(key_private, 'r') as f:
        data = f.read()
        dA = int(data)
        return dA

"""
    Cipher
"""


class EllipticCurve(object):
    def __init__(self, a, b, p, n):
        self.a = a
        self.b = b
        self.p = p
        self.n = n

        self.discriminant = -16 * (4 * a * a * a + 27 * b * b)
        if not self.isSmooth():
            raise Exception("The curve %s is not smooth!" % self)

    def isSmooth(self):
        return self.discriminant != 0

    def testPoint(self, x, y, p):
        return (y ** 2) % p == (x ** 3 + self.a * x + self.b) % p

    def __str__(self):
        return 'y^2 = x^3 + %Gx + %G (mod %G)' % (self.a, self.b, self.p)

    def __eq__(self, other):
        return (self.a, self.b, self.p) == (other.a, other.b, other.p)


class Point(object):
    def __init__(self, curve, x, y):
        self.curve = curve
        self.x = x
        self.y = y
        if not curve.testPoint(x, y, curve.p):
            raise Exception("The point %s is not on the given curve %s" % (self, curve))

    def __neg__(self):
        return Point(self.curve, self.x, -self.y)

    def __add__(self, Q):
        if isinstance(Q, Ideal):
            return self
        x_1, y_1, x_2, y_2 = self.x, self.y, Q.x, Q.y
        if (x_1, y_1) == (x_2, y_2):
            if y_1 == 0:
                return Ideal(self.curve)
            s = (3 * x_1 * x_1 + self.curve.a) * int(numeric.inverse_mod(2 * y_1, self.curve.p))
        else:
            if x_1 == x_2:
                return Ideal(self.curve)
            s = (y_2 - y_1) * int(numeric.inverse_mod(x_2 - x_1, self.curve.p))
        x_3 = (s * s - x_2 - x_1) % self.curve.p
        y_3 = (s * (x_3 - x_1) + y_1) % self.curve.p
        return Point(self.curve, x_3, self.curve.p - y_3)

    def __sub__(self, Q):
        return self + -Q

    def __mul__(self, n):
        if n < 0:
            return -self * -n
        if n == 0:
            return Ideal(self.curve)
        else:
            Q = self
            R = self if n & 1 == 1 else Ideal(self.curve)
            i = 2
            while i <= n:
                Q = Q + Q
                if n & i == i:
                    R = Q + R
                i = i << 1
        return R

    def __rmul__(self, n):
        return self * n


class Ideal(Point):

    def __init__(self, curve):
        self.curve = curve

    def __str__(self):
        return "Ideal"

    def __neg__(self):
        return self

    def __add__(self, Q):
        return Q

    def __mul__(self, n):
        if not isinstance(n, int):
            raise Exception("Can't scale a point by something which isn't an int!")
        else:
            return self


class ECDSA(object):
    def __init__(self, g, priv):
        self.curve = g.curve
        self.g = g
        self.privkey = priv
        self.pubkey = priv * g
        self.Ln = len(bin(self.curve.n)[2:])
        assert priv < self.curve.n - 1

    def __str__(self):
        mes = "ECDSA with parameters:\n"
        mes += "CURVE:\n\t"
        mes += str(self.curve)
        mes += "\n\tOrder: {}\n".format(self.curve.n)
        mes += "\tG = ({}, {})\n".format(self.g.x, self.g.y)
        mes += "KEYS:\n"
        mes += "\tPrivate: {}\n".format(hex(self.privkey))
        mes += "\tPublic: ({}, {})\n".format(hex(self.pubkey.x), hex(self.pubkey.y))
        return mes

    def sign(self, mes):
        e = int(hashlib.sha512(mes).hexdigest(), 16)
        try:
            z = e >> (512 - self.Ln)
        except:
            raise Exception("Choose another curve with order smaller than 512")
        k = int(os.urandom(50).encode('hex'), 16) % self.curve.n
        xy = k * self.g
        r = xy.x % self.curve.n
        assert r != 0
        s = int(numeric.inverse_mod(k, self.curve.n) * (z + r * self.privkey) % self.curve.n)
        assert s != 0
        return r, s

    def verify(self, mes, r, s, pub):
        assert pub != Ideal(self.curve)
        assert str(self.curve.n * self.g) == "Ideal"
        if not (1 < r < self.curve.n - 1):
            return False
        if not (1 < s < self.curve.n - 1):
            return False
        e = int(hashlib.sha512(mes).hexdigest(), 16)
        try:
            z = e >> (512 - self.Ln)
        except:
            raise Exception("Choose another curve with order smaller than 512")
        w = numeric.inverse_mod(s, self.curve.n)
        u1 = int(z * w % self.curve.n)
        u2 = int(r * w % self.curve.n)
        xy = u1 * self.g + u2 * self.pubkey
        return r % self.curve.n == xy.x % self.curve.n


"""
	Curve parameters
"""

p = 39402006196394479212279040100143613805079739270465446667948293404245721771496870329047266088258938001861606973112319
n = 39402006196394479212279040100143613805079739270465446667946905279627659399113263569398956308152294913554433653942643
a = -3
b = int('b3312fa7e23ee7e4988e056be3f82d19181d9c6efe8141120314088f5013875ac656398d8a2ed19d2a85c8edd3ec2aef', 16)
NIST384 = EllipticCurve(a, b, p, n)


"""
	Generator
"""

Gx = int('aa87ca22be8b05378eb1c71ef320ad746e1d3b628ba79b9859f741e082542a385502f25dbf55296c3a545e3872760ab7', 16)
Gy = int('3617de4a96262c6f5d9e98bf9292dc29f8f41dbd289a147ce9da3113b5f0b8c00a60b1ce1d7e819d7a431d7c90ea0e5f', 16)
G = Point(NIST384, Gx, Gy)


"""
	Keys
"""

dA = import_private_key('.') # Файл  содержит только число - секретный ключ
QA = import_public_key('.') # файл содержит точку Q(x, y)
QA = Point(NIST384, QA[0], QA[1])

"""
    Main
"""

signature = ECDSA(G, dA)

