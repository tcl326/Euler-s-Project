
import functools
import copy
from lib import seq


def count(a, b):
    if (2 * a < b):
        return 0
    
    if (a >= b):
        return b // 2
    
    return a - (b - 1) // 2



def all_routes(max_len: int):
    memo = [0 for _ in range(max_len + 1)]

    for a, b, _ in seq.primitive_pythagorean_triples():
        if a > max_len or b > max_len:
            break
        k = 1
        while a * k < max_len:
            memo[a * k] += count(a * k, b * k)
            k += 1
        k = 1
        while b * k < max_len:
            memo[b * k] += count(b * k, a * k)
            k += 1
    
    res = copy.deepcopy(memo)
    for i, s in enumerate(res):
        res[i] += res[i - 1]

    return res


def main(limit: int) -> int:
    routes = all_routes(10_000)

    for i, c in enumerate(routes):
        if c > limit:
            print(c)
            return i


if __name__ == "__main__":
    print(main(1_000_000))

