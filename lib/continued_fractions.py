"""
libraries to work with continued fraction representation of different numbers
"""

from typing import Tuple, List

import math


def sqrt(s: int) -> Tuple[List[int], List[int]]:
    """
    continued fraction representation of the square root
    of the given number 's'

    based on the formula listed here: https://en.wikipedia.org/wiki/Periodic_continued_fraction

    returns [non-repeating sequence], [repeating sequence]
    """
    m_0 = 0
    d_0 = 1
    s_sqrt = math.sqrt(s)
    a_0 = int(s_sqrt)
    i = 0
    seen = {(a_0, m_0, d_0): i}
    a_list = [a_0]
    while d_0:
        m_n = d_0 * a_0 - m_0
        d_n = (s - m_n ** 2 ) / d_0
        a_n = int((s_sqrt + m_n) / d_n)
        i += 1
        if (a_n, m_n, d_n) in seen:
            start = seen[(a_n, m_n, d_n)]
            end = i
            return a_list[:start], a_list[start:end]
        seen[(a_n, m_n, d_n)] = i
        a_list.append(a_n)
        d_0 = d_n
        a_0 = a_n
        m_0 = m_n
        
    return a_list


def fraction(a: int, b: int) -> Tuple[List[int], List[int]]:
    a_list = []
    if a < b:
        a, b = b, a
        a_list.append(0)
    r = a % b
    while r != 0:
        a_list.append(a // b)
        a = b
        b = r
        r = a % b
    a_list.append(a // b)
    return a_list, []


def convergent(a: List[int]) -> Tuple[int, int]:
    """
    https://pi.math.cornell.edu/~gautam/ContinuedFractions.pdf

    based on theorem Theorem 2.4.
    """
    assert a, 'a cannot be empty'
    p_0 = a[0]
    q_0 = 1
    if len(a) == 1:
        return p_0, q_0
    p_1 = a[1] * a[0] + 1
    q_1 = a[1]
    for i in range(2, len(a)):
        p_n = a[i] * p_1 + p_0
        q_n = a[i] * q_1 + q_0
        p_0, q_0, p_1, q_1 = p_1, q_1, p_n, q_n
    return p_1, q_1


if __name__ == '__main__':
    print(sqrt(13))
    print(fraction(43, 19))
    print(convergent([2, 3, 1, 4]))