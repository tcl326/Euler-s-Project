import collections

def letter_set(i: int):
    return collections.Counter(str(i))


def main():
    i = 0
    while True:
        i += 1
        s = letter_set(i)
        if (
            s == letter_set(2 * i)
            and s == letter_set(3 * i)
            and s == letter_set(4 * i)
            and s == letter_set(5 * i)
            and s == letter_set(6 * i)
        ):
            return i


if __name__ == "__main__":
    print(main())