import math

from lib import continued_fractions


def main():
    res = 0
    for i in range(2, 10_000 + 1):
        if math.sqrt(i).is_integer():
            continue
        _, p = continued_fractions.sqrt(i)
        if len(p) % 2 == 1:
            res += 1
    return res


if __name__ == "__main__":
    print(main())
