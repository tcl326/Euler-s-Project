
import tqdm

def main(limit: int) -> int:
    seen = {}

    def recurse(i: int) -> int:
        if i == 1 or i == 89:
            return i
        if i in seen:
            return seen[i]
        
        n = 0
        for d in str(i):
            n += int(d) ** 2
        res = recurse(n)
        seen[i] = res
        return res

    r = 0
    for i in tqdm.tqdm(range(1, limit)):
        if recurse(i) == 89:
            r += 1
    return r


if __name__ == "__main__":
    print(main(10_000_000))
