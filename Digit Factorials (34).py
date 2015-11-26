"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
__author__ = 'student'
import math
def sumOfFactorials (number):
    numberList = list(str(number))
    return sum([math.factorial(int(i)) for i in numberList])
sumOfNumbers = 0
for i in range(3,2540161):
    if sumOfFactorials(i) == i:
        sumOfNumbers+=i
print (sumOfNumbers)