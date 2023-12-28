
from typing import List, Set

import math
import functools
import itertools

import tqdm


@functools.cache
def combination(n: int, k: int) -> int:
    return math.factorial(n) / (math.factorial(k) * (math.factorial(n - k)))


digits = {
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
}

square_digits = {
    "01", "04", "09", "16", "25", "36", "49", "64", "81"
}


def main():
    r = 0
    seen = set()

    def is_possible(c1: Set[str]) -> bool:
        c = 0
        for sq in square_digits:
            for d in sq:
                if d in c1 or ((d == "9" or d == "6") and ("9" in c1 or "6" in c1)):
                    c += 1
                    break
        return c == len(square_digits)

    def get_rem(c1: Set[str], c2: Set[str], rem: Set[str]) -> Set[str]:
        res = set()
        for r in rem:
            r1, r2 = r
            if r1 == "6" or r1 == "9":
                if (("6" in c1 or "9" in c1) and r2 in c2) or (r2 in c1 and ("6" in c2 or "9" in c2)):
                    continue
            if r2 == "6" or r2 == "9":
                if (("6" in c1 or "9" in c1) and r1 in c2) or (r1 in c1 and ("6" in c2 or "9" in c2)):
                    continue
            if (r1 in c1 and r2 in c2) or (r2 in c1 and r1 in c2):
                continue
            res.add(r)
        return res


    def recurse(c1: Set[str], c2: Set[str], rem: Set[str], avail: Set[str]):
        if len(c2) == 6:
            if not rem:
                seen.add(tuple(sorted([tuple(sorted(c1)), tuple(sorted(c2))])))
            return
        for d in avail:
            c2.add(d)
            recurse(c1, c2, get_rem(c1, c2, rem), avail - {d, })
            c2.discard(d)
        return

    for comb in tqdm.tqdm(itertools.combinations(list(digits), 6)):
        comb = set(comb)
        if is_possible(comb):
            # print(comb)
            recurse(comb, set(), square_digits, digits)
    print(seen)
    return len(seen)




if __name__ == "__main__":
    print(main())