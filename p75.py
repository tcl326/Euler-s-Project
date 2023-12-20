from typing import Iterable, Tuple
import collections
import heapq

def odd_odd_co_prime_pair() -> Iterable[Tuple[int, int]]:
    """
    https://en.wikipedia.org/wiki/Coprime_integers#Generating_all_coprime_pairs
    """
    min_heap = [(3, 1)]
    while True:
        m, n = heapq.heappop(min_heap)
        yield (m, n)
        heapq.heappush(min_heap, (2 * m - n, m))
        heapq.heappush(min_heap, (2 * m + n, m))
        heapq.heappush(min_heap, (m + 2 * n, n))


def primitive_pythagorean_triples() -> Iterable[Tuple[int, int, int]]:
    """
    https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
    """
    for m, n in odd_odd_co_prime_pair():
        m2 = m ** 2
        n2 = n ** 2
        yield sorted((m * n, (m2 - n2) // 2, (m2 + n2) // 2))



def main(n: int) -> int:
    counter = collections.Counter()
    p_s = 0
    for a, b, c in primitive_pythagorean_triples():
        s = a + b + c
        if s > n * 2:
            break
        k = 1
        while k * s <= n:
            counter[s * k] += 1
            k += 1
    r = sum([1 for c in counter.values() if c == 1])
    # print(counter)
    return r
        

if __name__ == "__main__":
    print(main(1_500_000))
    # print(main(120))
