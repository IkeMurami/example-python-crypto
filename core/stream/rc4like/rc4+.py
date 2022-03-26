m = 0
l = 0
i = j = 0
N = 256
S = [0 for i in range(0, N)]
def transposition(i, j):
    f = S[i]
    S[i] =S[j]
    S[j] = f
def KSA(key, iv):
    m = len(key)
    l = len(iv)
    for i in range(0, N):
        S[i] = i
    j = 0
    for i in range(0, N):
        j = (j + S[i] + key[i % m]) % N
        transposition(i, j)
    for i in range( N / 2-1, -1, -1):
        j = ((j + S[i])%N) ^ ((key[i%m] + iv[i%l])%N)
        transposition(i, j)
    for i in range(N/2, N):
        j = ((j + S[i]) % N) ^ ((key[i % m] + iv[i % l]) % N)
        transposition(i, j)
    i = 0
    for y in range(0, N):
        if y % 2 == 0:
            i = y / 2
        else:
            i = N-(y+1)/2
        j = (j + S[i] + key[i%m]) % N
        transposition(i, j)
    i = j = 0
    return S
def PRGA(state):
    i = (state[0] + 1) % N
    S = state[3]
    j = (state[1] + S[i])%N
    transposition(i, j)
    t = (S[i]+S[j])%N
    t1 = ((S[((i >> 3) ^ (j << 5))% N]+S[((i << 5) ^ (j >> 3))% N])^int("AA", 16))%N
    t2 = (j + S[j])%N
    z = ((S[t]+S[t1])%N)^S[t2]
    return (z, [i, j, S])