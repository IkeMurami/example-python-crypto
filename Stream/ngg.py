class State:
    def __init__(self, m, a):
        self.i = 0
        self.j = 0
        self.b = a

    def transposition(self, k, l):
        s = self.b[k]
        self.b[k] = self.b[l]
        self.b[l] = s

class NGG:
    # n - количество элементов в перестановке b, a - нач перестановка, в RC4 - это нули
    # m - размер элементов, например байт = 256
    def __init__(self, key, a, n, m):
        self.n = n
        self.m = m
        self.state = self.BeginState(key, a)
        self.key = key

    def BeginState(self, key, a):
        bState = State(self.n, a)
        for t in range(1, self.n + 1):
            bState.i = t - 1
            bState.j = (bState.j + bState.b[bState.i] + key[(t-1) % len(key)]) % self.m
            bState.transposition(bState.i, bState.j)
            bState.b[bState.i] = (bState.b[bState.i] + bState.b[bState.j]) % self.m
        bState.i = 0
        bState.j = 0
        return  bState

    def Next(self):
        self.state.i = (self.state.i + 1) % self.n
        self.state.j = (self.state.j + self.state.b[self.state.i]) % self.n
        self.state.transposition(self.state.i, self.state.j)
        z = self.state.b[(self.state.b[self.state.i] + self.state.b[self.state.j]) % self.n]
        self.state.b[(self.state.b[self.state.i] + self.state.b[self.state.j]) % self.n] = (self.state.b[self.state.i] + self.state.b[self.state.j]) % self.m
        return  z

    # mes - massiv byte
    def Encrypt(self, mes):
        self.state = self.BeginState(self.key)
        for i in range(0, len(mes)):
            mes[i] = mes[i] ^ self.Next()
        return mes
