import math


def get_pentagon_number(n: int) -> int:
    return n * ( 3 * n - 1 ) / 2


def is_pentagon_number(p: int) -> bool:
    """
    P_n = n * (3 * n - 1) / 2
    => 0 = 3 * n ^ 2 - n - 2 * P_n
    => n = (1 + math.sqrt(1 + 24 * P_n)) / 6 as n can only be positive
    """
    n = (1 + math.sqrt(1 + 24 * p)) / 6
    return n.is_integer()


def main():
    i = 0
    while True:
        i += 1
        a = get_pentagon_number(i)
        for j in range(i - 1, 0, -1):
            b = get_pentagon_number(j)
            s = a + b
            d = a - b
            if is_pentagon_number(s) and is_pentagon_number(d):
                return int(d)
    return -1


if __name__ == "__main__":
    print(main())
