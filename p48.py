
def square_number(n, last_n: int = 10) -> int:
    m = 10 ** last_n
    v = 1
    for _ in range(n):
        v *= n
        v = v % m
    return v


def main():
    s = 0
    for i in range(1, 1000 + 1):
        s += square_number(i, 10)
    return s % 10 ** 10

if __name__ == "__main__":
    print(main())