__author__ = 'student'
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
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

def consecutivePrimeSum(n):
    listOfPrime = sieveOfEratosthenes(n)
    j = 0
    largestPrime = 0
    longestConsecutivePrime = 0
    while j <= len(listOfPrime):
        j+=1
        c = longestConsecutivePrime+j
        numberOfSum = longestConsecutivePrime
        primeSum = sum(listOfPrime[j:c])
        while primeSum <= n and c < len(listOfPrime):
            primeSum += listOfPrime[c]
            numberOfSum += 1
            c+= 1
            if primeSum in listOfPrime and numberOfSum > longestConsecutivePrime:
                largestPrime = primeSum
                longestConsecutivePrime = numberOfSum
    return largestPrime
print(consecutivePrimeSum(1000000))