from typing import Iterator, List

import itertools
import collections

def triangle_number(max_value: int) -> Iterator:
    n = 1
    v = 0
    while v < max_value:
        v = n * ( n + 1 ) // 2
        yield v
        n += 1


def square_number(max_value: int) -> Iterator:
    n = 1
    v = 0
    while v < max_value:
        v = n * n
        yield v
        n += 1

def pentagonal_number(max_value: int) -> Iterator:
    n = 1
    v = 0
    while v < max_value:
        v = n * ( 3 * n - 1 ) // 2
        yield v
        n += 1


def hexagonal_number(max_value: int) -> Iterator:
    n = 1
    v = 0
    while v < max_value:
        v = n * ( 2 * n - 1 )
        yield v
        n += 1

def heptagonal_number(max_value: int) -> Iterator:
    n = 1
    v = 0
    while v < max_value:
        v = n * ( 5 * n - 3 ) // 2
        yield v
        n += 1

def octagonal_number(max_value: int) -> Iterator:
    n = 1
    v = 0
    while v < max_value:
        v = n * ( 3 * n - 2 )
        yield v
        n += 1


def get_first_two_digits_map(numbers: List[int]):
    r = collections.defaultdict(set)
    for n in numbers:
        two_digits = n // 100
        r[two_digits].add(n)
    return r


def main():
    triangles = [t for t in triangle_number(max_value=10_000) if t > 999]
    squares = [s for s in square_number(max_value=10_000) if s > 999]
    pentagons = [p for p in pentagonal_number(max_value=10_000) if p > 999]
    hexagons = [h for h in hexagonal_number(max_value=10_000) if h > 999]
    heptagons = [h for h in heptagonal_number(max_value=10_000) if h > 999]
    octagons = [o for o in octagonal_number(max_value=10_000) if o > 999]

    tr_maps = get_first_two_digits_map(triangles)
    sq_maps = get_first_two_digits_map(squares)
    pe_maps = get_first_two_digits_map(pentagons)
    hex_maps = get_first_two_digits_map(hexagons)
    hep_maps = get_first_two_digits_map(heptagons)
    oct_maps = get_first_two_digits_map(octagons)

    for p in itertools.permutations([tr_maps, sq_maps, pe_maps, hex_maps, hep_maps, oct_maps], 6):
        m1, m2, m3, m4, m5, m6 = p
        for t in itertools.chain(*m1.values()):
            print(t)
            t_2 = t % 100
            for s in m2.get(t_2, set()):
                s_2 = s % 100
                for p in m3.get(s_2, set()):
                    print(t, s, p)
                    p_2 = p % 100
                    for hex in m4.get(p_2, set()):
                        hex_2 = hex % 100
                        for hep in m5.get(hex_2, set()):
                            hep_2 = hep % 100
                            for o in m6.get(hep_2, set()):
                                o_2 = o % 100
                                print(t, s, p, hex, hep, o)
                                if o_2 == t // 100:
                                    return t + s + p + hex + hep + o
    print(tr_maps)
    print(sq_maps)
    return -1



if __name__ == "__main__":
    print(main())