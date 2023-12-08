"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16 the smallest
number that can be weritten as the sum of two abundant number is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be weritten as the
sum of two abundant numbers.
"""
from typing import List
import math


abundant_numbers = {}

def get_all_proper_divisors(n: int) -> List[int]:
    divisors = []
    if n == 1:
        return divisors
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    # print(divisors)
    return divisors

def is_abundant(n: int) -> bool:
    if sum(get_all_proper_divisors(n)) > n:
        return True
    return False

def is_sum_of_two_abundant(n: int) -> bool:
    for a in abundant_numbers.keys():
        if a > (n // 2 + 1):
            return False
        if (n - a) in abundant_numbers:
            return True
    return False

def main():
    res = 0
    not_sum_of_two_abundant = []
    for i in range(1, 28123 + 1):
        if not is_sum_of_two_abundant(i):
            res += i
            not_sum_of_two_abundant.append(i)
        if is_abundant(i):
            abundant_numbers[i] = None
    print(not_sum_of_two_abundant[:100])
    print(list(abundant_numbers)[:100])
    return res


if __name__ == "__main__":
    print(main())