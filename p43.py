import itertools
import functools

def is_divisible(n: int, d: int) -> bool:
    return n % d == 0

def is_special(n: int) -> bool:
    n_str = str(n)
    # print(n_str)
    return (
        is_divisible(int(n_str[1:4]), 2)
        and is_divisible(int(n_str[2:5]), 3)
        and is_divisible(int(n_str[3:6]), 5)
        and is_divisible(int(n_str[4:7]), 7)
        and is_divisible(int(n_str[5:8]), 11)
        and is_divisible(int(n_str[6:9]), 13)
        and is_divisible(int(n_str[7:10]), 17)
    )

def main():
    res = 0
    for v in itertools.permutations(range(10), 10):
        if v[0] == 0:
            continue
        value = functools.reduce(lambda a, b: a * 10 + b, v)
        # print(value)
        if is_special(value):
            res += value

    return res

if __name__ == "__main__":
    print(main())
    # print(is_special(1406357289))