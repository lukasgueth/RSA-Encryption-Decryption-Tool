from next_prime import get_next_prime
from random import randint
from public_exponent import get_public_exponent
from extended_euclid import gcdExtended
from encrypt import encrypt
from decrypt import decrypt


def generate_keys():
    d = -1
    while d < 0:
        rand_range = [9999999, 99999999]
        # 1.
        p = get_next_prime(randint(rand_range[0], rand_range[1]))
        q = get_next_prime(randint(rand_range[0], rand_range[1]))

        n = p*q

        # 2.
        m = (p-1)*(q-1)

        # 3.
        e = get_public_exponent(m)

        # 4.
        d = gcdExtended(e, m)[1]
    return {'public_key': [e, n], 'private_key': [d, n]}
