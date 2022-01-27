from math import sqrt

def gen_primes(limit):
    """
    Python generator that yields all prime numbers
    that are less than or equal to limit.
    Uses minimal memory.
    """
    if limit < 2:
        return
    i = 2
    yield 2
    i += 1
    while i <= limit:
        is_prime = True
        for j in range(3, int(sqrt(i)+1), 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i
        i += 2
