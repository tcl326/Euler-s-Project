"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
__author__ = 'student'

def isPalindrome(n):
    if str(n)[::-1] == str(n):
        return True
    else:
        return False
def dec_to_bin(x):
    return int(bin(x)[2:])
listPalindromeBase10 = []
for i in range(1000000):
    if isPalindrome(i):
        listPalindromeBase10.append(i)
listPalindromeBase10andBase2 = []
for i in listPalindromeBase10:
    if isPalindrome(dec_to_bin(i)):
        listPalindromeBase10andBase2.append(i)
print(sum(listPalindromeBase10andBase2))