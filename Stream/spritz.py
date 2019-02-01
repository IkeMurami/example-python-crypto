import binascii

def gcd(a, b):
    while a:
        a, b = b % a, a
    return b
def Swap(S, i, j):
    a = S[i]
    S[i] = S[j]
    S[j] = a
    return S

class SpritzCipher:
    def __init__(self, key, iv = None, n = 256):
        self.spritz = Spritz()
        self.spritz.InitializeState(n)
        self.spritz.Absorb(key)
        if iv:
            self.spritz.AbsorbStop()
            self.spritz.Absorb(iv)

    def encrypt(self, msg):
        gamma = self.spritz.Squeeze(len(msg))
        for i in range(0, len(msg)):
            gamma[i] = gamma[i] ^ msg[i]
        return gamma

    decrypt = encrypt


class Spritz:
    def __init__(self):
        self.w = self.n = self.i = self.j = self.k = self.a = self.z = 0
        self.S = []

    def InitializeState(self, n):
        self.i = self.j = self.k = self.a = self.z = 0
        self.n = n
        self.w = 1
        self.S = [v for v in range(0, n)]

    def Whip(self, r):
        for v in range(0, r):
            self.Update()

        self.w = (self.w + 1) % self.n
        while gcd(self.w, self.n) == 1:
            self.w = (self.w + 1) % self.n

    def Absorb(self, I):
        for v in range(0, len(I)):
            self.AbsorbByte(I[v])

    def Crush(self):
        for v in range(0, self.n // 2):
            if self.S[v] > self.S[self.n - 1 - v]:
                self.S = Swap(self.S, v, self.n - 1 - v)

    def AbsorbByte(self, b):
        self.AbsorbNibble(b % 16)
        self.AbsorbNibble(b >> 4)

    def AbsorbNibble(self, x):
        if self.a == self.n // 2:
            self.Shuffle()
        self.S = Swap(self.S, self.S[self.a], self.S[self.n // 2 + x])
        self.a = (self.a + 1) % self.n

    def AbsorbStop(self):
        if self.a == self.n // 2:
            self.Shuffle()
        self.a = (self.a + 1) % self.n

    def Squeeze(self, r):
        if self.a > 0:
            self.Shuffle()
        return [self.Drip() for v in range(0, r)]

    def Drip(self):
        if self.a > 0:
            self.Shuffle()
        self.Update()
        return self.Output()

    def Shuffle(self):
        self.Whip(self.n << 1)
        self.Crush()
        self.Whip(self.n << 1)
        self.Crush()
        self.Whip(self.n << 1)
        self.a = 0

    def Update(self):
        self.i = (self.i + self.w) % self.n
        self.j = (self.k + self.S[(self.j + self.S[self.i]) % self.n]) % self.n
        self.k = (self.i + self.k + self.S[self.j]) % self.n
        self.S = Swap(self.S, self.S[self.i], self.S[self.j])

    def Output(self):
        self.z = self.S[(self.j + self.S[(self.i + self.S[(self.z + self.k) % self.n]) % self.n]) % self.n]
        return self.z


spritz = Spritz()
spritz.InitializeState(256)
K = [255, 255, 255, 255, 255, 255, 255, 255]
spritz.Absorb(K)
#### опционально
spritz.AbsorbStop()
IV = [0, 0, 0, 0, 0, 0, 0, 0]
spritz.Absorb(IV)
#####
print(spritz.Squeeze(10))

# test enc/dec
spritz_cipher = SpritzCipher(K, IV, 256)
enc = spritz_cipher.encrypt([31, 31, 31, 31])
print (enc)
spritz_cipher = SpritzCipher(K, IV, 256)
dec = spritz_cipher.encrypt(enc)
print (dec)
