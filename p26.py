

def get_recurring_decimals(numerator: int, denominator: int):
    seen_numerator = {numerator}
    numerator *= 10
    decimals = []
    num = numerator // denominator
    rem = numerator % denominator
    decimals.append(num)
    while rem != 0:
        numerator = rem * 10
        decimals.append(numerator // denominator)
        rem = numerator % denominator
        if rem in seen_numerator:
            return decimals
        seen_numerator.add(rem)
    return decimals
            


if __name__ == "__main__":
    longest = 0
    res = 0
    for i in range(1, 1000):
        d = get_recurring_decimals(1, i)
        print(i, d)
        if len(d) > longest:
            longest = len(d)
            res = i
    print(res)