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


if __name__ == '__main__':
    print(sqrt(13))