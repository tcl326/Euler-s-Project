from typing import List, Iterator
import itertools

def permutation_without_cycles(digits: List[int]):
    d = digits.pop()
    for p in itertools.permutations(digits):
        yield p + (d, )

def rotate(path):
    min_idx = 0
    min_value = path[0]
    for i, p in enumerate(path):
        if p < min_value:
            min_idx = i
            min_value = p
    
    res = []
    for c in range(len(path)):
        res.append(path[(min_idx + c) % len(path)])
    return res


def five_gon_strings(digits: List[int]) -> Iterator[int]:
    def recurse(i, inner, available, v, path):
        if not available:
            print(rotate(path))
            yield int("".join("".join([str(i) for i in t]) for t in rotate(path)))
        for a in available:
            if a + inner[i] + inner[(i + 1) % len(inner)] != v:
                continue
            yield from recurse(i + 1, inner, available - {a}, v, path + ((a, inner[i], inner[(i + 1) % len(inner)]),))
        

    for c in itertools.combinations(digits, 5):
        available = set(digits) - set(c)
        for p in permutation_without_cycles(list(c)):
            for a in available:
                v = a + p[0] + p[1]
                left = available - {a}
                yield from recurse(1, p, left, v, ((a, p[0], p[1]),))
                



def main():
    res = 0
    for v in five_gon_strings(list(range(1, 10 + 1))):
        if len(str(v)) == 16:
            res = max(v, res)
    return res


if __name__ == "__main__":
    print(main())