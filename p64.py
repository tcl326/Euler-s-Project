import math


def invert_fraction(sqrt: int, num: int, numerator: int):
    """
    numerator / ( sqrt + num ) => numerator * (sqrt - num) / (sqrt + num) * (sqrt - num) => ( sqrt + num_n ) / denominator_n
    """

    denominator = sqrt - num ** 2
    denominator /= numerator

    return sqrt, -1 * num, denominator


def simplify_fraction(sqrt: int, num: int, denominator: int):
    """
    (sqrt + num) / denominator => a + (sqrt + num_n) / denominator
    """
    a = (math.sqrt(sqrt) + num) / denominator
    a = a // 1

    num_n = num - denominator * a
    return a, sqrt, num_n, denominator


def continued_fraction_sqrt(sqrt: int):
    """
    general structure 

    (sqrt + num_i) / den_i => a_i + 1 / ((sqrt + num_{i + 1}) / den_{i + 1})

    """
    v = math.sqrt(sqrt)
    a_n = v // 1
    denominator_n = 1
    num_n = a_n * -1
    res = [a_n]
    seen = {}
    for i in range(100000):
        _, num_i, denominator_i = invert_fraction(sqrt, num_n, denominator_n)
        a_n, _, num_n, denominator_n = simplify_fraction(sqrt, num_i, denominator_i)
        if (num_n, denominator_n) in seen:
            return res, i - seen[(num_n, denominator_n)]
        seen[(num_n, denominator_n)] = i
        res.append(a_n)
    return res



def main():
    res = 0
    for i in range(2, 10_000 + 1):
        if math.sqrt(i).is_integer():
            continue
        r, p = continued_fraction_sqrt(i)
        print(i, r, p)
        if p % 2 == 1:
            res += 1
    return res




if __name__ == "__main__":
    print(main())
