# Тест Касиски (Kasiski 1863, Babage - 1854)
from asymmetric.tools import numeric
ct = 'KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST'

def get_t_gramms(mes, t):
    t_gramms = dict()
    for i in range(0, len(mes) - t + 1):
        if mes[i : i + t] in t_gramms.keys():
            t_gramms[mes[i : i + t]].append(i)
        else:
            t_gramms[mes[i : i + t]] = [i]
    return t_gramms
def gcdlist(l):
    # НОД от попарных разностей
    s = l[1] - l[0]
    for i in range(2, len(l)):
        s = numeric.gcd(s, l[i] - l[i-1])
    return s
d = dict()
for length in range(3, 10):
    t_gramms = get_t_gramms(ct, length)
    flag = True
    for s in t_gramms.values():
        if len(s) > 1:
            nod = gcdlist(s)
            if nod % length != 0:
                flag = False
                break
    if flag:
        print(length)
