import functools


def main():
    res = 0
    for a in range(100):
        for b in range(100):
            r = a ** b
            res = max(res, int(functools.reduce(lambda a, b: int(a) + int(b), str(r))))
    return res

if __name__ == "__main__":
    print(main())