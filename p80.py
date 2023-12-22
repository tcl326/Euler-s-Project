from typing import List

import math
from lib import continued_fractions


def get_sum_of_100_decimals(num, denum) -> List[int]:
    r = []
    while len(r) < 100:
        r.append(num // denum)
        num = (num % denum) * 10
        if num == 0:
            break
    return r


def main(n: int = 100):
    r = 0
    for n in range(1, n + 1):
        if math.sqrt(n).is_integer():
            continue
        a, b = continued_fractions.sqrt(n)
        if not b:
            continue
        digits = []
        while len(digits) < 100:
            a = a + b * (200 // (len(b)))
            # print(a)
            numerator, denominator = continued_fractions.convergent(a)
            # print(numerator, denominator)
            digits = get_sum_of_100_decimals(numerator, denominator)
        r += sum(digits)
        print(digits)
    return r



if __name__ == "__main__":
    print(main(100))
