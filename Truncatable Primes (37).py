"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

__author__ = 'student'

from math import sqrt; from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    return all(n%i for i in islice(count(2), int(sqrt(n)-1)))
def isRightTruncatablePrime (n):
    return all(isPrime(i) for i in [int(str(n)[:c+1]) for c in range(len(str(n)))])
def isLeftTruncatablePrime (n):
    return all(isPrime(i) for i in [int(str(n)[c:]) for c in range(len(str(n)))])


print(isLeftTruncatablePrime(71))

rightLeftTruncatablePrime = []
rightTruncatablePrime = []
start = 20
while len(rightLeftTruncatablePrime) != 11:
    if isPrime(start):
        if isRightTruncatablePrime(start) and isLeftTruncatablePrime(start):
            rightLeftTruncatablePrime.append(start)
    start+=1
print(sum(rightLeftTruncatablePrime))
print(rightLeftTruncatablePrime)