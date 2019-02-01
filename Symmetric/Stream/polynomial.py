class Polynomial(list):
    def __str__(self):
        L = ['{}*x^{}'.format(e, i) for i,e in enumerate(self)]
        return ' + '.join(L)

    def __add__(self, other):
        if len(self) < len(other):
              return other + self
        else:
            k = len(self) - len(other)
            new = [a^b for (a,b) in zip(self,([0]*k)+other)]
            try:
                while new[0] == 0:
                    new.pop(0)
            except IndexError:
                new = []
            return Polynomial(new)

    def dot(self,S):
        """ This returns the sum of ck*S{N-k} where N+1 = len(S),
            and k runs from 0 to m-1 (m is my degree)
        """
        m = len(self)
        N = len(S)
        C = self[:-1]
        S = S[N-m+1:]
        return dot(C,S)

    def __mul__(self,other):
        deg = len(self) + len(other) - 2
        prod = [0]*(deg + 1)
        for k,x in enumerate(self):
            for j,y in enumerate(other):
                prod[k+j] ^= (x&y)
        return Polynomial(prod)

    def __pow__(self,ex):
        if ex==0:
            return Polynomial([1])
        else:
            return self*(self**(ex-1))

def xor(a, b):
    return a ^ b

def dot(x, y):
        """Returns the dot product of two lists."""
        return reduce(xor, [a&b for (a,b) in zip(x,y)], 0)