
def main():
    res = 0
    numerator = 3
    denominator = 2
    for _ in range(1000):
        if len(str(numerator)) > len(str(denominator)):
            res += 1
        prev = denominator
        denominator = numerator + denominator
        numerator = prev + denominator
    return res


if __name__ == "__main__":
    print(main())