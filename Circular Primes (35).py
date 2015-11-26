"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
__author__ = 'student'

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

def rotate(string,n):
    return string[n:] + string[:n]

print(rotate("12",0))
collected = []
allPrimeUnderOneMillion = sieveOfEratosthenes(1000000)

for i in allPrimeUnderOneMillion:
    if i in collected:
        continue
    allRotation = [int(rotate(str(i),numRotations)) for numRotations in range(len(str(i)))]

    if set(allRotation).issubset( allPrimeUnderOneMillion ):
        collected += allRotation
print(len(set(collected)))