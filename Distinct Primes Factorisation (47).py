__author__ = 'student'
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
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

def findPrimeFactorization(n,primeList):
    prime = primeList [0]
    primeFactorization = []
    c = 0
    while prime <= math.ceil(n/2):
        if n%prime == 0:
            primeFactorization.append(prime)
        c+=1
        prime = primeList [c]
    return primeFactorization

def findConsecutiveNumber (n):
    primeList = sieveOfEratosthenes(1000000)
    number = 0
    primeFact1 = findPrimeFactorization(number,primeList)
    while True:
        number += n-1
        primeFact2 = findPrimeFactorization(number,primeList)
        if primeFact1 == primeFact2:
            primeFact1 = primeFact2
            continue
        if len(primeFact1)<n or len(primeFact2)<n:
            primeFact1 = primeFact2
            continue
        j = 1
        while j< n-1:
            notValid = 1
            number1 = number - j
            primeFact3 = findPrimeFactorization(number1,primeList)
            if primeFact3 == primeFact2 or primeFact3 == primeFact1:
                notValid = 0
                break
            if len(primeFact3)<n:
                notValid = 0
                break
            j+=1
        if notValid:
            return number-n+1
print(findConsecutiveNumber(4))