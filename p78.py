
from typing import Iterable

def generalized_pentagonal_numbers() -> Iterable[int]:
    a = 1
    while True:
        yield a, a * (3 * a - 1) // 2
        a = a * -1
        yield a, a * (3 * a - 1) // 2
        a = a * -1
        a += 1


def main(n: int) -> int:
    seen = {}
    seen[0] = 1
    i = 1
    while True:
        r = 0
        for k, g in generalized_pentagonal_numbers():
            if (i - g) < 0:
                break
            r += int((-1) ** (k - 1)) * seen[i - g] % n
        seen[i] = r
        if r % n == 0:
            return i, r
        i += 1

if __name__ == "__main__":
    print(main(1_000_000))
