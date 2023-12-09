import itertools


def main(power: int) -> int:
    max_value = 9 ** power
    value = max_value
    digits = 1
    while digits < len(str(value)):
        digits += 1
        value = max_value * digits
    res = 0
    for i in range(2, digits + 1):
        for ds in itertools.combinations_with_replacement(range(10), i):
            value = sum([d ** power for d in ds])
            print(ds, tuple(sorted([v for v in str(value)])))
            if tuple(sorted([int(v) for v in str(value)])) == ds and len(str(value)) == i:
                res += value
    return res



if __name__ == "__main__":
    print(main(power=5))