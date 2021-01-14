from is_prime import is_prime


def get_next_prime(start_int):
    n = start_int

    while is_prime(n) == False:
        n += 1

    return n
