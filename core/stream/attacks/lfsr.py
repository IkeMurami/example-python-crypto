import itertools
"""

f(x[1] .. x[n]) = a[n-1] x[n] + .. + a[1] x[2] + a[0] x[1]
F[X] = X^n - a[n-1] X^(n-1) - .. - a[1] X - a[0]

example:
        --->
gamma = 0, 1, 1, 0, 1, 1, 1, 0, 1
        --->
polynom = x^5+x^2+1
seed = bin(10110)
polynom = bin(00101) = bin(10100)
right shift
"""
def myLFSR(seed, polynom, length, lengthLFSR = 128):
    state = seed
    gamma = []
    for i in range(0, length):
        gamma.append(state & 1)
        newstate = len(bin(state & polynom)[2:].replace('0', '')) % 2
        state = (state >> 1) | (newstate << (lengthLFSR - 1))
    return gamma

def lsfr(seed, polynom):
    data = seed
    poly = polynom

    while 1:
        lsb = data & 1
        data = data >> 1
        if lsb != 0:
            data = data ^ poly
            yield 1
        else:
            yield 0

def getPoly():
    pol = [128, 127, 126, 123, 122, 120, 118, 109, 107, 106, 104, 102, 101, 100, 98, 97, 96, 91, 90, 89, 86, 83, 81, 80, 76, 71, 70, 68, 67, 65, 64, 62, 60, 59, 58, 51, 49, 48, 45, 43, 42, 41, 40, 39, 35, 30, 29, 27, 26, 23, 22, 21, 17, 16, 15, 12, 11, 10, 9, 8, 6, 3, 2, 0]
    length = pol[0]
    res = ''
    for i in range(pol[0] - 1, -1, -1):
        if i in pol:
            res += str(1)
        else:
            res += str(0)
    return res

def bin2hex(data):
    res = ''
    for i in range(0, len(data), 8):
        res += hex(int(data[i:i+8], 2))[2:].rjust(2, '0')
    return res
# test
polynom = getPoly()
result = '00100011100101111001100101011111001101100110001101010011111111110001000011101101000100111111111010110110110010011110111111001000111000110100111100001101001111011001000100001111101001000111110011110010000000100110011010101000000100011011010011010011100011010100001111101011010110000011001001111000010011111110101010001010110111111111000010100000100001110001010001001110100110000110101001011100110001010101010001111010101000111101111001100001110010111010011010011011100111010001101110110010010100101111001100010010010100010010001100010000100111111101111000100001'[::-1]
result = bin2hex(result)
iv = int('00010011111101111001001101101101011111111100100010110111000010001111111111001010110001100110110011111010100110011110100111000100', 2)
polynom = int(polynom, 2)
seed = 22
poly = 5
gamma = myLFSR(iv, polynom, 560, lengthLFSR = 128)
res = ''
for g in gamma:
    res += str(g)
print(res)
out = lsfr(seed, poly)
gamma = []
for i in out:
    gamma.append(i)
f = [1, 0, 1, 0, 0]
s = [1, 0, 1, 1, 1]
res = []
for i in range(0, 120):
    res.append(s[0])
    up = s[0] ^ s[2]
    for j in range(1, 5):
        s[j-1] = s[j]
    s[4] = up
print(res[110:])