__author__ = 'student'
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
def checkPandigital(number):
    numberList = set(str(number))
    if "0" in number:
        return False
    if len(numberList) != 9:
        return False
    else:
        return True

p = set()
for i in range(2,  60):
    start = 1234 if i < 10 else 123
    for j in range(start, 10000//i):
        if checkPandigital(str(i) + str(j) + str(i*j)): p.add(i*j)

print ("Sum of products =", sum(p), p)
