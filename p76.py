
def main(n: int) -> int:
    seen = {}

    def recurse(v: int, m: int):
        if v == 0:
            return 0
        if v == 1:
            return 1
        if (v, m) in seen:
            return seen[(v, m)]
        r = 0
        for i in range(m, 0, -1):
            r += recurse(v - i, min(v - i, i))
        if v <= m:
            r += 1
        seen[(v, m)] = r
        return r

    res = recurse(n, n)
    print(seen)
    return res - 1
        


if __name__ == "__main__":
    print(main(100))