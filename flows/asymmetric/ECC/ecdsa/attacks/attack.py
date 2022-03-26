"""
Атака на ECDSA
Возможна если параметр r не меняется при подписи
Подробнее: http://www.nilsschneider.net/2013/01/28/recovering-bitcoin-private-keys.html
"""
import hashlib
from asymmetric.tools import numeric
# Такой хеш был в таске Curved200 на VolgaCTF2017Quals, Так то он мб любым
def customhash(mes):
    return int(hashlib.sha512('exit').hexdigest(), 16) >> 128
n = 39402006196394479212279040100143613805079739270465446667946905279627659399113263569398956308152294913554433653942643
s1 = 34855921360927916070986212109819500225655651650874609025244135362773790814285754503375195745383314214044123943832259
s2 = 30319268030018639511551117879575625408953110962874264740912972950968883326846458408981004916433253051594118273327537
r = 9540946282644423304958237178123966732301592745413906651991128246584667628620778601005222874778554839816137094172414
z1 = customhash('exit')
z2 = customhash('leave')
sdiff_inv = numeric.inverse_mod(((s1 - s2) % n), n)
k = (((z1 - z2) % n) * sdiff_inv) % n
r_inv = numeric.inverse_mod(r, n)
da = (((((s1 * k) % n) - z1) % n) * r_inv) % n

print ("Recovered Da: " + str(da))