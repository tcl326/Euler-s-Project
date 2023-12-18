

def mediant(a, b, c, d):
    """
    based on https://en.wikipedia.org/wiki/Mediant_(mathematics)
    The idea is that the mediant of two fraction is always between
    the two given fractions. So repeatdly finding the mediant of
    two fractions will return a value as close as possible to 3 / 7
    """
    return a + c, b + d


def main():
    a, b, c, d = 2, 5, 3, 7
    n = 1_000_000
    i = 0
    an, bn = mediant(a, b, c, d)
    while bn <= n:
        a, b = an, bn
        an, bn = mediant(a, b, c, d)
        i += 1
        print(i, f"{a}/{b}")
    return a, b

if __name__ == "__main__":
    print(main())
