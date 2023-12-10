import math

def comb_count(n, r):
    return math.factorial(n) / (math.factorial(r)) / (math.factorial(n - r))

def main():
    res = 0
    for n in range(1, 100 + 1):
        for r in range(1, n + 1):
            if comb_count(n, r) > 1_000_000:
                res += 1
    return res


if __name__ == "__main__":
    print(main())