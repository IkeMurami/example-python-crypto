# Тест Фридмана (каппа-тест) оценки длины ключа и поиск самого ключа

# Значение можно назвать точным, при длине > 1350 символов (можно искусственно удлинять тест (дублируя его))
def TestFriedman(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = list()
    sum = 0
    kp = 0.067 # Вероятность того, что два случайных символа совпадут в тексте (на английском языке)
    kr = 1 / len(alphabet)
    for ch in alphabet:
        count = len(text) - len(text.replace(ch, ''))
        sum += (count*(count-1))
    N = len(text)
    k0 = sum / (N * (N - 1))
    p = (kp - kr) / (k0 - kr)
    return p


t = 'KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST'
