def rational_to_contfrac(x,y):
    '''
    Converts a rational x/y fraction into
    a list of partial quotients [a0, ..., an]
    '''
    a = x//y
    pquotients = [a]
    while a * y != x:
        x,y = y,x-a*y
        a = x//y
        pquotients.append(a)
    return pquotients

def convergents_from_contfrac(frac):
    '''
    computes the list of convergents
    using the list of partial quotients
    '''
    convs = [];
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0:i]))
    return convs

def contfrac_to_rational (frac):
    '''Converts a finite continued fraction [a0, ..., an]
     to an x/y rational.
     '''
    if len(frac) == 0:
        return (0,1)
    num = frac[-1]
    denom = 1
    for _ in range(-2,-len(frac)-1,-1):
        num, denom = frac[_]*num+denom, num
    return (num,denom)

def bitlength(x):
    '''
    Calculates the bitlength of x
    '''
    assert x >= 0
    n = 0
    while x > 0:
        n = n+1
        x = x>>1
    return n

def isqrt(n):
    '''
    Calculates the integer square root
    for arbitrary large nonnegative integers
    '''
    if n < 0:
        raise ValueError('square root not defined for negative numbers')

    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y

def is_perfect_square(n):
    '''
    If n is a perfect square it returns sqrt(n),

    otherwise returns -1
    '''
    h = n & 0xF;  # last hexadecimal "digit"

    if h > 9:
        return -1  # return immediately in 6 cases out of 16.

    # Take advantage of Boolean short-circuit evaluation
    if (h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8):
        # take square root if you must
        t = isqrt(n)
        if t * t == n:
            return t
        else:
            return -1

    return -1

def hack_RSA(e, n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)

    for (k, d) in convergents:

        # check if d is actually the key
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s * s - 4 * n
            if (discr >= 0):
                t = is_perfect_square(discr)
                if t != -1 and (s + t) % 2 == 0:
                    print("Hacked!")
                    return d


e = 65537
n = 71521286555472299312252291246589709247849481750774732993492805730954699131789
p = 273130256889334854338089243490350662083
q = 261857794043121448213410325750790838383
d = 66043993770909144601963534517312602411294055720082623568097196488923525348009
c = 49261759487956473329685313812271645883131850171569790962655880778772489980709
test = print(pow(pow(c, e, n), d, n))
f = (p-1)*(q-1)
res = pow(c, d, n)


e = int('6117c60448b139451ab5b60b6257a12bda90c0960fad1e007d16d8fa43aa5aaa3850fc240e5414ad2ba1090e8e12d6495bbc73a0cba562504255c73ea3fbd36a8883f831da8d1b9b8133ac2109e20628e80c7e53baba4ce5a14298811e70b4a2313c914a2a3217c02e951aaee4c9eb39a3f080357b533a6cca9517cb2b95bfcd', 16)
n = int('03303b790fb149da3406d495ab9b9fb8a9e293445e3bd43b18ef2f0521b726ebe8d838ba774bb5240f08f7fbca0a142a1d4a61ea973294e684a8d1a2cdf18a84f2db7099b8e977588b0b891292558caa05cf5df2bc6334c5ee5083a234edfc79a95c478a78e337c723ae8834fb8a9931b74503ffea9e61bf53d8716984ac47837b', 16)
d = 44217944188473654528518593968293401521897205851340809945591908757815783834933
data = int('01A25FEF76635BDBEA7EE76B5AC4318A07C4A8D134CE49A5395617D1D6BFC65E1547F2C215E428852B334C7522DA54E9020824BEA0C94630EB5650A701D6BE6A40ECB802E1F4C0C97C6A1ACFE499D8E7E5857BC2BEEC7F2C9586F0F4FC5945A9A98D13EFEFAC58380878E6FC2CADEF638F4E2616486C32B9D38DC6E55B6FA41DEE', 16)
res = hex(pow(data, d, n))
print(res)
print(hack_RSA(e, n))