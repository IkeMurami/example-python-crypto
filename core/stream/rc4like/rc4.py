class State:
    def __init__(self, m):
        self.i = 0
        self.j = 0
        self.b = [i for i in range(0, m)]

    def transposition(self, k, l):
        s = self.b[k]
        self.b[k] = self.b[l]
        self.b[l] = s

class RC4:
    # m - количество элементов в перестановке b
    def __init__(self, key, m):
        self.m = m
        self.state = self.BeginState(key)
        self.key = key

    def BeginState(self, key):
        bState = State(self.m)
        for t in range(1, self.m + 1):
            bState.i = t - 1
            bState.j = (bState.j + bState.b[bState.i] + key[(t-1) % len(key)]) % self.m
            bState.transposition(bState.i, bState.j)
        bState.i = 0
        bState.j = 0
        return  bState

    def Next(self):
        self.state.i = (self.state.i + 1) % self.m
        self.state.j = (self.state.j + self.state.b[self.state.i]) % self.m
        self.state.transposition(self.state.i, self.state.j)
        return self.state.b[(self.state.b[self.state.i] + self.state.b[self.state.j]) % self.m]

    # mes - massiv byte
    def Encrypt(self, mes):
        self.state = self.BeginState(self.key)
        for i in range(0, len(mes)):
            mes[i] = mes[i] ^ self.Next()
        return mes

rc4 = RC4([2, 3, 1, 0, 2, 3, 1, 0, 1, 1], 10)
rc4.state.b = [8, 1, 4, 6, 0, 9, 3, 2, 7, 5]
rc4.state.j = 1
res = ''
for i in range(0, 90):
    res += str(rc4.Next())
print(res)
