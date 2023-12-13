from typing import Iterator
import functools

from lib.continued_fractions import convergent

def e_continued_fraction(n: int) -> Iterator[int]:
    yield 2
    k = 1
    c = 1
    while c < n:
        if (c - 2) % 3 == 0:
            yield 2 * k
            k += 1
        else:
            yield 1
        c += 1


def main(n: int) -> int:
    num, _ = convergent(list(e_continued_fraction(n)))
    return functools.reduce(lambda a, b: int(a) + int(b), str(num))


if __name__ == "__main__":
    print(main(100))
