

def farey_sequence(n: int, descending: bool = False) -> None:
    """Print the n'th Farey sequence. Allow for either ascending or descending."""
    a, b, c, d = 0, 1, 1, n
    if descending:
        a, c = 1, n - 1
    while c <= n and not descending or a > 0 and descending:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        yield a, b


def main(n: int) -> int:
    start = 1 / 3
    end = 1 / 2

    r = 0
    for a, b in farey_sequence(n):
        v = a / b
        if v >= end:
            break
        if v > start:
            print(f"{a}/{b}")
            r += 1
    return r


if __name__ == "__main__":
    print(main(12_000))