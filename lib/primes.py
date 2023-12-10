"""
Utilities for working with Prime Numbers
"""

def is_prime(n: int) -> bool:
    if (n <= 3):
        return n > 1
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while i * i <= n:
        if (n % i) == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
