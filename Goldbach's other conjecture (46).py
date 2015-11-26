__author__ = 'student'
"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

import math
def sieveOfEratosthenes (n):
    assert n > 1
    A = [1 for i in range (n+1)]
    for c in range (2,math.ceil(math.sqrt(n))):
        if A[c]:
            j = c**2
            while j<=n:
                A[j] = 0
                j += c
    return [d for d in range(2,n+1) if A[d]]


def findConjectureProblem ():
    primeList = sieveOfEratosthenes(100000)
    number = 1
    foundProblem = False
    while not foundProblem:
        number += 2
        c = 0
        foundProblem = True
        while number >= primeList[c]:
            if math.sqrt((number-primeList[c])/2)%1 == 0.0:
                foundProblem = False
            c +=1
    return number
print(findConjectureProblem())