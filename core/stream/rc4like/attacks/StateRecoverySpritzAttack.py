# Алгоритм восстановления начального состояния из гаммы, при условии, что мы попали в слабое состояние =>
# как я понял, мы можем восстановить это слабое состояние (внутреннюю перестановку), а может и целиком нач состояние?..
# На основе статьи Banik and Isobe "Cryptoanalysis of the Full Spritz Stream Cipher"
# Input гамма z[t], t = 0..10*N
# Output: Внутренняя перестановка в начале стадии SQUEEZE
N = 256
w = 7 # расчитывается по длине ключа и IV
z = [0 for t in range(0, 10*N)]
S = [None for t in range(0, N)]
def Swap(S, i, j):
    a = S[i]
    S[i] = S[j]
    S[j] = a
def StateRecovery(S, i, j, k, r):
    i = (i + w)%N
    for u1 in range(0, N):
        if S[i] == None and not(u1 in S) and u1 % 2 != i % 2:
            S[i] = u1

    a = (j + S[i])%N
    for u2 in range(0, N):
        if S[a] == None and not(u2 in S) and u2 % 2 != a % 2:
            S[a] = u2

    j = (j + S[a])%N
    for u3 in range(0, N):
        if S[j] == None and not(u3 in S) and u3 % 2 != j % 2:
            S[j] = u3

    k = (k + i + S[j])%N
    Swap(S, i, j)
    if r == 0:
        b = k
    else:
        b = (z[r-1] + k)%N
    for u4 in range(0, N):
        if S[b] == None and not (u4 in S) and u4 % 2 != b % 2:
            S[b] = u4

    c = (i + S[b]) % N
    for u5 in range(0, N):
        if S[c] == None and not (u5 in S) and u5 % 2 != c % 2:
            S[c] = u5

    d = (j + S[c]) % N
    if S[d] == None and not (z[r] in S):
        S[d] = z[r]
        StateRecovery(S, i, j, k, r + 1)
    if S[d] == None and z[r] in S:
        # Противоречие
        pass
    if S[d] != None and S[d] != z[r]:
        # Противоречие
        pass
    if S[d] != None and S[d] == z[r]:
        StateRecovery(S, i, j, k, r + 1)

# Предположение
S[0] = 0
# Как расчитывать j, k?
StateRecovery(S, 0, 0, 0, 0)