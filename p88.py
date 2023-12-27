
from typing import Iterable, Tuple, List
import heapq
import math
import tqdm


def product_set_sequence(n: int) -> Iterable[Tuple[int, List[int]]]:
    r = tuple([1 for _ in range(n)])
    product = 1
    queue = [(product, r)]
    seen = set()
    while queue:
        product, r = heapq.heappop(queue)
        yield product, r
        for i in range(len(r)):
            if i == 0 or r[i - 1] > r[i]:
                n_r = r[:i] + (r[i] + 1, ) + r[i + 1:]
                if n_r in seen:
                    continue
                n_p = math.prod(n_r)
                seen.add(n_r)
                heapq.heappush(queue, (n_p, n_r))


def divisors(n: int) -> List[int]:
    divs = [n]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            divs.append(n // i)
    return sorted(set(divs))



def possible_factor_size(n: int) -> List[int]:
    memo = {}
    def recurse(original, curr, prod, _sum, count):
        if (original, curr, prod, _sum, count) in memo:
            return memo[(original, curr, prod, _sum, count)]
        possibles = []
        if prod > original or _sum > original:
            return []
        
        if prod == original and _sum == original:
            memo[(original, curr, prod, _sum, count)] = [count]
            return [count]
        
        if curr == 1:
            return [count + (original - _sum)]
        
        for d in divisors(curr):
            possibles += recurse(original, curr // d, prod * d, _sum + d, count + 1)
        memo[(original, curr, prod, _sum, count)] = possibles
        return possibles
    return recurse(n, n, 1, 0, 0)


def main(lower: int, upper: int) -> int:
    minimal_sum = {}

    for n in range(4, 2 * upper + 1):
        for set_size in set(possible_factor_size(n)):
            minimal_sum[set_size] = min(minimal_sum.get(set_size, float('inf')), n)
    res = set()
    # print(minimal_sum)
    for i in range(lower, upper):
        res.add(minimal_sum[i])
    return sum(res)

if __name__ == "__main__":
    print(main(2, 12_000))
