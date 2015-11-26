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

def findPermutations(listOfNumbers):
    permutationsDict = {}
    addedIndex = []
    for i in range(len(listOfNumbers)):
        if i in addedIndex:
            continue
        permutationsDict[str(listOfNumbers[i])] = [listOfNumbers[i]]
        j = i+1
        while j < len(listOfNumbers):
            if sorted(str(listOfNumbers[i])) == sorted(str(listOfNumbers[j])):
                addedIndex.append(j)
                permutationsDict[str(listOfNumbers[i])].append(listOfNumbers[j])
            j+=1
    return permutationsDict

def primePermutations():
    listOfValidPerm = []
    primes = sieveOfEratosthenes(10000)
    for i in range(len(primes)):
        if primes[i] > 999:
            primes = primes[i:]
            break
    permutationDict = findPermutations(primes)
    validPermutation = []
    for key, value in permutationDict.items():
        if len(value) >= 3:
            validPermutation.append(value)
    for i in validPermutation:
        for c in range(len(i)):
            j = c+1
            while j< len(i):
                if 2*i[j]-i[c] in i:
                    listOfValidPerm.append([i[c],i[j],2*i[j]-i[c]])
                j+=1
    return listOfValidPerm
print(primePermutations())