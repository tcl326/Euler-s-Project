import collections


def get_signature(n: int) -> str:
    c = collections.Counter(str(n))
    return tuple(c.get(str(d), 0) for d in range(10))


def main():
    i = 1
    seen = collections.defaultdict(list)
    while i < 1_000_000:
        c = i * i * i
        sig = get_signature(c)
        seen[sig].append(c)
        i += 1
    res = float('inf')
    for k, v in seen.items():
        if len(v) == 5:
            for c in v:
                res = min(c, res)
    return res

if __name__ == "__main__":
    print(main())