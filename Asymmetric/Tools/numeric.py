import math

def inverse_mod( a, m ):
    """Inverse of a mod m."""
    if a < 0 or m <= a: a = a % m
    # From Ferguson and Schneier, roughly:
    c, d = a, m
    uc, vc, ud, vd = 1, 0, 0, 1
    while c != 0:
        q, c, d = divmod( d, c ) + ( c, )
        uc, vc, ud, vd = ud - q*uc, vd - q*vc, uc, vc

    # At this point, d is the GCD, and ud*a+vd*m = d.
    # If d == 1, this means that ud is a inverse.
    assert d == 1
    if ud > 0: return ud
    else: return ud + m

def gcd(a, b):
  """Greatest common divisor using Euclid's algorithm."""
  while a:
    a, b = b % a, a
  return b


def lcm(a, b):
  """Least common multiple of two integers."""

  return (a * b) // gcd(a, b)

res = inverse_mod(65537, 71521286555472299312252291246589709247314493699842276690941306161713557631324)
pass