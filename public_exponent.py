from gcd import gcd
from is_prime import is_prime


def get_public_exponent(m):
    n = m-1

    while n > 0:
        if gcd(n, m) == 1 and is_prime(n):
            return n

        n -= 1

    return -1
