import math

def main(limit: int) -> int:
    res = -1
    max_soln_cnt = 0
    for p in range(1, limit + 1):
        solns = set()
        for a in range(p // 2 + 1):
            for b in range(p // 2 + 1):
                c = math.sqrt(a ** 2 + b ** 2)
                if (a + b + c) == p:
                    solns.add(tuple(sorted([a, b, c])))
        if len(solns) > max_soln_cnt:
            max_soln_cnt = len(solns)
            res = p
        print(p, solns)
    return res

if __name__ == "__main__":
    print(main(limit=1000))