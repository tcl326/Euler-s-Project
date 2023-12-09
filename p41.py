from typing import Iterator
import itertools
import functools

from lib.primes import is_prime

def pandigital(digits: int) -> Iterator[int]:
    for v in itertools.permutations(range(1, digits + 1)):
        yield functools.reduce(lambda a, b: a * 10 + b, v)


def main():
    res = 0
    for v in itertools.chain(pandigital(4), pandigital(7)):
        if is_prime(v):
            print(v)
            res = max(v, res)
    return res


if __name__ == "__main__":
    print(main())