m = 0
i = 0
j = 0
N = 256
S = [0 for i in range(0, N)]
def transposition(i, j):
    f = S[i]
    S[i] =S[j]
    S[j] = f
def KSA(key, iv):
    m = len(key)
    for i in range(0, N):
        S[i] = i
    j = 0
    for i in range(0, 768):
        i = i % N
        j = S[(j + S[i]+key[i % m]) % N]
        transposition(i, j)
    for i in range(0, 768):
        i = i % N
        j = S[(j + S[i] + iv[i % m]) % N]
        transposition(i, j)
    i = 0

def PRGA(state):
    j = state[1]
    i = state[0]
    S = state[2]
    j = S[(j+S[i])%N]
    z = S[(S[S[j]]+1)%N]
    transposition(i, j)
    i = (i + 1) % N
    return (z, (i, j, S))