"""
Utilities for working with Prime Numbers
"""
import random
import math


def is_prime(n: int) -> bool:
    if (n <= 3):
        return n > 1
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while i * i <= n:
        if (n % i) == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def miller_rabin_test(n: int, k: int = 4) -> bool:
    """
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d = d // 2
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        for _ in range(s):
            y = (x ** 2) % n
            if y == 1 and x != 1 and x != (n - 1):
                return False
            x = y
        if y != 1:
            return False
    return True


def sieve_of_eratosthenes(max_n: int = 100000):
    primes = [True] * max_n
    for i in range(2, int(math.sqrt(max_n)) + 1):
        if primes[i]:
            for j in range(i ** 2, max_n, i):
                primes[j] = False
            yield i
    for i in range(int(math.sqrt(max_n)) + 1, max_n):
        if primes[i]:
            yield i


if __name__ == "__main__":
    # for p in sieve_of_eratosthenes():
    def test(method: str = "default"):
        if method == "miller":
            t = miller_rabin_test
        else:
            t = is_prime
        for p in sieve_of_eratosthenes(1000000):
            assert t(p)

    import timeit
    print("default")
    print(timeit.timeit("is_prime(999_999_000_0001)", setup="from __main__ import is_prime", number=3))
    print("miller-karbin")
    print(timeit.timeit("miller_rabin_test(999_999_000_001)", setup="from __main__ import miller_rabin_test", number=3))
    
    print("default")
    print(timeit.timeit("test()", setup="from __main__ import test", number=1))
    print("miller-karbin")
    print(timeit.timeit("test('miller')", setup="from __main__ import test", number=1))
