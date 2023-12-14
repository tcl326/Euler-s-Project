from typing import Tuple
from lib import continued_fractions
import math

def minimal_solution(n: int) -> Tuple[int, int]:
    a, rep = continued_fractions.sqrt(n)
    a_list = a
    found = False
    i = 0
    while not found:
        num, den = continued_fractions.convergent(a_list)
        if num ** 2 - n * den ** 2 == 1:
            return num
        a_list.append(rep[i % len(rep)])
        i += 1

def main(n: int) -> int:
    res = 0
    min_sol = 0
    for d in range(2, n + 1):
        if math.sqrt(d).is_integer():
            continue
        sol = minimal_solution(d)
        print(d, sol)
        if min_sol < sol:
            res = d
            min_sol = sol
    return res, min_sol

if __name__ == "__main__":
    print(main(1000))
