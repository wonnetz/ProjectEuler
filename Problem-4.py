"""
Coded by Wonnetz Phanthavong
Title: Largest Palindrome Product
Difficulty Rating: 5%
Question:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


import math
pal = []
count = 0

# This nested for loop iterates through the number 100 - 999 twice
for i in range(100, 999):
    for j in range(100, 999):
        product = i * j
        digits = int(math.log10(product)) + 1
        str1 = str(product)
        if digits % 2 == 0: # Considers the case when the number of digits are odd
            n = digits / 2
            for k in range(0, int(n)): # Checks if the digits are identical in the forward and backward position
                if str1[k] == str1[len(str1) - k - 1]:
                    count = count + 1
                if count == n:
                    pal.append(product)
            count = 0
        else: # Considers the case when the number of digits are odd
            n = (digits - 1) / 2
            for k in range(0, int(n)): #Checks if the digits are identical in the forward and backward position
                if str1[k] == str1[len(str1) - k - 1]:
                    count = count + 1
                if count == n:
                    pal.append(product)
            count = 0
print(max(pal))

"""
Output: 906609
"""