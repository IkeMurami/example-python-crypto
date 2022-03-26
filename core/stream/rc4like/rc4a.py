from .rc4 import RC4


class State:
    def __init__(self, m):
        self.i = 0
        self.j1 = 0
        self.j2 = 0
        self.s1 = [i for i in range(0, m)]
        self.s2 = [i for i in range(0, m)]

    def transposition(self, k, l, s=1):
        if s == 1:
            s = self.s1[k]
            self.s1[k] = self.s1[l]
            self.s1[l] = s
        else:
            s = self.s2[k]
            self.s2[k] = self.s2[l]
            self.s2[l] = s

class RC4A:
    # m - количество элементов в перестановке b
    def __init__(self, key, m):
        self.m = m
        self.state = self.BeginState(key)
        self.key = key

    def BeginState(self, key):
        bState = State(self.m)
        rc4 = RC4(key, self.m)
        bState.s1 = rc4.state.b
        key2 = [0 for i in range(0, self.m)]
        for i in range(0, self.m):
            key2[i] = rc4.Next()
        rc4 = RC4(key2, self.m)
        bState.s2 = rc4.state.b
        return  bState

    def Next(self):
        self.state.i = (self.state.i + 1) % self.m
        self.state.j1 = (self.state.j1 + self.state.s1[self.state.i]) % self.m
        self.state.transposition(self.state.i, self.state.j1)
        z1 = self.state.s2[(self.state.s1[self.state.i] + self.state.s1[self.state.j1]) % self.m]

        self.state.i = (self.state.i + 1) % self.m
        self.state.j2 = (self.state.j2 + self.state.s2[self.state.i]) % self.m
        self.state.transposition(self.state.i, self.state.j2, 2)
        z2 = self.state.s1[(self.state.s2[self.state.i] + self.state.s2[self.state.j2]) % self.m]
        return [z1, z2]

    # mes - massiv byte
    def Encrypt(self, mes):
        self.state = self.BeginState(self.key)
        for i in range(0, len(mes), 2):
            z = self.Next()
            mes[i] = mes[i] ^ z[0]
            mes[i+1] = mes[i+1] ^ z[1]
        return mes
