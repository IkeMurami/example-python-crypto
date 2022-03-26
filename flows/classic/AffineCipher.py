# Аффинный шифр
class AffineCipher:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.lowercase = 97

    # k = (a, b, mod)
    # m - lowercase
    def encrypt(self, m, k):
        res = ''
        for ch in m:
            res += self.alphabet[((ord(ch)-self.lowercase)*k[0]+k[1]) % k[2]]
        return res


m = 'kqerejebcppcjcrkieacuzbkrvpkrbcibqcarbjcvfcupkriofkpacuzqepbkrxpeiieabdkpbcpfcdccafieabdkpbcpfeqpkazbkrhaibkapcciburccdkdccjcidfuixpafferbiczdfkabicbbenefcupjcvkabpcydccdpkbcocperkivkscpicbrkijpkabi'

ac = AffineCipher()
print(ac.encrypt(m, (11, 8, 26)))
